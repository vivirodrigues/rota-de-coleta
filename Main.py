from __future__ import division

import networkx as nx
import pytest_benchmark as benchmark
import os
import sys
import subprocess
import random
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
import cProfile
from route.Heuristics import nearest_neighbor as nn
from route.Heuristics import closest_insertion as ci
from route.Heuristics import further_insertion as fi


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
                        traci.vehicle.slowDown(vehicle_id, 0, 5)

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
    """
    sumo = subprocess.Popen(
        [sumo, "-c", scenario, "--tripinfo-output", output, "--device.emissions.probability", "1.0", "--remote-port",
         str(remote_port), "--duration-log.statistics", "--log", "logfile.txt"], stdout=sys.stdout, stderr=sys.stderr)
    unused_port_lock.release()

    length_total = 0
    """

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


def verify_graph_exists(file_name, file_coords): #, stop_points, coordinates_list):
    try:
        G = ox.load_graphml(file_name)
        f = open(file_coords + '.json', "r")
        dados = json.loads(f.read())
        f.close()
        #lats = [a_tuple[0] for a_tuple in stop_points]
        #lons = [a_tuple[1] for a_tuple in stop_points]
        #nodes = [(n, d) for n, d in G.nodes(data=True) if d['y'] in lats and d['x'] in lons]
        #if len(nodes) == len(stop_points):
        return True
    except:
        pass
    return False


def nodes_data(file_name, net_file, material_weights, file_osm, geotiff, file):

    G = ox.load_graphml(file_name)
    #ox.plot_graph(G)
    G = Scenario.simulation_edit_graph(G, file_osm, net_file)
    #ox.plot_graph(G)

    nodes_coordinates = {}
    nodes_mass_increment = {}
    try:
        f = open(file + '.json', "r")
        dados = json.loads(f.read())
        f.close()
    except:
        dados = 0
        pass

    dados = dict(dados)
    tam = len(list(dados.values()))
    dados = list(dados.values())[:tam-2]

    [nodes_coordinates.update([(int(d[0][2]), (d[0][0], d[0][1]))]) \
     for d in list(dados)]

    [nodes_mass_increment.update([(int(d[0][2]), int(d[0][3]))]) \
     for d in list(dados)]

    # sorts the ids of the nodes that will be inserted in the osm file
    nodes_coordinates = dict(sorted(nodes_coordinates.items(), key=lambda item: item[0]))
    nodes_mass_increment = dict(sorted(nodes_mass_increment.items(), key=lambda item: item[0]))

    id_1adjacent_street1 = 40000000000
    id_1adjacent_street2 = 50000000000
    id_2adjacent_street1 = 60000000000
    id_2adjacent_street2 = 70000000000

    tree = Map_Simulation.parse_file_tree(file_osm)
    osm_tag = tree.getroot()

    for o in range(len(list(nodes_coordinates.keys()))):

        id_1adjacent_street1 += 1
        id_1adjacent_street2 += 1
        id_2adjacent_street1 += 1
        id_2adjacent_street2 += 1

        id_nearest_node = list(nodes_coordinates.keys())[o]

        if str(id_nearest_node)[0:2] == '30':

            #nearest_node = list(nodes_coordinates.values())[o]
            nearest_node = nodes_coordinates.get(id_nearest_node)

            adj = list(G.succ[int(id_nearest_node)].keys())

            if o == 0:
                osm_tag = Scenario.create_node(osm_tag, str(0), str(0), str(0))

            osm_tag = Scenario.create_node(osm_tag, str(id_nearest_node), str(nearest_node[0]), str(nearest_node[1]))

            # edges between nearest node and first id node
            osm_tag = Scenario.create_way(osm_tag, str(id_1adjacent_street1), str(int(adj[0])), str(int(id_nearest_node)))
            osm_tag = Scenario.create_way(osm_tag, str(id_1adjacent_street2), str(int(id_nearest_node)), str(int(adj[0])))

            # edges between nearest node and second id node
            osm_tag = Scenario.create_way(osm_tag, str(id_2adjacent_street1), str(id_nearest_node), str(int(adj[1])))
            osm_tag = Scenario.create_way(osm_tag, str(id_2adjacent_street2), str(int(adj[1])), str(id_nearest_node))

    tree.write(file_osm, xml_declaration=True)

    Scenario.simulation_edit_graph(G, file_osm, net_file)
    G = Graph.set_node_elevation(G, geotiff)
    G = Graph.edge_grades(G)
    G = Graph.surface(G, file_osm)
    #G = Graph.update_weighnetconvert_geotifft(G, VEHICLE_MASS)
    #Graph.save_graph_file(G, file_name)
    """
    
    G, nodes_coordinates, nodes_mass_increment = Graph.configure_graph_simulation(G, geotiff, stop_points,
                                                                                  material_weights, file_osm, file_name)
    """
    return G, nodes_coordinates, nodes_mass_increment


