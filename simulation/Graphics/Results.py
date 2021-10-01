import json
import scipy.stats
import matplotlib.pyplot as plt
import numpy as np
from Constants import *
import matplotlib.ticker as ticker


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
        files = FILES_12_SP
    elif n_points == 112:
        files = FILES_12_BL
    elif n_points == 18:
        files = FILES_18_SP
    elif n_points == 118:
        files = FILES_18_BL
    elif n_points == 24:
        files = FILES_24_SP
    elif n_points == 124:
        files = FILES_24_BL

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
        print(a, float(data.get('total_time')))
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


def medias_and_errors_time2(heuristics, alg, politic, extension, n_points):
    d_medias = []
    d_errors = []
    s_medias = []
    s_errors = []
    a_medias = []
    a_errors = []
    for k in alg:
        for j in heuristics:
            for n in politics:
                files_result = create_list_files(n, k, j, '_coords', extension, n_points)
                m, h = average_time_processing(files_result)
                if n == 'weight':
                    s_medias.append(m)
                    s_errors.append(h)
                elif n == 'impedance':
                    a_medias.append(m)
                    a_errors.append(h)
                else:
                    d_medias.append(m)
                    d_errors.append(h)
    all_medias = [s_medias, a_medias, d_medias]
    all_errors = [s_errors, a_errors, d_errors]

    return all_medias, all_errors


def graphic_power(politics, heuristics, alg, n_points):

    medias, errors = medias_and_errors(heuristics, alg, politics, '.json', n_points)

    labels = ['Vizinho mais próximo', 'Inserção do mais próximo', 'Inserção do mais distante']

    x = np.arange(len(labels))  # the label locations
    width = 0.20  # 0.35  # the width of the bars

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


def graphic_power_all(politics, heuristics, algs, n_points):

    medias, errors = medias_and_errors(heuristics, algs[0], politics, '.json', n_points)
    a = [medias[i].append(float(0)) for i in range(3)]
    b = [errors[i].append(float(0)) for i in range(3)]
    a = [medias[i].append(float(0)) for i in range(3)]
    b = [errors[i].append(float(0)) for i in range(3)]
    a = [medias[i].append(float(0)) for i in range(3)]
    b = [errors[i].append(float(0)) for i in range(3)]
    a = [medias[i].append(float(0)) for i in range(3)]
    b = [errors[i].append(float(0)) for i in range(3)]
    print(medias, errors)

    medias1, errors1 = medias_and_errors(heuristics, algs[0], politics, '.json', int(n_points + 100))
    a = [medias1[i].insert(0, float(0)) for i in range(3)]
    b = [errors1[i].insert(0, float(0)) for i in range(3)]
    a = [medias1[i].insert(0, float(0)) for i in range(3)]
    b = [errors1[i].insert(0, float(0)) for i in range(3)]
    a = [medias1[i].insert(0, float(0)) for i in range(3)]
    b = [errors1[i].insert(0, float(0)) for i in range(3)]
    a = [medias1[i].insert(0, float(0)) for i in range(3)]
    b = [errors1[i].insert(0, float(0)) for i in range(3)]
    print(medias1, errors1)

    labels = ['VP', 'IP', 'ID', '', 'VP', 'IP', 'ID']

    x = np.arange(len(labels))  # the label locations
    width = 0.25  # 0.35  # the width of the bars

    fig, ax = plt.subplots()
    r1 = ax.bar(x - width, medias[0], width, yerr=errors[0], label='PMT', zorder=10, color='tab:blue')
    r2 = ax.bar(x, medias[1], width, yerr=errors[1], label='PMI', zorder=10, color='darkorange')
    r3 = ax.bar(x + width, medias[2], width, yerr=errors[2], label='PMD', zorder=10, color='tab:green')
    r6 = ax.bar(x - width, medias1[2], width, yerr=errors1[0], zorder=10, color='tab:green') #PMD
    r5 = ax.bar(x + width, medias1[1], width, yerr=errors1[2], zorder=10, color='darkorange')  # PMI
    r4 = ax.bar(x, medias1[0], width, yerr=errors1[1], zorder=10, color='tab:blue')  # PMT

    # Add some text for labels, title and custom x-axis tick labels, etc.
    plt.ylabel('Potência [W]', fontweight="bold", fontsize=11)
    plt.ylim(0, 75)
    plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)
    ax.set_xticks(x)
    ax.set_xlabel("Heurística", fontweight="bold", fontsize=11)
    ax.set_xticklabels(labels)
    ax.legend(numpoints=1, loc="upper center", ncol=3, prop={'size': 10})

    ax2 = ax.twiny()
    ax2.set_xlabel("Cidade do cenário", fontweight="bold", fontsize=11)
    #ax2.set_xticks(['1', '5'])
    ax2.set_xticklabels(['','São Paulo','','','Belém',''])

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
    plt.ylabel('Tempo [s]', fontweight="bold", fontsize=11)
    plt.ylim(10 ** (-2), 10 ** (3))  # max(medias_ci) + 5)
    plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(numpoints=1, loc="upper right", ncol=1, prop={'size': 9})
    fig.tight_layout()
    plt.show()


