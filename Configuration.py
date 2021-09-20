import Simulation
import time
from route import Scenario
import json
from Constants import *
from geography import GeoTiff, OpenSteetMap, Coordinates
from general import Saves
from route import Graph_Collect
from simulation import Map_Simulation
import osmnx as ox
import matplotlib.pyplot as plt
from route import Graph
from route.Heuristics import nearest_neighbor as nn
from route.Heuristics import closest_insertion as ci
from route.Heuristics import farthest_insertion as fi


def verify_graph_exists(file_name, file_coords):  # , stop_points, coordinates_list):
    try:
        print(file_name, file_coords + '.json')
        G = ox.load_graphml(file_name)

        # file coords is the results
        f = open(file_coords + '.json', "r")
        dados = json.loads(f.read())
        f.close()
        return True
    except:
        pass
    return False


def verify_file_exists(file_name):
    try:
        f = open(file_name, "r")
        f.close()
        return True
    except:
        pass
    return False


def nodes_data(file_name, file_osm, geotiff, file):
    G = ox.load_graphml(file_name)

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
    dados = list(dados.values())[:tam - 2]

    [nodes_coordinates.update([(int(d[0][2]), (d[0][0], d[0][1]))]) \
     for d in list(dados)]

    [nodes_mass_increment.update([(int(d[0][2]), int(d[0][3]))]) \
     for d in list(dados)]

    # sorts the ids of the nodes that will be inserted in the osm file
    nodes_coordinates = dict(sorted(nodes_coordinates.items(), key=lambda item: item[0]))
    nodes_mass_increment = dict(sorted(nodes_mass_increment.items(), key=lambda item: item[0]))
    G = Graph.set_node_elevation(G, geotiff)
    G = Graph.edge_grades(G)
    G = Graph.surface(G, file_osm)
    return G, nodes_coordinates, nodes_mass_increment


def reconstruct_osm(G, nodes_coordinates, file_osm):
    id_1adjacent_street1 = 40000000000
    id_1adjacent_street2 = 50000000000
    id_2adjacent_street1 = 60000000000
    id_2adjacent_street2 = 70000000000
    id_0adjacent_street1 = 80000000000
    id_0adjacent_street2 = 90000000000

    tree = Map_Simulation.parse_file_tree(file_osm)
    osm_tag = tree.getroot()

    for o in range(len(list(nodes_coordinates.keys()))):

        id_1adjacent_street1 += 1
        id_1adjacent_street2 += 1
        id_2adjacent_street1 += 1
        id_2adjacent_street2 += 1
        id_0adjacent_street1 += 1
        id_0adjacent_street2 += 1

        id_nearest_node = list(nodes_coordinates.keys())[o]

        if str(id_nearest_node)[0:2] == '30':

            # nearest_node = list(nodes_coordinates.values())[o]
            nearest_node = nodes_coordinates.get(id_nearest_node)

            adj = list(G.succ[int(id_nearest_node)].keys())

            if o == 0:
                osm_tag = Scenario.create_node(osm_tag, str(0), str(0), str(0))

            osm_tag = Scenario.create_node(osm_tag, str(id_nearest_node), str(nearest_node[0]), str(nearest_node[1]))

            # edges between nearest node and first id node
            osm_tag = Scenario.create_way(osm_tag, str(id_1adjacent_street1), str(int(adj[0])),
                                          str(int(id_nearest_node)))
            osm_tag = Scenario.create_way(osm_tag, str(id_1adjacent_street2), str(int(id_nearest_node)),
                                          str(int(adj[0])))

            # edges between nearest node and second id node
            osm_tag = Scenario.create_way(osm_tag, str(id_2adjacent_street1), str(id_nearest_node), str(int(adj[1])))
            osm_tag = Scenario.create_way(osm_tag, str(id_2adjacent_street2), str(int(adj[1])), str(id_nearest_node))
        else:
            i = nodes_coordinates.get(id_nearest_node)
            adj = list(G.succ[int(id_nearest_node)].keys())

            if o == 0:
                osm_tag = Scenario.create_node(osm_tag, str(0), str(0), str(0))

            osm_tag = Scenario.create_node(osm_tag, str(id_nearest_node), str(i[0]), str(i[1]))
            # edges between nearest node and first id node
            osm_tag = Scenario.create_way(osm_tag, str(id_0adjacent_street1), str(int(adj[0])),
                                          str(int(id_nearest_node)))
            osm_tag = Scenario.create_way(osm_tag, str(id_0adjacent_street2), str(int(id_nearest_node)),
                                          str(int(adj[0])))

            lat = float(i[0]) + 0.00002
            lon = float(i[1]) + 0.00002
            osm_tag = Scenario.create_node(osm_tag, str(int(id_nearest_node + 50)), str(lat), str(lon))
            # edges between nearest node and first id node
            osm_tag = Scenario.create_way(osm_tag, str(int(id_0adjacent_street1 + 50)), str(int(adj[1])),
                                          str(int(id_nearest_node + 50)))
            osm_tag = Scenario.create_way(osm_tag, str(int(id_0adjacent_street2 + 50)), str(int(id_nearest_node + 50)),
                                          str(int(adj[1])))
            osm_tag = Scenario.create_way(osm_tag, str(int(id_0adjacent_street1 + 300)), str(int(id_nearest_node)),
                                          str(int(id_nearest_node + 50)))
            osm_tag = Scenario.create_way(osm_tag, str(int(id_0adjacent_street2 + 300)), str(int(id_nearest_node + 50)),
                                          str(int(id_nearest_node)))
            ##

    tree.write(file_osm, xml_declaration=True)

    return True


