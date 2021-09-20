import networkx as nx
import time
import datetime
import random
from time import perf_counter_ns
import more_itertools
from time import perf_counter
import random
import matplotlib.pyplot as plt


def graph_create(n_nodes, node_names):

    # creating a complete graph
    H = nx.complete_graph(n_nodes)

    # Modifying node names (id nodes of G = id nodes of H)
    mapping = {i: node_names for i, node_names in enumerate(node_names)}
    H = nx.relabel_nodes(H, mapping)

    return H


def verifying_nodes(path, nodes):
    for i in nodes:
        if i not in list(path):
            return True
    return False


def nearest_neighbor(H, source, target):

    if source not in H:
        print("Error")
        return False

    open = [source]
    closed = []
    nodes_graph = list(H.nodes)
    nodes_graph.remove(target)
    nodes_graph.remove(source)
    route = [source]
    cost_total = 0

    while len(open) > 0:

        dist = {}
        node = open.pop(0)
        closed.append(node)
        missing = set(nodes_graph) - set(closed)

        # if current node is the target (objective) and
        # there is not nodes missing to be visited
        if len(missing) < 1:

            route.append(target)
            return cost_total, route
        else:

            # checks nodes that have not yet been added in closed
            possibilities = set(H.adj[node]) - set(closed)
            if target in possibilities:
                possibilities.remove(target)

            for u in possibilities:
                # checks the edge weight according to the vehicle's mass +
                # mass increase at the current vertex
                edge_cost = H[node][u]['weight']
                dist.update([(u, edge_cost)])

            # sorting the dict according to edge weights
            dist = dict(sorted(dist.items(), key=lambda item: item[1]))

            new_node = list(dist.keys())[0]
            route.append(list(dist.keys())[0])
            cost_total += float(list(dist.values())[0])
            open.append(new_node)


def furthest_insertion(H, source, target):
    path = [source]
    costs_to_source = {}
    total_cost = 0

    # verify the cost of the source to the nodes
    for u in H.adj[source]:
        edge_cost = H[source][u]['weight']
        costs_to_source.update([(u, edge_cost)])

    # sorting the dict according to edge weights
    costs_to_source = dict(sorted(costs_to_source.items(), key=lambda item: item[1], reverse=True))

    # remove the target
    costs_to_source.pop(target)

    # add the closest node of the source
    path.append(list(costs_to_source.keys())[0])

    nodes = list(H.nodes)
    nodes.remove(target)
    possibilities = set(nodes) - set(path)

    # all nodes must be visited
    while len(possibilities) > 0:

        # get the closest node of any node inside the path
        max_cost = float('-inf')
        k_node = float('inf')
        for a in path:
            for b in possibilities:
                cost = H[a][b]['weight']
                if cost > max_cost:
                    max_cost = cost
                    k_node = b

        # the k node must be inserted in a position of the path
        # where the cost (cost_IK + cost_KJ - cost_IJ) is minimum
        min_cost = float('inf')
        position = 0
        for i in range(len(path) - 1):
            cost_IK = H[path[i]][k_node]['weight']
            cost_KJ = H[k_node][path[i + 1]]['weight']
            cost_IJ = H[path[i]][path[i + 1]]['weight']
            total_cost = cost_IK + cost_KJ - cost_IJ
            if total_cost < min_cost:
                min_cost = total_cost
                position = i + 1

        path.insert(position, k_node)

        # nodes not yet visited
        possibilities = set(nodes) - set(path)

    path.append(target)
    return total_cost, path


def closest_insertion(H, source, target):
    path = [source]
    costs_to_source = {}
    total_cost = 0

    # verify the cost of the source to the nodes
    for u in H.adj[source]:
        edge_cost = H[source][u]['weight']
        costs_to_source.update([(u, edge_cost)])

    # sorting the dict according to edge weights
    costs_to_source = dict(sorted(costs_to_source.items(), key=lambda item: item[1], reverse=True))

    # remove the target
    costs_to_source.pop(target)

    # add the closest node of the source
    path.append(list(costs_to_source.keys())[0])

    nodes = list(H.nodes)
    nodes.remove(target)
    possibilities = set(nodes) - set(path)

    # all nodes must be visited
    while len(possibilities) > 0:

        # get the closest node of any node inside the path
        min_cost = float('inf')
        k_node = float('inf')
        for a in path:
            for b in possibilities:
                cost = H[a][b]['weight']
                if cost < min_cost:
                    min_cost = cost
                    k_node = b

        # the k node must be inserted in a position of the path
        # where the cost (cost_IK + cost_KJ - cost_IJ) is minimum
        min_cost = float('inf')
        position = 0
        for i in range(len(path) - 1):
            cost_IK = H[path[i]][k_node]['weight']
            cost_KJ = H[k_node][path[i + 1]]['weight']
            cost_IJ = H[path[i]][path[i + 1]]['weight']
            total_cost = cost_IK + cost_KJ - cost_IJ
            if total_cost < min_cost:
                min_cost = total_cost
                position = i + 1

        path.insert(position, k_node)

        # nodes not yet visited
        possibilities = set(nodes) - set(path)

    path.append(target)
    return total_cost, path


