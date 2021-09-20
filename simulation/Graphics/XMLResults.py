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
            print(alg, k, j)
            files_result = Results.create_list_files(k, alg, j, '', extension, n_points)
            m, h = average_xml(files_result, data)
            medias.append(m)
            errors.append(h)
            print(medias)
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
    plt.ylim(0, max(max(medias[2]),max(medias[1]), max(medias[0]))+1)
    plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(numpoints=1, loc="upper left", ncol=3, prop={'size': 10})
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    graphic('duration', 24)
    graphic('routeLength', 24)