def combination(function, G, H, node_source, node_target, politic, alg, stop_points, dict_edges_net, nodes_mass,
                file_name, nodes_coordinates, net_file):

    start = time.time()
    cost, paths, edges_update = function(G, H, node_source, node_target, politic, alg)
    end = time.time()
    time_total = end - start

    print("node source", node_source, "node target", node_target, nodes_coordinates)
    print("path", paths)

    function = function.__name__

    for i in list(nodes_coordinates.keys()):
        if i not in paths:
            print("O nó", i, " não está sendo visitado na ", function)

    # simulation results dictionary
    result_work = {}

    var_list = [(stop_points[i][0], stop_points[i][1], str(list(nodes_coordinates.keys())[i]),
                 str(list(nodes_mass.values())[i])) for i in
                range(len(stop_points))]
    [result_work.update([(str(i), [var_list[i]])]) for i in range(len(stop_points))]

    sumo_route = [dict_edges_net.get((int(paths[i]), int(paths[i + 1]))) for i in range(len(paths) - 1)]
    edges_stop = [dict_edges_net.get((int(i[0]), int(i[1]))) for i in edges_update]
    print(sumo_route, edges_stop)

    # creates a dictionary with mass increment value of the edges
    edges_mass_increments = {}
    [edges_mass_increments.update([(edges_stop[i], nodes_mass.get(edges_update[i][0]))]) for i in
     range(len(edges_update))]

    out = file_name + '_' + politic + '_' + alg + '_' + str(function) + '.xml'
    file_name = file_name + '_' + politic + '_' + alg + '_' + str(function)

    # it simulates the 'carrinheiro' on the route and returns the total distance traveled
    total_length = Simulation.start_simulation('sumo', net_file, out, sumo_route, G, dict_edges_net, file_name,
                                    edges_mass_increments, politic)
    result_work.update([('total_length', float(total_length))])
    result_work.update([('total_time', float(time_total))])

    # write the json with simulation results
    Simulation.write_json(result_work, file_name + '_coords')  # _' + politic + '_alg_' + alg)

    # plot the route
    # fig, ax = ox.plot_graph_route(G, paths, route_linewidth=6, node_size=0, bgcolor='w')


