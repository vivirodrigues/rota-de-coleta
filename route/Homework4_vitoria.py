import networkx as nx
import matplotlib.pyplot as plt


k_average_degree = [0.8, 1, 8]
N = 500
print("Number of nodes (N): ", N)
p = [i / (N - 1) for i in k_average_degree]
for i in p:
    print("Probability of two nodes are connected (p): ", i)
    G = nx.gnp_random_graph(N, i, directed=False)
    print("Number of links (L):", G.number_of_edges())
    plt.figure()
    nx.draw_random(G,
                    node_color='green',
                    with_labels=False,
                    node_size=100,
                    width=0.3
                    )
    plt.show()

