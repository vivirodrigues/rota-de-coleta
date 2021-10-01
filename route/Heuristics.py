from route import Graph
from Constants import *
from route import Graph_Collect


def verifying_nodes(path, nodes):
    for i in nodes:
        if i not in list(path):
            return True
    return False


def nearest_neighbor(G, H, source, target, politic, search_alg):
    """

    :param G:           NetworkX graph.
                        input graph

    :param source:      Float
                        Id of the start node

    :param target:      Float
                        Id of the goal node

    :param politic:     Edges weight politic
                        Ex: 'length' for distance

    :return:            List
                        List with all nodes of the
                        shortest path
    """
    if source not in H:
        print("Error")
        return False

    open = [source]
    closed = []
    current_vehicle_mass = VEHICLE_MASS
    nodes_graph = list(H.nodes)
    nodes_graph.remove(target)
    nodes_graph.remove(source)
    route = []
    route1 = []
    cost_total = 0
    edges_update_mass = []

    while len(open) > 0:
        dist = {}
        node = open.pop(0)
        closed.append(node)
        missing = set(nodes_graph) - set(closed)

        # if current node is the target (objective) and
        # there is not nodes missing to be visited
        if len(missing) < 1:

            edge_cost, path = Graph_Collect.cost_path(G, node, target, current_vehicle_mass, politic, search_alg)
            route.extend(path[:-1])
            route1.append(path)

            if politic == 'weight':
                G = Graph.update_weight(G, VEHICLE_MASS)

            return cost_total, route, edges_update_mass
        else:

            # checks nodes that have not yet been added in closed
            possibilities = set(H.adj[node]) - set(closed)

            for u in possibilities:
                # checks the edge weight according to the vehicle's mass +
                # mass increase at the current vertex
                edge_cost, path = Graph_Collect.cost_path(G, node, u, current_vehicle_mass, politic, search_alg)
                dist.update([(u, [edge_cost, path])])

            # sorting the dict according to edge weights
            dist = dict(sorted(dist.items(), key=lambda item: item[1][0]))

            new_node = list(dist.keys())[0]
            route.extend(list(dist.values())[0][1][:-1])
            route1.append(list(dist.values())[0][1][:-1])
            cost_total += float(list(dist.values())[0][0])
            edges_update_mass.append(list(dist.values())[0][1][:2])

            open.append(new_node)
            current_vehicle_mass += H.nodes[new_node]['mass']


def updates_vehicle_mass(path, mass):
    """

    :param path:    list
    :param mass:    dict

    :return:
    """
    vehicle_mass = VEHICLE_MASS
    for i in path:
        vehicle_mass += mass.get(i)
    return vehicle_mass


def closest_insertion(G, H, source, target, politic, search_alg):
    current_vehicle_mass = VEHICLE_MASS
    path = [source]
    costs_to_source = {}
    total_path = []

    # create a dictionary with the nodes and respective mass increments of the vehicle
    mass = {}
    for i in H.nodes:
        mass.update([(i, H.nodes[i]['mass'])])

    # verify the cost of the source to the nodes
    for u in H.adj[source]:
        edge_cost, _ = Graph_Collect.cost_path(G, source, u, current_vehicle_mass, politic, search_alg)
        costs_to_source.update([(u, [edge_cost])])

    # sorting the dict according to edge weights
    costs_to_source = dict(sorted(costs_to_source.items(), key=lambda item: item[1][0]))

    # add the closest node of the source
    path.append(list(costs_to_source.keys())[0])

    # updates the vehicle mass according to current path
    current_vehicle_mass = updates_vehicle_mass(path, mass)

    nodes = list(H.nodes)
    nodes.remove(target)
    possibilities = set(nodes) - set(path)

    # all nodes must be visited
    while len(possibilities) > 0:  # len(path) < len(nodes):

        # get the closest node of any node inside the path
        min_cost = float('inf')
        k_node = float('inf')

        for a in path:
            for b in possibilities:
                cost, way = Graph_Collect.cost_path(G, a, b, current_vehicle_mass, politic, search_alg)
                if cost < min_cost:
                    min_cost = cost
                    k_node = b

        # the k node must be inserted in a position of the path
        # where the cost (cost_IK + cost_KJ - cost_IJ) is minimum
        min_cost = float('inf')
        position = float('inf')

        for i in range(len(path) - 1):
            current_vehicle_mass = updates_vehicle_mass(path[:i], mass)
            cost_IK, _ = Graph_Collect.cost_path(G, path[i], k_node, current_vehicle_mass, politic, search_alg)
            cost_KJ, _ = Graph_Collect.cost_path(G, k_node, path[i + 1], current_vehicle_mass, politic, search_alg)
            cost_IJ, _ = Graph_Collect.cost_path(G, path[i], path[i + 1], current_vehicle_mass, politic, search_alg)
            total_cost = cost_IK + cost_KJ - cost_IJ
            if total_cost < min_cost:
                min_cost = total_cost
                position = i + 1

        path.insert(position, k_node)
        current_vehicle_mass = updates_vehicle_mass(path, mass)

        # nodes not yet visited
        possibilities = set(nodes) - set(path)

    path.append(target)

    if politic == 'weight':
        G = Graph.update_weight(G, VEHICLE_MASS)

    # get all paths
    cost_total, paths, edges_update = Graph_Collect.sum_costs_route(G, H, path, VEHICLE_MASS, politic, search_alg)

    return cost_total, paths, edges_update