def combination(function, G, H, node_source, node_target, politic, alg, stop_points, dict_edges_net, nodes_mass, file_name, nodes_coordinates, net_file):

    start = time.time()
    #print("node source", node_source, "node target", node_target, nodes_coordinates)
    cost, paths, edges_update = function(G, H, node_source, node_target, politic, alg)
    end = time.time()
    time_total = end - start

    function = function.__name__

    # simulation results dictionary
    result_work = {}
    #[result_work.update([(str(i), [stop_points[i]])]) for i in range(len(stop_points))]
    var_list = [(stop_points[i][0], stop_points[i][1], str(list(nodes_coordinates.keys())[i]), str(list(nodes_mass.values())[i])) for i in
           range(len(stop_points))]
    [result_work.update([(str(i), [var_list[i]])]) for i in range(len(stop_points))]

    sumo_route = [dict_edges_net.get((int(paths[i]), int(paths[i + 1]))) for i in range(len(paths) - 1)]
    edges_stop = [dict_edges_net.get((int(i[0]), int(i[1]))) for i in edges_update]
    print(sumo_route, edges_stop)

    # creates a dictionary with mass increment value of the edges
    edges_mass_increments = {}
    [edges_mass_increments.update([(edges_stop[i], nodes_mass.get(edges_update[i][0]))]) for i in
     range(len(edges_update))]

    out = file_name + '_' + politic + '_alg_' + alg + '_' + str(function) + '.xml'
    file_name = file_name + '_' + politic + '_alg_' + alg + '_' + str(function)

    # it simulates the 'carrinheiro' on the route and returns the total distance traveled
    #total_length = start_simulation('sumo-gui', SUMO_CONFIG, out, sumo_route, G, dict_edges_net, file_name,
    #                                edges_mass_increments, politic)
    total_length = start_simulation('sumo-gui', net_file, out, sumo_route, G, dict_edges_net, file_name,
                                    edges_mass_increments, politic)
    result_work.update([('total_length', float(total_length))])
    result_work.update([('total_time', float(time_total))])

    # write the json with simulation results
    write_json(result_work, file_name + '_coords') #_' + politic + '_alg_' + alg)

    # plot the route
    #fig, ax = ox.plot_graph_route(G, paths, route_linewidth=6, node_size=0, bgcolor='w')


