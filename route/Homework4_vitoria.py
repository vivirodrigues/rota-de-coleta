from networkx.algorithms.graphical import is_graphical
from networkx.utils.random_sequence import powerlaw_sequence
import networkx as nx
import random
import numpy as np

seed = 1142
random.seed(seed)

N, _lambda = 10**5, 2.2
while True:
    #Create the sequence
    #seq = [int(round(d)) for d in powerlaw_sequence(N, _lambda)]
    seq = [int(round(i)) for i in powerlaw_sequence(N, _lambda)]
    #Test if is possible to generate a graph
    if is_graphical(seq):
        # print("LOL")
        break
#Configure a model using the tested sequence
G = nx.configuration_model(seq, seed=seed)

# conta multilinks
num_par = 0
a = 0
for node in G.nodes:
    for vizinho in G.neighbors(node):
        if node != vizinho:
            if len(G[node][vizinho]) > 1:
                num_par += len(G[node][vizinho])-1



############## self-loops
n_edges = G.number_of_edges()
n_loops = nx.number_of_selfloops(G)
loops = (n_loops*100)/n_edges
print("Porcentagem de loops", loops)

############## multi links
num_par = num_par/2
multi = (num_par * 100) / n_edges
print(multi)


