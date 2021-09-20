import json
import scipy.stats
import matplotlib.pyplot as plt
import numpy as np
from Constants import *


def open_file(name_file):
    try:
        f = open('../' + name_file, "r")
        data = json.loads(f.read())
        f.close()
    except:
        data = 0
        pass

    return data


def mean_confidence_interval(data, confidence=0.90):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n - 1)
    return m, h


def create_list_files(politic, alg, heuristic, type, extension, n_points):
    """

    :param politic:
    :param alg:
    :param heuristic:

    :param type:            Ex: '_pdf_speed_', '_pdf_speeds_', '_i', '_coords'

    :param extension:
    :return:
    """

    if n_points == 12:
        files = FILES_12
    elif n_points == 18:
        files = FILES_18
    elif n_points == 24:
        files = FILES_24
    else:
        files = FILES_30

    files_result = []

    for i in files:
        files_result.append(i + '_' + politic + '_' + alg + '_' + heuristic + type + extension)
    return files_result


def average_power(files_result, confidence=0.95):
    all_averages = []
    for a in files_result:
        average_power = 0
        data = dict(open_file(a))
        for i in list(data.keys()):
            average_power += int(data.get(str(i)))
        average_power = average_power / len(list(data.keys()))
        all_averages.append(average_power)
    m, h = mean_confidence_interval(all_averages, confidence)
    return m, h


def average_time_processing(files_result, confidence=0.95):
    all_times = []
    for a in files_result:
        data = dict(open_file(a))
        all_times.append(float(data.get('total_time')))
    m, h = mean_confidence_interval(all_times, confidence)
    return m, h


def medias_and_errors(heuristics, alg, politic, extension, n_points):
    all_medias = []
    all_errors = []
    for k in politic:
        medias = []
        errors = []
        for j in heuristics:
            files_result = create_list_files(k, alg, j, '', extension, n_points)
            m, h = average_power(files_result)
            medias.append(m)
            errors.append(h)
        all_medias.append(medias)
        all_errors.append(errors)

    return all_medias, all_errors


def medias_and_errors_time(heuristics, alg, politic, extension, n_points):
    all_medias = []
    all_errors = []
    for k in heuristics:
        medias = []
        errors = []
        for j in alg:
            files_result = create_list_files(politic, j, k, '_coords', extension, n_points)
            m, h = average_time_processing(files_result)
            medias.append(m)
            errors.append(h)
        all_errors.append(errors)
        all_medias.append(medias)
    return all_medias, all_errors


def graphic_power(politics, heuristics, alg, n_points):

    medias, errors = medias_and_errors(heuristics, alg, politics, '.json', n_points)

    labels = ['Vizinho mais próximo', 'Inserção do mais próximo', 'Inserção do mais distante']

    x = np.arange(len(labels))  # the label locations
    width = 0.25  # 0.35  # the width of the bars

    fig, ax = plt.subplots()
    r1 = ax.bar(x - width, medias[0], width, yerr=errors[0], label='PMT', zorder=10)
    r2 = ax.bar(x, medias[1], width, yerr=errors[1], label='PMI', zorder=10)
    r3 = ax.bar(x + width, medias[2], width, yerr=errors[2], label='PMD', zorder=10)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    plt.ylabel('Potência [W]', fontweight="bold", fontsize=11)
    plt.ylim(0, max(max(medias[2]),max(medias[1]), max(medias[0]))+16)
    plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(numpoints=1, loc="upper left", ncol=3, prop={'size': 10})
    fig.tight_layout()
    plt.show()


def graphic_time_processing(politic, heuristics, alg, n_points):

    medias, errors = medias_and_errors_time(heuristics, alg, politic, '.json', n_points)

    labels = ['SPFA', 'Dijkstra Bidirecional', 'A-star']

    x = np.arange(len(labels))  # the label locations
    width = 0.45  # 0.35  # the width of the bars

    fig, ax = plt.subplots()
    r1 = ax.bar(x - width / 3, medias[0], width / 3, yerr=errors[0], label='Vizinho mais próximo', zorder=10)
    r2 = ax.bar(x, medias[1], width / 3, yerr=errors[1], label='Inserção do mais próximo', zorder=10)
    r3 = ax.bar(x + width / 3, medias[2], width / 3, yerr=errors[2], label='Inserção do mais distante', zorder=10)

    plt.yscale('log')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    plt.ylabel('Tempo [ms]', fontweight="bold", fontsize=11)
    plt.ylim(10 ** (-1), 10 ** (4))  # max(medias_ci) + 5)
    plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(numpoints=1, loc="upper right", ncol=1, prop={'size': 9})
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    politics = ['weight', 'impedance', 'length']
    alg = ['SPFA', 'dijkstra', 'astar']
    heuristics = ['nearest_neighbor', 'closest_insertion', 'farthest_insertion']
    #graphic_power(politics, heuristics, alg[0], 24)
    graphic_time_processing(politics[2], heuristics, alg, 12)