def farthest_insertion(G, H, source, target, politic, search_alg):
    current_vehicle_mass = VEHICLE_MASS
    path = [source]
    costs_to_source = {}

    # create a dictionary with the nodes and respective mass increments of the vehicle
    mass = {}
    for i in H.nodes:
        mass.update([(i, H.nodes[i]['mass'])])

    # verify the cost of the source to the nodes
    for u in H.adj[source]:
        edge_cost, _ = Graph_Collect.cost_path(G, source, u, current_vehicle_mass, politic, search_alg)
        costs_to_source.update([(u, edge_cost)])

    # sorting the dict according to edge weights
    costs_to_source = dict(sorted(costs_to_source.items(), key=lambda item: item[1], reverse=True))

    # add the closest node of the source
    path.append(list(costs_to_source.keys())[0])

    # updates the vehicle mass according to current path
    current_vehicle_mass = updates_vehicle_mass(path, mass)

    nodes = list(H.nodes)
    nodes.remove(target)
    possibilities = set(nodes) - set(path)

    # all nodes must be visited
    while len(possibilities) > 0:  # len(path) < len(nodes):

        # get the closest node of any node inside the path
        max_cost = float('-inf')
        k_node = float('inf')
        for a in path:
            for b in possibilities:
                cost, _ = Graph_Collect.cost_path(G, a, b, current_vehicle_mass, politic, search_alg)
                if cost > max_cost:
                    max_cost = cost
                    k_node = b

        # the k node must be inserted in a position of the path
        # where the cost (cost_IK + cost_KJ - cost_IJ) is minimum
        min_cost = float('inf')
        position = 0
        for i in range(len(path) - 1):
            current_vehicle_mass = updates_vehicle_mass(path[:i], mass)
            cost_IK, _ = Graph_Collect.cost_path(G, path[i], k_node, current_vehicle_mass, politic, search_alg)
            cost_KJ, _ = Graph_Collect.cost_path(G, k_node, path[i + 1], current_vehicle_mass, politic, search_alg)
            cost_IJ, _ = Graph_Collect.cost_path(G, path[i], path[i + 1], current_vehicle_mass, politic, search_alg)
            total_cost = cost_IK + cost_KJ - cost_IJ
            if total_cost < min_cost:
                min_cost = total_cost
                position = i + 1

        path.insert(position, k_node)
        current_vehicle_mass = updates_vehicle_mass(path, mass)

        # nodes not yet visited
        possibilities = set(nodes) - set(path)

    path.append(target)

    # get all paths
    cost_total, paths, edges_update = Graph_Collect.sum_costs_route(G, H, path, VEHICLE_MASS, politic, search_alg)

    if politic == 'weight':
        G = Graph.update_weight(G, VEHICLE_MASS)

    return cost_total, paths, edges_update





