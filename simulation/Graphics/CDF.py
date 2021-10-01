import Results
from decimal import Decimal, ROUND_HALF_UP
import matplotlib.pyplot as plt
import json


def open_file(name_file):
    try:
        f = open('../../' + name_file, "r")
        data = json.loads(f.read())
        f.close()
    except:
        data = 0
        pass

    return data


def cdf_values(files_result):
    power = []
    for a in files_result:
        data = dict(open_file(a))
        for i in list(data.keys()):
            power.append(data.get(str(i)))

    pdf_power = [0] * (int(max(power)) + 10)
    cdf = [0] * (int(max(power)) + 10)

    for i in power:
        num = Decimal(float(i)).quantize(0, ROUND_HALF_UP)
        pdf_power[int(num)] += 1

    x = []
    cumulative = 0

    for i in range(len(pdf_power)):
        cumulative += (pdf_power[i] / len(power)) * 100
        x.append(i)
        cdf[i] = cumulative

    return x, cdf


def results(heuristics, alg, politic, extension, n_points):
    xs = []
    cdfs = []
    for k in politic:
        for j in heuristics:
            files_result = Results.create_list_files(k, alg, j, '', extension, n_points)
            x, cdf = cdf_values(files_result)
            xs.append(x)
            cdfs.append(cdf)
    return xs, cdfs


def graphic(n_points):
    politics = ['weight', 'impedance', 'length']
    alg = 'SPFA'
    heuristics = ['nearest_neighbor', 'closest_insertion', 'farthest_insertion']

    xs, cdfs = results(heuristics, alg, politics, '.json', n_points)

    xs1, cdfs1 = results(heuristics, alg, politics, '.json', n_points + 100)

    fig = plt.figure()
    plt.xlim(-7, 350)
    plt.xticks(size=13)
    plt.yticks(size=13)
    plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)

    plt.errorbar(xs1[0], cdfs1[0], label='PMT Belém', color='tab:red', ls="-", linewidth=1.5)  # Vizinho mais próximo
    # plt.errorbar(xs1[1], cdfs1[1], label='PMT Belém', color='tab:red', ls="-", linewidth=1.1) # Inserção do mais próximo
    # plt.errorbar(xs1[2], cdfs1[2], label='PMT Belém', color='tab:red', ls="-", linewidth=1.1)  # marker='P' # Inserção do mais distante
    plt.errorbar(xs1[3], cdfs1[3], label='PMI Belém', color='k', ls="-", linewidth=1.5)  # Vizinho mais próximo
    # plt.errorbar(xs1[4], cdfs1[4], label='PMI Belém', color='k', ls="-", linewidth=1.1) # Inserção do mais próximo
    # plt.errorbar(xs1[5], cdfs1[5], label='PMI Belém', color='k', ls="-", linewidth=1.1) # Inserção do mais distante
    plt.errorbar(xs1[6], cdfs1[6], label='PMD Belém', color='tab:pink', ls="-", linewidth=1.5)  # Vizinho mais próximo
    # plt.errorbar(xs1[7], cdfs1[7], label='PMD Belém', color='tab:pink', ls="-", linewidth=1.1) # Inserção do mais próximo
    # plt.errorbar(xs1[8], cdfs1[8], label='PMD Belém', color='k', ls="-", linewidth=1.1) # Inserção do mais distante

    plt.errorbar(xs[0], cdfs[0], label='PMT SP', color='tab:orange', ls="-", linewidth=1.5)  # Vizinho mais próximo
    # plt.errorbar(xs[1], cdfs[1], label='PMT SP', color='tab:orange', ls="-", linewidth=1.1) # Inserção do mais próximo
    # plt.errorbar(xs[2], cdfs[2], label='PMT SP', color='tab:orange', ls="-", linewidth=1.1)  # marker='P' # Inserção do mais distante
    plt.errorbar(xs[3], cdfs[3], label='PMI SP', color='tab:green', ls="-", linewidth=1.5)  # Vizinho mais próximo
    # plt.errorbar(xs[4], cdfs[4], label='PMI SP', color='tab:green', ls="-", linewidth=1.1) # Inserção do mais próximo
    # plt.errorbar(xs[5], cdfs[5], label='PMI SP', color='tab:green', ls="-", linewidth=1.1) # Inserção do mais distante
    plt.errorbar(xs[6], cdfs[6], label='PMD SP', color='tab:blue', ls="-", linewidth=1.5)  # Vizinho mais próximo
    # plt.errorbar(xs[7], cdfs[7], label='PMD SP', color='tab:blue', ls="-", linewidth=1.1) # Inserção do mais próximo
    # plt.errorbar(xs[8], cdfs[8], label='PMD SP', color='tab:blue', ls="-", linewidth=1.1) # Inserção do mais distante

    ylabel = 'Função de Distribuição Acumulada Empírica [%]'
    xlabel = 'Potência Instantânea [W]'

    plt.ylabel(ylabel, fontweight="bold", fontsize=11)
    plt.xlabel(xlabel, fontweight="bold", fontsize=11)

    plt.legend(numpoints=1, loc="lower right", ncol=1, prop={'size': 10})
    plt.show()


if __name__ == '__main__':
    graphic(18)