# @profile
def create_route(stop_points, material_weights, json_files, seed, n = None, n_points=10):

    # the desired geotiff name to the mosaic
    mosaic_geotiff_name = 'out.tif'
    geotiff_name_out = MAPS_DIRECTORY + mosaic_geotiff_name

    # creates the geographic rectangular area based on stop points coordinates
    # downloads the Open Street Map (osm) file of the area
    osm_file = OpenSteetMap.file_osm(MAPS_DIRECTORY, stop_points)

    # downloads the GeoTiff file(s) of the area from the Topodata site
    # it returns the geotiff name of the Topodata database
    geotiff_name = GeoTiff.geotiff(MAPS_DIRECTORY, stop_points)
    geotiff_name = MAPS_DIRECTORY + geotiff_name + '.tif'

    # gdal translate of the geotiff file
    geotiff_transformation(geotiff_name, geotiff_name_out)

    # creates a rectangular area based on stop points coordinates
    max_lat, min_lat, max_lon, min_lon = Coordinates.create_osmnx(stop_points)

    # G_file is the name of the graph file (.graphml extension)
    G_file = Saves.def_file_name(MAPS_DIRECTORY, stop_points, '_' + str(n_points) + '_' + str(seed) + '.graphml')

    # defines the json file name of the simulation results
    file_name_json = Saves.def_file_name(RESULTS_DIRECTORY, stop_points, '') + '_' + str(n) + '_' + str(n_points)
    json_files.append(file_name_json)

    # the coordinates of the area is used to verify if the graph exists
    # coordinates_list = Coordinates.coordinates_list_bbox(stop_points)

    file_coords = file_name_json + '_weight_alg_SPFA_nearest_neighbor_coords'
    print(file_coords)

    ### test
    net_file = Map_Simulation.net_file_name('simulation/', stop_points)
    print(net_file)
    #G = ox.graph_from_bbox(max_lat, min_lat, max_lon, min_lon, network_type='all')
    ###

    # if the graph exists, it is not necessary to do all configurations on the graph
    if verify_graph_exists(G_file, file_coords) is True:

        print("Entrou aqui")

        Map_Simulation.delete_osm_items(osm_file)

        # configure the elevation and edge weights
        # creates dictionaries with coordinates and mass increment data
        G, nodes_coordinates, nodes_mass_increment = nodes_data(G_file, net_file, material_weights, osm_file, geotiff_name, file_coords)

        # creates the .net.xml file (SUMO simulator file)
        #netconvert_geotiff(osm_file, geotiff_name_out, NET)                

        netconvert_geotiff(osm_file, geotiff_name_out, net_file)
    
    else:

        # delete collect points added before in the osm file
        Map_Simulation.delete_osm_items(osm_file)

        # if there are ways that can be bidirectional to 'carrinheiro'
        if BIDIRECTIONAL is True:
            Map_Simulation.edit_map(osm_file)

        # creates the osmnx graph based on the geographic area
        # Scenario graph (paths are edges and junctions are nodes)
        G = ox.graph_from_bbox(max_lat, min_lat, max_lon, min_lon, network_type='all')

        # configure the graph
        G, nodes_coordinates, nodes_mass_increment = Graph.configure_graph_simulation(G, geotiff_name, stop_points, material_weights, osm_file, G_file, net_file)

    ###########

    # the starting point is the first collect point of the vector
    index_source = list(nodes_coordinates.values()).index(stop_points[0])
    node_source = list(nodes_coordinates.keys())[index_source]

    # the arrival point is the last collect point of the vector
    index_target = list(nodes_coordinates.values()).index(stop_points[-1])
    node_target = list(nodes_coordinates.keys())[index_target]

    # creates the ordering graph
    # it is a complete graph with the number of nodes equivalent to number of collect points
    H = Graph_Collect.create_graph_route(nodes_coordinates, nodes_mass_increment)

    # dictionary with adjacent edges information
    #dict_edges_net = Map_Simulation.edges_net(NET)
    dict_edges_net = Map_Simulation.edges_net(net_file)

    # it is necessary configure the edges on simulator to allow the carrinheiro's type of vehicle
    #Map_Simulation.allow_vehicle(NET)
    Map_Simulation.allow_vehicle(net_file)

    politics = ['weight', 'length']
    search_algorithms = ['SPFA', 'dijkstra', 'astar']

    # Nearest

    combination(nn, G, H, node_source, node_target, politics[0], search_algorithms[0], stop_points, dict_edges_net,
                nodes_mass_increment, file_name_json, nodes_coordinates, net_file)
    """
    combination(nn, G, H, node_source, node_target, politics[0], search_algorithms[1], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coordinates)
    combination(nn, G, H, node_source, node_target, politics[0], search_algorithms[2], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coordinates)
    combination(nn, G, H, node_source, node_target, politics[1], search_algorithms[0], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coordinates)
    combination(nn, G, H, node_source, node_target, politics[1], search_algorithms[1], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coordinates)
    combination(nn, G, H, node_source, node_target, politics[1], search_algorithms[2], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coordinates)
    """
    # Closest
    #combination(ci, G, H, node_source, node_target, politics[0], search_algorithms[0], stop_points, dict_edges_net,
    #            nodes_mass_increment, file_name_json, nodes_coordinates)
    """
    combination(ci, G, H, node_source, node_target, politics[0], search_algorithms[1], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coordinates)
    combination(ci, G, H, node_source, node_target, politics[0], search_algorithms[2], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coordinates)
    combination(ci, G, H, node_source, node_target, politics[1], search_algorithms[0], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coordinates)
    combination(ci, G, H, node_source, node_target, politics[1], search_algorithms[1], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coordinates)
    combination(ci, G, H, node_source, node_target, politics[1], search_algorithms[2], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coordinates)
    """

    # Further
    #combination(fi, G, H, node_source, node_target, politics[0], search_algorithms[0], stop_points, dict_edges_net,
    #            nodes_mass_increment, file_name_json, nodes_coordinates)
    #combination(fi, G, H, node_source, node_target, politics[0], search_algorithms[1], stop_points, dict_edges_net,
    #            nodes_mass_increment, file_name_json, nodes_coordinates)
    """
    combination(fi, G, H, node_source, node_target, politics[0], search_algorithms[2], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coordinates)
    combination(fi, G, H, node_source, node_target, politics[1], search_algorithms[0], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coordinates)
    combination(fi, G, H, node_source, node_target, politics[1], search_algorithms[1], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coordinates)
    combination(fi, G, H, node_source, node_target, politics[1], search_algorithms[2], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coordinates)
    """
    return json_files


