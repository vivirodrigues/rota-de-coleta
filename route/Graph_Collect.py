import networkx as nx
from route import Search
from route import Graph


def create_graph_route(nodes_coordinates, nodes_mass_increment):
    """
    This function creates a complete graph with all collect nodes.
    Each node of the graph is a collect point.

    :param nodes_coordinates:       dictionary
                                    The dictionary must have the
                                    id of nodes and their geographic
                                    coordinates.
                                    Example: {id_node:(x, y)}

    :param nodes_mass_increment:    dictionary
                                    The dictionary must have the
                                    id of nodes and a tuple with
                                    the vehicle mass increment
                                    value in this point.
                                    The first item of the tuple is
                                    the amount, and the second is
                                    the type of data, as kilograms,
                                    grams, etc.
                                    Example: {id_node:(50, 'Kg')}

    :return:                        NetworkX graph.
                                    Complete graph not directed.
    """

    # creating a complete graph
    H = nx.complete_graph(len(nodes_coordinates.keys()))

    # Modifying node names (id nodes of G = id nodes of H)
    node_names = list(nodes_mass_increment.keys())
    mapping = {i:node_names for i, node_names in enumerate(node_names)}
    H = nx.relabel_nodes(H, mapping)

    # Add x, y and value of vehicle mass increment
    for i in nodes_coordinates:
        coord = nodes_coordinates.get(i)
        weight_node = nodes_mass_increment.get(i)
        H.nodes[i]['x'] = coord[1]
        H.nodes[i]['y'] = coord[0]
        H.nodes[i]['mass'] = weight_node

    return H


def sum_costs(G, path, politic):
    """
    This function calculates the sum of the costs
    of a path created according to the geographic
    scenario graph.

    :param G:       NetworkX graph.
                    Geographic scenario

    :param path:    list
                    The list must contains the id
                    of nodes of the path.

    :param politic:  String or function

    :return:        float
                    The sum of all cost (weight)
                    edges of the path.
    """
    sum_costs = nx.path_weight(G, path, politic)

    return sum_costs


def cost_path(G, source, target, vehicle_mass, politic, search_alg):
    """
    This function calculates the path between source and
    target nodes, and returns it. Besides, calculates the
    sum of all edges weight of the path, and returns it.

    :param G:               NetworkX graph.
                            Geographic scenario

    :param source:
    :param target:
    :param vehicle_mass:
    :return:
    """

    # updates the weight of all edges of the scenario according
    # to the current weight of the vehicle
    if politic == 'weight':
        G = Graph.update_weight(G, vehicle_mass)

    # finds the shortest path to the destination in the scenario graph
    if search_alg == 'SPFA':

        distance, path = Search.bellman_ford(G, source, target, weight=politic)
        #path = Heuristics.shortest_path_faster(G, source, target, impedance)

    elif search_alg == 'dijkstra':

        distance, path = Search.bidirectional_dijkstra(G, source, target, weight=politic)

    elif search_alg == 'astar':

        path = nx.astar_path(G, source, target, weight=politic)

    else:

        distance, path = Search.bellman_ford(G, source, target, weight=politic)

    # cost to get to the destination:
    # the sum of the weight of all the edges from the path
    sum_path_costs = sum_costs(G, path, politic)

    # updates the weight of all edges of the scenario according
    # to the current weight of the vehicle
    #if impedance == 'weight':
    #    G = Graph.update_weight(G, VEHICLE_MASS)

    return sum_path_costs, path


def sum_costs_route(G, H, route, vehicle_mass, impedance, heuristic):
    """
    This function calculates the total cost of a route,
    according to the collect points in the scenario, and
    the vehicle mass update in each H node (collect point).

    :param G:                   NetworkX graph.
                                Geographic scenario

    :param H:                   NetworkX graph.
                                Complete graph where each node
                                is acollect point
    :param route:
    :param vehicle_mass:
    :return:
    """
    vehicle_mass += H.nodes[route[0]]['mass']
    paths = []
    cost_work_all = 0
    edges_update_mass = []

    for node in range(len(route)-1):

        # adds the current weight of the vehicle to the weight
        # of the materials being collected in this node
        vehicle_mass += H.nodes[route[node]]['mass']

        # checks the cost of going from one node to the next collection point
        cost_work, path = cost_path(G, route[node], route[node + 1], vehicle_mass, impedance, heuristic)
        cost_work_all += cost_work
        if len(path) > 1:

            if node == len(route)-2:
                paths.extend(path)
            else:
                paths.extend(path[:-1])
            edges_update_mass.append(path[:2])
        else:
            paths.extend(path)
            #edges_update_mass.append([paths[len(paths)-2], path[0]])
            #edges_update_mass.append([path[0], path[0]])
    return cost_work_all, paths, edges_update_mass



