from __future__ import division

import networkx as nx
import os
import sys
import subprocess
import socket
import threading
import time
from route import Scenario
import json
from decimal import Decimal, ROUND_HALF_UP
from Constants import *
from geography import GeoTiff, OpenSteetMap, Coordinates
from general import Saves
from route import Graph_Collect
from simulation import Map_Simulation
import osmnx as ox
import matplotlib.pyplot as plt
from route import Graph
import inspect
from route.Heuristics import nearest_neighbor as nn
from route.Heuristics import closest_insertion as ci
from route.Heuristics import farthest_insertion as fi


if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Environment variable SUMO_HOME not defined")

sys.path.append(os.path.join('/home/-/sumo-1.8.0/tools'))

import traci


class UnusedPortLock:
    lock = threading.Lock()

    def __init__(self):
        self.acquired = False

    def __enter__(self):
        self.acquire()

    def __exit__(self):
        self.release()

    def acquire(self):
        if not self.acquired:
            UnusedPortLock.lock.acquire()
            self.acquired = True

    def release(self):
        if self.acquired:
            UnusedPortLock.lock.release()
            self.acquired = False


def find_unused_port():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.bind(('127.0.0.1', 0))
    sock.listen(socket.SOMAXCONN)
    ipaddr, port = sock.getsockname()
    sock.close()
    return port


def terminate_sumo(sumo):
    if sumo.returncode is not None:
        os.system("taskkill.exe /F /im sumo.exe")
        time.sleep(1)


def calculate_power(G, dict_edges_net, id_edge, vehicle_mass, speed):

    nodes = Map_Simulation.edges_to_nodes(id_edge, dict_edges_net)
    data_edge = G.get_edge_data(nodes[0], nodes[1])

    slope = data_edge.get(0).get('grade')
    surface_floor = data_edge.get(0).get('surface')

    current_force = Graph.force(vehicle_mass, surface_floor, slope)
    power = current_force * speed

    return power


def time_streets(G, dict_edges_net, id_edge):
    nodes = Map_Simulation.edges_to_nodes(id_edge, dict_edges_net)
    data_edge = G.get_edge_data(nodes[0], nodes[1])

    max_speed = data_edge.get(0).get('maxspeed')

    return float(max_speed)


def calculate_length(G, dict_edges_net, id_edge):
    nodes = Map_Simulation.edges_to_nodes(id_edge, dict_edges_net)
    data_edge = G.get_edge_data(nodes[0], nodes[1])

    return data_edge.get(0).get('length')