def exact_method(H, source, target):
    nodes_graph = list(H.nodes)
    nodes_graph.remove(source)
    if source != target:
        nodes_graph.remove(target)
    permutations = list(more_itertools.distinct_permutations(nodes_graph, len(nodes_graph)))

    costs = []
    all_permutations = []
    for i in permutations:
        i = list(i)
        i.insert(0, source)
        i.append(target)
        all_permutations.append(i)
        cost = 0
        for a in range(0, len(i)-1):
            cost += H[i[a]][i[a+1]]['weight']
        #sum_costs, paths = Graph_Collect.sum_costs_route(G, H, i, VEHICLE_MASS)

        costs.append(cost)
    minimum = min(costs)
    print(costs)
    index_minimum = costs.index(minimum)
    print(minimum)
    print(all_permutations)

    #return minimum, all_permutations[index_minimum]


if __name__ == '__main__':

    runtimes_nearest = []
    runtimes_closest = []
    runtimes_furthest = []
    n_point = []

    for n_points in range(10, 11, 10):

        n_point.append(n_points)

        max_weight = 5

        node_names = [i + 10000 for i in range(n_points)]
        mapping = {i: node_names for i, node_names in enumerate(node_names)}

        H = nx.complete_graph(n_points)

        H = nx.relabel_nodes(H, mapping)

        for i in H.edges:
            H.edges[i]['weight'] = random.randint(0, max_weight)

        source = list(H.nodes)[0]
        target = list(H.nodes)[-1]

        start = perf_counter() * 1000
        cost_total1, path1 = nearest_neighbor(H, source, target)
        end = perf_counter() * 1000
        time_total = end - start
        runtimes_nearest.append(time_total)
        if verifying_nodes(path1, list(H.nodes)) is True:
            print("ALERTA")

        start = perf_counter() * 1000
        cost_total2, path2 = closest_insertion(H, source, target)
        end = perf_counter() * 1000
        time_total = end - start
        runtimes_closest.append(time_total)
        if verifying_nodes(path1, list(H.nodes)) is True:
            print("ALERTA")

        start = perf_counter() * 1000
        cost_total3, path3 = furthest_insertion(H, source, target)
        end = perf_counter() * 1000
        time_total = end - start
        runtimes_furthest.append(time_total)
        if verifying_nodes(path1, list(H.nodes)) is True:
            print("ALERTA")

    #print(runtimes_nearest)
    #print(runtimes_closest)
    #print(runtimes_furthest)
    #print(n_point)

    n_point = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500]
    #runtimes = [0.0001938343048095703, 0.0012612342834472656, 0.0036034584045410156, 0.008948326110839844, 0.01688385009765625, 0.023128747940063477, 0.037000417709350586, 0.0603482723236084, 0.07227706909179688, 0.1111302375793457, 0.13323402404785156, 0.17711496353149414, 0.2183237075805664, 0.25499510765075684, 0.29552721977233887, 0.3574371337890625, 0.4192066192626953, 0.559412956237793, 0.5688130855560303, 0.6901719570159912, 0.8179559707641602, 0.8576962947845459, 1.0051400661468506, 1.0282750129699707, 1.2934269905090332, 1.3517215251922607, 1.7639143466949463, 1.9897778034210205, 2.23512601852417, 2.6735291481018066, 2.6339337825775146, 2.74637770652771, 3.1383697986602783, 3.5194485187530518, 3.591848134994507, 3.9539952278137207, 3.8851633071899414, 4.104515790939331, 5.211892127990723, 5.363824844360352, 4.920464754104614, 6.206448554992676, 6.219696998596191, 6.591721773147583, 6.192683219909668, 8.951211929321289, 8.229309320449829, 8.843323945999146, 8.234997272491455, 8.926319122314453]

    new = [i for i in range(0, n_point[-1], 50)]

    nearest = [0.10432499999296851, 0.2986289999971632, 0.6426870000141207, 1.0694999999832362, 1.6207720000529662, 2.3260000000009313, 3.4396599999745376, 3.7446789999958128, 5.106160999974236, 5.677083000016864, 6.95982799999183, 8.505507999972906, 9.44666600000346, 11.746853999997256, 12.545290000009118, 14.545722999988357, 16.399662999989232, 17.958757000014884, 21.718931000010343, 21.82227099998272, 23.91285599998082, 27.70976199998404, 28.355079000000842, 30.849541000003228, 33.38538100000005, 38.45550899996306, 42.529529999999795, 42.38039499998558, 46.430898000020534, 48.363670999970054, 55.23060100001749, 58.11514700000407, 62.72891700002947, 69.27820199995767, 69.5748410000233, 75.93793100002222, 77.81482800003141, 84.52449599996908, 95.20556099998066, 101.39093900000444, 105.63502300000982, 111.59361900005024, 105.0996359999408, 115.1620099999709, 119.63887999992585, 126.3395030000247, 125.30112800002098, 157.24026400002185, 146.3008480001008, 142.83653900003992]

    closest = [0.17472300000372343, 1.1702099999820348, 3.6972659999737516, 8.770669999968959, 17.037100999994436, 29.811171999986982, 52.06814600000507, 57.99866200002725, 83.57100799999898, 115.84163500001887, 195.64671500000986, 194.08633200000622, 268.0935959999915, 320.807792000036, 495.83842300000833, 516.8877769999963, 562.8328789999941, 759.5301489999983, 761.7405189999845, 872.7595019999717, 1140.9963510000089, 1310.042814000015, 1328.4929370000027, 1495.5054869999876, 1703.6078660000057, 2361.1807240000053, 2597.717313000001, 2881.446640000009, 3146.4290390000097, 3583.90271200001, 3868.017117999989, 4294.087082999991, 5039.109675999964, 5365.914374000044, 5813.448840000026, 6503.3736590000335, 7047.735777999973, 7661.141876000038, 8300.192372999969, 9228.841247000091, 10205.192423000059, 10347.21146999998, 10946.323943000054, 11885.788837999979, 12826.217440999986, 13585.008733000024, 14648.194658000022, 16370.50887999998, 16493.548596999957, 17083.670575000113]

    farthest = [0.16803000000072643, 1.1925760000303853, 3.933920000010403, 8.62512999997125, 16.947084000014, 30.54276499999105, 44.366957999998704, 61.019982000027085, 81.76195499999449, 112.96056799998041, 177.15335799998138, 193.8228919999965, 280.56888499998604, 344.8392640000093, 432.08027900001616, 517.2628239999758, 685.9655979999807, 702.8185119999689, 750.6417579999834, 883.6238309999753, 1295.2545160000154, 1162.0459160000028, 1346.292414000025, 1511.722796999995, 1883.982154999976, 2233.290311000019, 2732.9681580000033, 2894.383352999983, 3107.708501999994, 3393.6662809999834, 4114.335143000004, 4503.344114999956, 5024.556565000035, 5292.614674999961, 6136.885595000058, 6398.090442000015, 7004.698661999952, 7661.623896999925, 8137.189849999966, 9067.528348999971, 10010.580973999982, 10273.275979999977, 11265.452050000022, 11932.691120000032, 12843.49878199998, 13666.546008999983, 15040.647019000142, 15715.96658700006, 16234.861689000041, 16968.355114999926]

    #runtimes_1 = [runtimes_nearest[i] for i in range(len(runtimes_nearest))]

    fig = plt.figure()
    plt.title("Inserção do mais próximo", y=1.05)
    plt.plot(n_point, nearest, label='Nearest Neighbor', color='tab:orange', ls="-", linewidth=1.1)
    plt.plot(n_point, closest, label='Closest Insertion', color='tab:green', ls="-", linewidth=1.1)
    plt.plot(n_point, farthest, label='Farthest Insertion', color='tab:blue', ls="-", linewidth=1.1)
    plt.xticks(new)
    plt.legend(numpoints=1, loc="upper right", ncol=3)
    plt.xlabel("Tamanho da entrada")
    plt.ylabel("Tempo de execução (s)")
    plt.grid()
    #plt.yscale('log')
    #plt.show()

    ##############################################

    H = nx.complete_graph(5)
    node_names = [i for i in range(1, 6)]
    mapping = {i: node_names for i, node_names in enumerate(node_names)}
    print(mapping)
    H = nx.relabel_nodes(H, mapping)

    H[1][2]['weight'] = 2
    H[1][3]['weight'] = 9
    H[1][4]['weight'] = 3
    H[1][5]['weight'] = 6
    H[2][3]['weight'] = 4
    H[2][4]['weight'] = 3
    H[2][5]['weight'] = 8
    H[3][4]['weight'] = 7
    H[3][5]['weight'] = 3
    H[4][5]['weight'] = 3

    exact_method(H, 5, 5)