def get_seed(seed_id):
    """
    This function provides the random seed.

    :param seed_id:     int
                        the seed_id is the 'seeds' vector index
    :return:
    """

    seeds = [1859168769, 1598189534, 1822174485,
             1871883252, 188312339, 2125204119,
             2041095833, 358485174,
             1695858027, 762772169, 437720306,
             939612284, 1998078925, 981631283, # 1973272912
             1024155645, 558746720, 1349341884,
             678622600, 1319566104, 722594620,
             1700738670, 1995749838, 346983590,
             565528207, 513791680, 2081634991,
             1769370802, 349544396, 1996610406,
             1973272912,1972392646, 605846893,
             934100682,222735214, 2101442385,
             2009044369, 1895218768, 701857417,
             89865291, 144443207, 720236707,
             822780843, 898723423, 1644999263,
             985046914, 1859531344, 1024155645,
             764283187, 778794064, 683102175,
             1334983095, 1072664641, 999157082,
             1277478588, 960703545, 186872697,
             425414105, 694388766, 773370613,
             1384311643, 1000004583, 1147024708,
             538474442, 1936856304, 1996632795, 1936856304]
    return seeds[seed_id]


def main():
    """
    This function executes the experiments on the SUMO simulator.
    First of all, it sets the characteristics of the scenario:
    number of collect points, values of vehicle weight increment,
    city of the scenario, number of repetitions of the simulations, etc.
    Then, it creates pseudo-random collect points/stop points of the
    scenario. Finally, the function calls the 'create_route' function.
    """

    # number of collect points
    n_points = 30

    # maximum increment of vehicle weight at the collect point (material mass)
    max_mass_material = 5

    # random seed of mass increment
    random.seed(get_seed(0))

    # scenarios: 'Belo Horizonte' and 'Belem'
    city = 'Salvador'

    # mean of the gaussian function
    if city == 'Belo Horizonte':
        mean_lon = [-43.9438]
        mean_lat = [-19.9202]
    elif city == 'Belem':
        mean_lon = [-48.47000]
        mean_lat = [-1.46000]
    elif city == 'Salvador':
        mean_lon = [-38.487310]
        mean_lat = [-12.947855]
    else:
        mean_lon = [-48.47000]
        mean_lat = [-1.46000]

    # standard deviation of the gaussian function
    sigma = 0.002 #0.005

    # vector with vehicle weight increment in the collect points
    mass_increments = [random.randint(0, max_mass_material) for i in range(n_points-2)]

    # add unit of measurement of vehicle weight increment in the collect points
    material_weights = [(mass_increments[i], 'Kg') for i in range(n_points-2)]

    # the arrival point must not increment the vehicle weight
    material_weights.append((0, 'Kg'))

    # the starting point must not increment the vehicle weight
    material_weights.insert(0, (0, 'Kg'))

    # number of repetitions of the simulations
    n_seeds = 2

    json_files = []
    materials = {}

    for a in range(1, n_seeds):

        random.seed(get_seed(a))
        print(get_seed(a))
        longitudes = [random.gauss(mean_lon[0], sigma) for i in range(n_points)]
        latitudes = [random.gauss(mean_lat[0], sigma) for i in range(n_points)]
        stop_points = [(float(latitudes[i]), float(longitudes[i])) for i in range(len(latitudes))]
        [materials.update([((latitudes[i], longitudes[i]), material_weights[i])]) for i in range(len(latitudes))]
        json_files = create_route(stop_points, materials, json_files, get_seed(a), a, n_points)

    print(json_files)


if __name__ == "__main__":
    main()