def run(route, G, dict_edges_net, file_name_json, edges_weight, impedance):

    power = []

    dicionario_power = {}
    pdf_power_dict = {}
    pdf_max_speed_dict = {}

    incline = {}
    inclination = []
    total = 0

    total_length = 0
    before_edge_id = 0

    step = 1
    max_speeds = []

    dados = []

    vehicle_weight = VEHICLE_MASS
    path_traveled = []
    edge_mass_ok = []

    vehicle_id = "carrinheiro"

    traci.route.add("path", route)
    traci.vehicle.add(vehicle_id, "path")
    traci.vehicle.setParameter("carrinheiro", "carFollowModel", "KraussPS")
    traci.vehicle.setVehicleClass(vehicle_id, "ignoring")
    traci.vehicle.setShapeClass(vehicle_id, VEHICLE)
    traci.vehicle.setEmissionClass(vehicle_id, "Zero")
    traci.vehicle.setMaxSpeed(vehicle_id, 1)

    while step == 1 or traci.simulation.getMinExpectedNumber() > 0:

        speed = traci.vehicle.getSpeed("carrinheiro")

        if speed < 0:
            speed = float(0)

        slope = traci.vehicle.getSlope(vehicle_id)

        total += 1

        x, y, z = traci.vehicle.getPosition3D(vehicle_id)
        dados.append({"x": x, "y": y, "z": z, "slope": slope})

        edge_id = traci.vehicle.getRoadID(vehicle_id)
        if len(edge_id) > 0 and step > 1 and edge_id[0] != ":":

            if step > 1 and edge_id[0] != ":":

                inclination.append(z)
                power.append(calculate_power(G, dict_edges_net, edge_id, vehicle_weight, speed))

                max_speeds.append(time_streets(G, dict_edges_net, edge_id))

                if edge_id != before_edge_id:

                    total_length += calculate_length(G, dict_edges_net, edge_id)

                    index_must_be = len(path_traveled)
                    index_edge_in_route = route.index(edge_id)
                    if index_must_be != index_edge_in_route:
                        must_be_set = set(route[index_must_be:index_edge_in_route])
                        missing = [a for a in must_be_set if a not in edge_mass_ok and a in list(edges_weight.keys())]
                        if len(missing) > 0:
                            for item in missing:
                                vehicle_weight += edges_weight.get(item)
                                edge_mass_ok.append(item)

                    # if the edge is a stop point and the edge has not yet been traveled
                    if edge_id in list(edges_weight.keys()) and edge_id not in edge_mass_ok:

                        # the vehicle needs to stop to pick up the material
                        traci.vehicle.slowDown(vehicle_id, 0, 10)

                        # weight is added to the vehicle
                        vehicle_weight += edges_weight.get(edge_id)
                        edge_mass_ok.append(edge_id)

                    before_edge_id = edge_id
                    path_traveled.append(edge_id)
        traci.simulationStep()
        vehicles = traci.simulation.getEndingTeleportIDList()

        for vehicle in vehicles:
            traci.vehicle.remove(vehicle, reason=4)

        step += 1

    for i in range(len(power)):
        sett = {i: power[i]}
        dicionario_power.update(sett)

    for i in range(len(inclination)):
        set2 = {i: inclination[i]}
        incline.update(set2)

    # PDF
    max_power = max(power)
    pdf_power = [0] * (int(max_power) + 10)

    max_speed = max(max_speeds)
    pdf_max_speeds = [0] * (int(max_speed) + 10)

    for i in power:
        num = Decimal(float(i)).quantize(0, ROUND_HALF_UP)
        pdf_power[int(num)] += 1

    for i in range(len(pdf_power)):
        pdf_power[i] = (pdf_power[i] / len(power)) * 100
        sett = {i: pdf_power[i]}
        pdf_power_dict.update(sett)

    for i in max_speeds:
        pdf_max_speeds[int(i)] += 1

    for i in range(len(pdf_max_speeds)):
        pdf_max_speeds[i] = (pdf_max_speeds[i] / len(max_speeds)) * 100
        sett = {i: pdf_max_speeds[i]}
        pdf_max_speed_dict.update(sett)

    traci.close()
    sys.stdout.flush()
    write_json(pdf_power_dict, file_name_json + '_pdf' + '_speed_')
    write_json(pdf_max_speed_dict, file_name_json + '_pdf_speeds_')
    write_json(dicionario_power, file_name_json)
    write_json(incline, file_name_json + '_i')

    return total_length


def start_simulation(sumo, scenario, output, route, G, dict_edges_net, file_name_json, edges_weight, impedance):
    unused_port_lock = UnusedPortLock()
    unused_port_lock.__enter__()
    remote_port = find_unused_port()

    sumo = subprocess.Popen(
        [sumo, "-n", scenario, '-r', 'simulation/map.rou.xml', "--tripinfo-output", output, "--device.emissions.probability", "1.0", "--remote-port",
         str(remote_port), "--duration-log.statistics", "--log", "logfile.txt"], stdout=sys.stdout, stderr=sys.stderr)
    unused_port_lock.release()

    try:
        traci.init(remote_port)
        length_total = run(route, G, dict_edges_net, file_name_json, edges_weight, impedance)
    except Exception as e:
        print(e)
        raise
    finally:
        terminate_sumo(sumo)
        unused_port_lock.__exit__()

    return length_total


def write_json(content, fileName):
    with open(fileName + '.json', 'w') as json_file:
        json.dump(content, json_file, separators=(',', ':'), ensure_ascii=False, sort_keys=True, indent=4)


def geotiff_transformation(name_file_in, name_file_out):

    gdal_command = "gdal_translate -of GTiff -ot Int16 -co TFW=YES " + name_file_in + " " + name_file_out
    process_gdal = subprocess.Popen(gdal_command.split(), stdout=subprocess.PIPE)
    output, error = process_gdal.communicate()


def netconvert_geotiff(name_file_osm, name_file_geotiff, name_file_output):

    netconvert_command = "netconvert --osm-files " + name_file_osm + " --heightmap.geotiff " + name_file_geotiff + " -o " + name_file_output # + " -t " + " map.typ.xml "
    process_netconvert = subprocess.Popen(netconvert_command.split(), stdout=subprocess.PIPE)
    output, error = process_netconvert.communicate()