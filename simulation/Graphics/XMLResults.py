import Results
from xml.dom import minidom
import numpy as np
import matplotlib.pyplot as plt


def average_xml(files_result, data, confidence=0.95):
    all_times = []
    for a in files_result:
        file = minidom.parse('../../' + a)
        tag = file.getElementsByTagName('tripinfo')
        duration = [float(node.attributes[data].value) for node in tag]
        if data == 'duration':
            all_times.append(duration[0] / 3600)
        else:
            all_times.append(duration[0] / 1000)
    m, h = Results.mean_confidence_interval(all_times, confidence)
    return m, h


def medias_and_errors_xml(heuristics, alg, politic, extension, data, n_points):
    all_medias = []
    all_errors = []
    for k in politic:
        medias = []
        errors = []
        for j in heuristics:
            files_result = Results.create_list_files(k, alg, j, '', extension, n_points)
            m, h = average_xml(files_result, data)
            medias.append(m)
            errors.append(h)
        all_medias.append(medias)
        all_errors.append(errors)
    return all_medias, all_errors


def graphic(data, n_points):
    politics = ['weight', 'impedance', 'length']
    alg = 'SPFA'
    heuristics = ['nearest_neighbor', 'closest_insertion', 'farthest_insertion']

    medias, errors = medias_and_errors_xml(heuristics, alg, politics, '.xml', data, n_points)

    labels = ['Vizinho mais próximo', 'Inserção do mais próximo', 'Inserção do mais distante']

    x = np.arange(len(labels))  # the label locations
    width = 0.25  # 0.35  # the width of the bars

    fig, ax = plt.subplots()
    r1 = ax.bar(x - width, medias[0], width, yerr=errors[0], label='PMT', zorder=10)
    r2 = ax.bar(x, medias[1], width, yerr=errors[1], label='PMI', zorder=10)
    r3 = ax.bar(x + width, medias[2], width, yerr=errors[2], label='PMD', zorder=10)

    # Add some text for labels, title and custom x-axis tick labels, etc.

    if data == 'duration':
        plt.ylabel('Tempo [h]', fontweight="bold", fontsize=11)
    else:
        plt.ylabel('Distância [Km]', fontweight="bold", fontsize=11)
    plt.ylim(0, max(max(medias[2]),max(medias[1]), max(medias[0]))+1.5)
    plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(numpoints=1, loc="upper left", ncol=3, prop={'size': 10})
    fig.tight_layout()
    plt.show()


def graphic_all(data, n_points):

    politics = ['weight', 'impedance', 'length']
    algs = ['SPFA', 'dijkstra', 'astar']
    heuristics = ['nearest_neighbor', 'closest_insertion', 'farthest_insertion']

    medias, errors = medias_and_errors_xml(heuristics, algs[0], politics, '.xml', data, n_points)
    a = [medias[i].append(float(0)) for i in range(3)]
    b = [errors[i].append(float(0)) for i in range(3)]
    a = [medias[i].append(float(0)) for i in range(3)]
    b = [errors[i].append(float(0)) for i in range(3)]
    a = [medias[i].append(float(0)) for i in range(3)]
    b = [errors[i].append(float(0)) for i in range(3)]
    a = [medias[i].append(float(0)) for i in range(3)]
    b = [errors[i].append(float(0)) for i in range(3)]

    medias1, errors1 = medias_and_errors_xml(heuristics, algs[0], politics, '.xml', data, int(n_points + 100))
    a = [medias1[i].insert(0, float(0)) for i in range(3)]
    b = [errors1[i].insert(0, float(0)) for i in range(3)]
    a = [medias1[i].insert(0, float(0)) for i in range(3)]
    b = [errors1[i].insert(0, float(0)) for i in range(3)]
    a = [medias1[i].insert(0, float(0)) for i in range(3)]
    b = [errors1[i].insert(0, float(0)) for i in range(3)]
    a = [medias1[i].insert(0, float(0)) for i in range(3)]
    b = [errors1[i].insert(0, float(0)) for i in range(3)]

    labels = ['VP', 'IP', 'ID', '', 'VP', 'IP', 'ID']

    x = np.arange(len(labels))  # the label locations
    width = 0.25  # 0.35  # the width of the bars

    fig, ax = plt.subplots()
    r1 = ax.bar(x - width, medias[0], width, yerr=errors[0], label='PMT', zorder=10, color='tab:blue')
    r4 = ax.bar(x, medias1[0], width, yerr=errors1[1], zorder=10, color='tab:blue') #PMT
    r2 = ax.bar(x, medias[1], width, yerr=errors[1], label='PMI', zorder=10, color='darkorange')
    r5 = ax.bar(x + width, medias1[1], width, yerr=errors1[2], zorder=10, color='darkorange') #PMI
    r3 = ax.bar(x + width, medias[2], width, yerr=errors[2], label='PMD', zorder=10, color='tab:green')
    r6 = ax.bar(x - width, medias1[2], width, yerr=errors1[0], zorder=10, color='tab:green') #PMD

    # Add some text for labels, title and custom x-axis tick labels, etc.
    if data == 'duration':
        plt.ylabel('Tempo [h]', fontweight="bold", fontsize=11)
    else:
        plt.ylabel('Distância [Km]', fontweight="bold", fontsize=11)
    plt.ylim(0, max(max(medias[2]),max(medias[1]), max(medias[0]))+1.5)
    plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)
    ax.set_xticks(x)
    ax.set_xlabel("Heurísticas")
    ax.set_xticklabels(labels)
    ax.legend(numpoints=1, loc="upper center", ncol=3, prop={'size': 10})

    ax2 = ax.twiny()
    ax2.set_xlabel("Cidade do cenário")
    #ax2.set_xticks(['1', '5'])
    ax2.set_xticklabels(['','São Paulo','','','Belém',''])

    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    #graphic('duration', 12)
    #graphic('duration', 112)
    #graphic('routeLength', 12)
    graphic_all('routeLength', 24)
    #graphic_all('routeLength', 24)