# @profile
def create_route(stop_points, material_weights, json_files, seed, n=None, n_points=10):
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
    Simulation.geotiff_transformation(geotiff_name, geotiff_name_out)

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
    #file_coords = file_name_json + '_weight_SPFA_nearest_neighbor_coords'
    print("Configuration file:", file_coords)

    net_file = Map_Simulation.net_file_name('simulation/', stop_points)
    print(net_file)

    # delete collect points added before in the osm file
    Map_Simulation.delete_osm_items(osm_file)

    # if the graph exists, it is not necessary to do all configurations on the graph
    if verify_graph_exists(G_file, file_coords) is True:

        print("Arquivo do grafo encontrado")
        # creates dictionaries with coordinates and mass increment data
        G, nodes_coords, nodes_mass_increment = nodes_data(G_file, osm_file, geotiff_name, file_coords)

        if verify_file_exists(net_file):
            print("Arquivo .net.xml encontrado")
        else:
            # configure the osm file according to the graph
            reconstruct_osm(G, nodes_coords, osm_file)

            # if there are ways that can be bidirectional to 'carrinheiro'
            # if BIDIRECTIONAL is True:
            #    Map_Simulation.edit_map(osm_file)

            # creates the .net.xml file (SUMO simulator file)
            Simulation.netconvert_geotiff(osm_file, geotiff_name_out, net_file)

    else:

        # if there are ways that can be bidirectional to 'carrinheiro'
        if BIDIRECTIONAL is True:
            Map_Simulation.edit_map(osm_file)

        # creates the osmnx graph based on the geographic area
        # Scenario graph (paths are edges and junctions are nodes)
        G = ox.graph_from_bbox(max_lat, min_lat, max_lon, min_lon, network_type='all')

        # configure the graph
        G, nodes_coords, nodes_mass_increment = Graph.config_graph(G, geotiff_name, stop_points, material_weights,
                                                                   osm_file, G_file, net_file)
    ###########

    # the starting point is the first collect point of the vector
    index_source = list(nodes_coords.values()).index(stop_points[0])
    node_source = list(nodes_coords.keys())[index_source]

    # the arrival point is the last collect point of the vector
    index_target = list(nodes_coords.values()).index(stop_points[-1])
    node_target = list(nodes_coords.keys())[index_target]

    # creates the ordering graph
    # it is a complete graph with the number of nodes equivalent to number of collect points
    H = Graph_Collect.create_graph_route(nodes_coords, nodes_mass_increment)

    # dictionary with adjacent edges information
    dict_edges_net = Map_Simulation.edges_net(net_file)

    # it is necessary configure the edges on simulator to allow the carrinheiro's type of vehicle
    Map_Simulation.allow_vehicle(net_file)

    politics = ['weight', 'length', 'impedance']
    search_algorithms = ['SPFA', 'dijkstra', 'astar']

    # Nearest

    combination(nn, G, H, node_source, node_target, politics[0], search_algorithms[0], stop_points, dict_edges_net,
                nodes_mass_increment, file_name_json, nodes_coords, net_file)
    combination(nn, G, H, node_source, node_target, politics[0], search_algorithms[1], stop_points, dict_edges_net,
                nodes_mass_increment, file_name_json, nodes_coords, net_file)
    combination(nn, G, H, node_source, node_target, politics[0], search_algorithms[2], stop_points, dict_edges_net,
                nodes_mass_increment, file_name_json, nodes_coords, net_file)

    combination(nn, G, H, node_source, node_target, politics[1], search_algorithms[0], stop_points, dict_edges_net,
                nodes_mass_increment, file_name_json, nodes_coords, net_file)
    combination(nn, G, H, node_source, node_target, politics[1], search_algorithms[1], stop_points, dict_edges_net,
                nodes_mass_increment, file_name_json, nodes_coords, net_file)
    combination(nn, G, H, node_source, node_target, politics[1], search_algorithms[2], stop_points, dict_edges_net,
                nodes_mass_increment, file_name_json, nodes_coords, net_file)

    combination(nn, G, H, node_source, node_target, politics[2], search_algorithms[0], stop_points, dict_edges_net,
                nodes_mass_increment, file_name_json, nodes_coords, net_file)
    combination(nn, G, H, node_source, node_target, politics[2], search_algorithms[1], stop_points, dict_edges_net,
                nodes_mass_increment, file_name_json, nodes_coords, net_file)
    combination(nn, G, H, node_source, node_target, politics[2], search_algorithms[2], stop_points, dict_edges_net,
                nodes_mass_increment, file_name_json, nodes_coords, net_file)

    # Closest
    combination(ci, G, H, node_source, node_target, politics[0], search_algorithms[0], stop_points, dict_edges_net,
                nodes_mass_increment, file_name_json, nodes_coords, net_file)
    combination(ci, G, H, node_source, node_target, politics[0], search_algorithms[1], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coords, net_file)
    combination(ci, G, H, node_source, node_target, politics[0], search_algorithms[2], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coords, net_file)
    
    combination(ci, G, H, node_source, node_target, politics[1], search_algorithms[0], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coords, net_file)
    combination(ci, G, H, node_source, node_target, politics[1], search_algorithms[1], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coords, net_file)
    combination(ci, G, H, node_source, node_target, politics[1], search_algorithms[2], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coords, net_file)

    combination(ci, G, H, node_source, node_target, politics[2], search_algorithms[0], stop_points, dict_edges_net,
                nodes_mass_increment, file_name_json, nodes_coords, net_file)
    combination(ci, G, H, node_source, node_target, politics[2], search_algorithms[1], stop_points, dict_edges_net,
                nodes_mass_increment, file_name_json, nodes_coords, net_file)
    combination(ci, G, H, node_source, node_target, politics[2], search_algorithms[2], stop_points, dict_edges_net,
                nodes_mass_increment, file_name_json, nodes_coords, net_file)
    

    # Further
    combination(fi, G, H, node_source, node_target, politics[0], search_algorithms[0], stop_points, dict_edges_net,
                nodes_mass_increment, file_name_json, nodes_coords, net_file)
    combination(fi, G, H, node_source, node_target, politics[0], search_algorithms[1], stop_points, dict_edges_net,
                nodes_mass_increment, file_name_json, nodes_coords, net_file)
    combination(fi, G, H, node_source, node_target, politics[0], search_algorithms[2], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coords, net_file)
    
    combination(fi, G, H, node_source, node_target, politics[1], search_algorithms[0], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coords, net_file)
    combination(fi, G, H, node_source, node_target, politics[1], search_algorithms[1], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coords, net_file)
    combination(fi, G, H, node_source, node_target, politics[1], search_algorithms[2], stop_points, dict_edges_net,
                          nodes_mass_increment, file_name_json, nodes_coords, net_file)

    combination(fi, G, H, node_source, node_target, politics[2], search_algorithms[0], stop_points, dict_edges_net,
                nodes_mass_increment, file_name_json, nodes_coords, net_file)
    combination(fi, G, H, node_source, node_target, politics[2], search_algorithms[1], stop_points, dict_edges_net,
                nodes_mass_increment, file_name_json, nodes_coords, net_file)
    combination(fi, G, H, node_source, node_target, politics[2], search_algorithms[2], stop_points, dict_edges_net,
                nodes_mass_increment, file_name_json, nodes_coords, net_file)

    return json_files