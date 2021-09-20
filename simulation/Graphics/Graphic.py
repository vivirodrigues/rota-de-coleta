import json
import osmnx as ox
import matplotlib.cm as cm
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx
from route import Graph
import numpy as np
from xml.dom import minidom


def open_file(name_file):
    try:
        f = open(name_file + ".json", "r")
        dados = json.loads(f.read())
        f.close()
    except:
        dados = 0
        pass

    return dados


def plot_edge_grades():
    files_map = '../data/maps/m43.96267779776494_m19.944747838679202_m43.929659815391865_m19.905049264605925.graphml'
    G = ox.load_graphml(files_map)

    max_lat = -12.934333867695516
    min_lat = -12.961083555974895
    max_lon = -38.473331269107426
    min_lon = -38.49996781691653

    name_geotiff = '../data/maps/19S45_ZN.tif'
    G = ox.graph_from_bbox(max_lat, min_lat, max_lon, min_lon, network_type='all')
    G = Graph.set_node_elevation(G, name_geotiff)
    # deadends = [(u, v) for u, v, k, data in G.edges(keys=True, data=True) if data['highway'] == '']
    # print(deadends)
    # G2.remove_nodes_from(deadends)
    G = Graph.edge_grades(G)
    G_proj = ox.project_graph(G)
    ec = ox.plot.get_edge_colors_by_attr(G_proj, "grade", cmap="plasma", num_bins=5, equal_size=True)
    fig, ax = ox.plot_graph(G_proj, edge_color=ec, edge_linewidth=0.5, node_size=0, bgcolor="w")


def plot_elevation():

    files_map = '../data/maps/m38.49905230272549_m12.960541036813272_m38.47398437502447_m12.935229804750517.graphml'
    G = ox.load_graphml(files_map)

    max_lat = -12.934333867695516
    min_lat = -12.961083555974895
    max_lon = -38.473331269107426
    min_lon = -38.49996781691653

    name_geotiff = '../data/maps/12S39_ZN.tif'
    G = ox.graph_from_bbox(max_lat, min_lat, max_lon, min_lon, network_type='all')
    G = Graph.set_node_elevation(G, name_geotiff)
    G = Graph.edge_grades(G)
    # G_proj = ox.project_graph(G)
    nc = ox.plot.get_node_colors_by_attr(G, 'elevation', cmap='plasma', num_bins=10)  # , start=0, stop=1
    cmap = plt.cm.get_cmap('plasma')
    #norm = plt.Normalize(vmin= 0, vmax=max(list(nx.get_node_attributes(G, 'elevation').values())) - min(list(nx.get_node_attributes(G, 'elevation').values())))
    print("Salvador", max(list(nx.get_node_attributes(G, 'elevation').values()))-
          min(list(nx.get_node_attributes(G, 'elevation').values())))
    norm = plt.Normalize(vmin=min(list(nx.get_node_attributes(G, 'elevation').values())),
                         vmax=max(list(nx.get_node_attributes(G, 'elevation').values())))
    sm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
    sm.set_array([min(list(nx.get_node_attributes(G, 'elevation').values())),2,10,20,30,40,50,60,70,80,86])

    figsize = (20, 20)
    fig, ax = ox.plot_graph(G, node_color=nc, node_size=35, edge_linewidth=0.7, bgcolor='w', show=False)

    fig, ax = ox.plot_graph(G, ax=ax, node_color=nc, node_size=35, edge_linewidth=0.7, bgcolor='w', show=False)
    #plt.axis([-38.49996781691653, -38.473331269107426, -12.961083555974895, -12.934333867695516],option='on')
    #ax.axis('on')
    #ax.set(xlim=(-38.49996781691653, -38.473331269107426), ylim=(-12.961083555974895, -12.934333867695516), option='on')

    # pad: position of colorbar, shrink=.92: colorbar size
    cb = fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, orientation='vertical', shrink=.94, fraction=0.15,
                      pad=-0.0001)
    cb.ax.tick_params(labelsize=25)
    cb.set_label('Altitude [m]', fontsize=25, labelpad=23, fontweight='bold')
    #ax.set_xticks(x)
    plt.show()


def plot_elevation_belem():

    files_map = '../data/maps/m48.488877797764935_m1.484547838679201_m48.45585981539186_m1.4448492646059234.graphml'
    G = ox.load_graphml(files_map)

    max_lat = -1.449
    min_lat = -1.479
    max_lon = -48.462
    min_lon = -48.488

    name_geotiff = '../data/maps/01S495ZN.tif'
    G = ox.graph_from_bbox(max_lat, min_lat, max_lon, min_lon, network_type='all')
    G = Graph.set_node_elevation(G, name_geotiff)
    G = Graph.edge_grades(G)
    # G_proj = ox.project_graph(G)
    nc = ox.plot.get_node_colors_by_attr(G, 'elevation', cmap='plasma', num_bins=10)  # , start=0, stop=1
    cmap = plt.cm.get_cmap('plasma')
    print("belem", max(list(nx.get_node_attributes(G, 'elevation').values()))-
          min(list(nx.get_node_attributes(G, 'elevation').values())))
    norm = plt.Normalize(vmin=min(list(nx.get_node_attributes(G, 'elevation').values())), vmax=max(list(nx.get_node_attributes(G, 'elevation').values())))
    sm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
    sm.set_array([])

    fig, ax = ox.plot_graph(G, node_color=nc, node_size=45, edge_linewidth=0.7, bgcolor='w', show=False)
    # pad: position of colorbar, shrink=.92: colorbar size
    cb = fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, orientation='vertical', shrink=.94, fraction=0.15,
                      pad=-0.0001)
    cb.ax.tick_params(labelsize=25)
    cb.set_label('Elevação (m)', fontsize=25, labelpad=23, fontweight='bold')
    plt.show()


if __name__ == '__main__':
    plot_elevation()