def graphic_time_all(politics, heuristics, alg, n_points):

    medias, errors = medias_and_errors_time2(heuristics, alg, politics, '.json', n_points)
    print(medias)

    labels = ['VP', 'IP', 'ID', 'VP', 'IP', 'ID', 'VP', 'IP', 'ID']

    x = np.arange(len(medias)*3)
    width = 0.55

    fig, ax = plt.subplots()
    r1 = ax.bar(x - width / 3, medias[0], width / 3, yerr=errors[0], label='PMT', zorder=10)
    r2 = ax.bar(x, medias[1], width / 3, yerr=errors[1], label='PMI', zorder=10)
    r3 = ax.bar(x + width / 3, medias[2], width / 3, yerr=errors[2], label='PMD', zorder=10)

    plt.yscale('log')
    plt.ylabel('Tempo [s]', fontweight="bold", fontsize=11)
    plt.ylim(10 ** (-2), 10 ** (3))
    plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_xlabel("Heurística", fontweight="bold", fontsize=11, labelpad = 7)
    ax.legend(numpoints=1, loc="upper center", ncol=3, prop={'size': 9})

    ax2 = ax.twiny()
    ax2.set_xlabel("Algoritmo de busca", fontweight="bold", fontsize=11, labelpad = 10)
    x2 = np.arange(7)
    ax2.set_xticks(x2)
    ax2.spines['bottom'].set_position(('axes', -0.22))
    ax2.set_xticklabels(['', 'SPFA','', 'Dijkstra Bidirecional', '', 'A-star', ''])
    ax2.tick_params(axis='x', labelbottom=True)
    ax2.xaxis.set_ticks_position("bottom")  # Added this line
    ax2.xaxis.set_label_position("bottom")  # Added this line

    """
    ax.xaxis.set_major_locator(ticker.MultipleLocator(3.0))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
    majors = ["SPFA", "Dijkstra", "A-star"]
    ax.xaxis.set_major_formatter(ticker.FixedFormatter(majors))
    minors = ['VP', 'IP', 'ID', 'VP', 'IP', 'ID', 'VP', 'IP', 'ID']
    ax.xaxis.set_minor_formatter(ticker.FixedFormatter(minors))
    """

    fig.tight_layout()
    plt.show()



if __name__ == '__main__':
    politics = ['weight', 'impedance', 'length']
    alg = ['SPFA', 'dijkstra', 'astar']
    heuristics = ['nearest_neighbor', 'closest_insertion', 'farthest_insertion']
    graphic_power_all(politics, heuristics, alg, 24)
    #graphic_time_all(politics, heuristics, alg, 118)
    # graphic_power(politics, heuristics, alg[0], 24)
    # graphic_power(politics, heuristics, alg[0], 124)
    # graphic_time_processing(politics[2], heuristics, alg, 112)