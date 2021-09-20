import json
import scipy.stats
import matplotlib.pyplot as plt
import numpy as np


def open_file(nameFile):
    try:
        f = open(nameFile + ".json", "r")
        dados = json.loads(f.read())
        f.close()
    except:
        dados = 0
        pass

    return dados


def mean_confidence_interval(data, confidence=0.90):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n - 1)
    #return m, m - h, m + h
    return m, h

"""
files = ['../data/results/m43.957018117658315_m19.931545102455843_m43.931890481507786_m19.907162672548026_0_coords_distance_heuristic_dijkstra_nn']
files_s = ['../data/results/m43.96267779776494_m19.944747838679202_m43.929659815391865_m19.905049264605925_0_coords_distance_heuristic_SPFA_nn']
files_a = ['../data/results/m43.96267779776494_m19.944747838679202_m43.929659815391865_m19.905049264605925_0_coords_distance_heuristic_astar_nn']

files_ci = ['../data/results/m43.957018117658315_m19.931545102455843_m43.931890481507786_m19.907162672548026_0_coords_distance_heuristic_dijkstra_ci']
files_s_ci = ['../data/results/m43.96267779776494_m19.944747838679202_m43.929659815391865_m19.905049264605925_0_coords_distance_heuristic_SPFA_ci']
files_a_ci = ['../data/results/m43.96267779776494_m19.944747838679202_m43.929659815391865_m19.905049264605925_0_coords_distance_heuristic_astar_ci']

files_fi = ['../data/results/m43.96267779776494_m19.944747838679202_m43.929659815391865_m19.905049264605925_0_coords_distance_heuristic_dijkstra_fi']
files_s_fi = ['../data/results/m43.96267779776494_m19.944747838679202_m43.929659815391865_m19.905049264605925_0_coords_distance_heuristic_SPFA_fi']
files_a_fi = ['../data/results/m43.96267779776494_m19.944747838679202_m43.929659815391865_m19.905049264605925_0_coords_distance_heuristic_astar_fi']
"""

files = [
         '../data/results/m38.49905230272549_m12.960541036813272_m38.47398437502447_m12.935229804750517_0_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.499613596916454_m12.961216812913838_m38.47548425277925_m12.934070088770925_1_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.50194412971296_m12.9624676749896_m38.472997875909336_m12.93487294586209_2_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.498581450235484_m12.9619559499298_m38.475389747728904_m12.934784985867735_3_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.49996781691653_m12.95986050660711_m38.474784788561664_m12.933876269107426_4_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.50102106363388_m12.960490752611433_m38.47530338641699_m12.935070144844953_5_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.50130467830106_m12.961824509508324_m38.47401790429914_m12.931900743216616_6_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.49922134252434_m12.959719860966981_m38.47230805005746_m12.932265326057136_7_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.499023327452186_m12.96043952416794_m38.47288011285585_m12.935194971832598_8_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.50157434253033_m12.960963430607745_m38.47367938539426_m12.934943284635198_9_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.50173708534096_m12.961142864695704_m38.472735872376994_m12.934002867600155_10_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.501770300615625_m12.962923879056133_m38.47456776187294_m12.933458582758297_11_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.500350682125635_m12.962082099834404_m38.474252489838484_m12.933159784666088_12_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.499541957062846_m12.961275066314741_m38.47543065870227_m12.933077757489697_13_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.50096584572687_m12.960054889071188_m38.47537633515103_m12.93494576442133_14_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.49992604759511_m12.96137329471482_m38.474439318456355_m12.934385438592946_15_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.501118552381065_m12.96079542837906_m38.47527163205215_m12.934807266431482_16_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.5002628268697_m12.96291845683024_m38.474969528890774_m12.935323121601408_17_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.50148403583942_m12.959860721735883_m38.473738459371354_m12.932454395581454_18_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.50449792282273_m12.960749843857812_m38.47312892278054_m12.934855166198494_19_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.501890924160584_m12.961519343957082_m38.474698888311465_m12.933784238917099_20_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.5007597052321_m12.959937832694857_m38.4746987632653_m12.934062022103753_21_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.50140543268961_m12.962059262780658_m38.47465373021255_m12.933888947418161_22_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.502953641658266_m12.963948797656334_m38.473898022861405_m12.935715998602321_23_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.50187151458964_m12.960561184183135_m38.47481398113283_m12.934620537016835_24_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.501402782516365_m12.96039753671852_m38.47361068224981_m12.93529938288262_25_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.49976769604373_m12.961496062259055_m38.474156963136124_m12.934301693944008_26_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.500486678608006_m12.959835378598493_m38.474758327361364_m12.936386705101464_27_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.50066682622218_m12.960812050907476_m38.47216531424985_m12.934908879722355_28_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.50234447884447_m12.962113594988761_m38.47520010149299_m12.935206277553998_29_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra',
         '../data/results/m38.501602450236554_m12.962836591132051_m38.47539177946605_m12.934754563384551_30_15_length_heuristic_dijkstra_nearest_neighbor_coords_length_heuristic_dijkstra'
         ]

files_s = [
           '../data/results/m38.49905230272549_m12.960541036813272_m38.47398437502447_m12.935229804750517_0_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.499613596916454_m12.961216812913838_m38.47548425277925_m12.934070088770925_1_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.50194412971296_m12.9624676749896_m38.472997875909336_m12.93487294586209_2_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.498581450235484_m12.9619559499298_m38.475389747728904_m12.934784985867735_3_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.49996781691653_m12.95986050660711_m38.474784788561664_m12.933876269107426_4_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.50102106363388_m12.960490752611433_m38.47530338641699_m12.935070144844953_5_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.50130467830106_m12.961824509508324_m38.47401790429914_m12.931900743216616_6_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.49922134252434_m12.959719860966981_m38.47230805005746_m12.932265326057136_7_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.499023327452186_m12.96043952416794_m38.47288011285585_m12.935194971832598_8_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.50157434253033_m12.960963430607745_m38.47367938539426_m12.934943284635198_9_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.50173708534096_m12.961142864695704_m38.472735872376994_m12.934002867600155_10_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.501770300615625_m12.962923879056133_m38.47456776187294_m12.933458582758297_11_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.500350682125635_m12.962082099834404_m38.474252489838484_m12.933159784666088_12_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.499541957062846_m12.961275066314741_m38.47543065870227_m12.933077757489697_13_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.50096584572687_m12.960054889071188_m38.47537633515103_m12.93494576442133_14_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.49992604759511_m12.96137329471482_m38.474439318456355_m12.934385438592946_15_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.501118552381065_m12.96079542837906_m38.47527163205215_m12.934807266431482_16_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.5002628268697_m12.96291845683024_m38.474969528890774_m12.935323121601408_17_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.50148403583942_m12.959860721735883_m38.473738459371354_m12.932454395581454_18_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.50449792282273_m12.960749843857812_m38.47312892278054_m12.934855166198494_19_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.501890924160584_m12.961519343957082_m38.474698888311465_m12.933784238917099_20_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.5007597052321_m12.959937832694857_m38.4746987632653_m12.934062022103753_21_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.50140543268961_m12.962059262780658_m38.47465373021255_m12.933888947418161_22_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.502953641658266_m12.963948797656334_m38.473898022861405_m12.935715998602321_23_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.50187151458964_m12.960561184183135_m38.47481398113283_m12.934620537016835_24_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.501402782516365_m12.96039753671852_m38.47361068224981_m12.93529938288262_25_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.49976769604373_m12.961496062259055_m38.474156963136124_m12.934301693944008_26_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.500486678608006_m12.959835378598493_m38.474758327361364_m12.936386705101464_27_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.50066682622218_m12.960812050907476_m38.47216531424985_m12.934908879722355_28_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.50234447884447_m12.962113594988761_m38.47520010149299_m12.935206277553998_29_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA',
           '../data/results/m38.501602450236554_m12.962836591132051_m38.47539177946605_m12.934754563384551_30_15_length_heuristic_SPFA_nearest_neighbor_coords_length_heuristic_SPFA'
           ]

files_a = [
            '../data/results/m38.49905230272549_m12.960541036813272_m38.47398437502447_m12.935229804750517_0_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.499613596916454_m12.961216812913838_m38.47548425277925_m12.934070088770925_1_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.50194412971296_m12.9624676749896_m38.472997875909336_m12.93487294586209_2_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.498581450235484_m12.9619559499298_m38.475389747728904_m12.934784985867735_3_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.49996781691653_m12.95986050660711_m38.474784788561664_m12.933876269107426_4_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.50102106363388_m12.960490752611433_m38.47530338641699_m12.935070144844953_5_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.50130467830106_m12.961824509508324_m38.47401790429914_m12.931900743216616_6_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.49922134252434_m12.959719860966981_m38.47230805005746_m12.932265326057136_7_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.499023327452186_m12.96043952416794_m38.47288011285585_m12.935194971832598_8_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.50157434253033_m12.960963430607745_m38.47367938539426_m12.934943284635198_9_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.50173708534096_m12.961142864695704_m38.472735872376994_m12.934002867600155_10_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.501770300615625_m12.962923879056133_m38.47456776187294_m12.933458582758297_11_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.500350682125635_m12.962082099834404_m38.474252489838484_m12.933159784666088_12_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.499541957062846_m12.961275066314741_m38.47543065870227_m12.933077757489697_13_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.50096584572687_m12.960054889071188_m38.47537633515103_m12.93494576442133_14_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.49992604759511_m12.96137329471482_m38.474439318456355_m12.934385438592946_15_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.501118552381065_m12.96079542837906_m38.47527163205215_m12.934807266431482_16_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.5002628268697_m12.96291845683024_m38.474969528890774_m12.935323121601408_17_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.50148403583942_m12.959860721735883_m38.473738459371354_m12.932454395581454_18_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.50449792282273_m12.960749843857812_m38.47312892278054_m12.934855166198494_19_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.501890924160584_m12.961519343957082_m38.474698888311465_m12.933784238917099_20_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.5007597052321_m12.959937832694857_m38.4746987632653_m12.934062022103753_21_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.50140543268961_m12.962059262780658_m38.47465373021255_m12.933888947418161_22_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.502953641658266_m12.963948797656334_m38.473898022861405_m12.935715998602321_23_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.50187151458964_m12.960561184183135_m38.47481398113283_m12.934620537016835_24_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.501402782516365_m12.96039753671852_m38.47361068224981_m12.93529938288262_25_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.49976769604373_m12.961496062259055_m38.474156963136124_m12.934301693944008_26_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.500486678608006_m12.959835378598493_m38.474758327361364_m12.936386705101464_27_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.50066682622218_m12.960812050907476_m38.47216531424985_m12.934908879722355_28_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.50234447884447_m12.962113594988761_m38.47520010149299_m12.935206277553998_29_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar',
            '../data/results/m38.501602450236554_m12.962836591132051_m38.47539177946605_m12.934754563384551_30_15_length_heuristic_astar_nearest_neighbor_coords_length_heuristic_astar'
        ]

files_ci = [
        '../data/results/m38.49905230272549_m12.960541036813272_m38.47398437502447_m12.935229804750517_0_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.499613596916454_m12.961216812913838_m38.47548425277925_m12.934070088770925_1_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50194412971296_m12.9624676749896_m38.472997875909336_m12.93487294586209_2_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.498581450235484_m12.9619559499298_m38.475389747728904_m12.934784985867735_3_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.49996781691653_m12.95986050660711_m38.474784788561664_m12.933876269107426_4_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50102106363388_m12.960490752611433_m38.47530338641699_m12.935070144844953_5_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50130467830106_m12.961824509508324_m38.47401790429914_m12.931900743216616_6_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.49922134252434_m12.959719860966981_m38.47230805005746_m12.932265326057136_7_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.499023327452186_m12.96043952416794_m38.47288011285585_m12.935194971832598_8_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50157434253033_m12.960963430607745_m38.47367938539426_m12.934943284635198_9_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50173708534096_m12.961142864695704_m38.472735872376994_m12.934002867600155_10_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.501770300615625_m12.962923879056133_m38.47456776187294_m12.933458582758297_11_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.500350682125635_m12.962082099834404_m38.474252489838484_m12.933159784666088_12_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.499541957062846_m12.961275066314741_m38.47543065870227_m12.933077757489697_13_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50096584572687_m12.960054889071188_m38.47537633515103_m12.93494576442133_14_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.49992604759511_m12.96137329471482_m38.474439318456355_m12.934385438592946_15_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.501118552381065_m12.96079542837906_m38.47527163205215_m12.934807266431482_16_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.5002628268697_m12.96291845683024_m38.474969528890774_m12.935323121601408_17_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50148403583942_m12.959860721735883_m38.473738459371354_m12.932454395581454_18_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50449792282273_m12.960749843857812_m38.47312892278054_m12.934855166198494_19_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.501890924160584_m12.961519343957082_m38.474698888311465_m12.933784238917099_20_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.5007597052321_m12.959937832694857_m38.4746987632653_m12.934062022103753_21_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50140543268961_m12.962059262780658_m38.47465373021255_m12.933888947418161_22_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.502953641658266_m12.963948797656334_m38.473898022861405_m12.935715998602321_23_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50187151458964_m12.960561184183135_m38.47481398113283_m12.934620537016835_24_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.501402782516365_m12.96039753671852_m38.47361068224981_m12.93529938288262_25_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.49976769604373_m12.961496062259055_m38.474156963136124_m12.934301693944008_26_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.500486678608006_m12.959835378598493_m38.474758327361364_m12.936386705101464_27_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50066682622218_m12.960812050907476_m38.47216531424985_m12.934908879722355_28_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50234447884447_m12.962113594988761_m38.47520010149299_m12.935206277553998_29_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.501602450236554_m12.962836591132051_m38.47539177946605_m12.934754563384551_30_15_length_heuristic_dijkstra_closest_insertion_coords_length_heuristic_dijkstra'
        ]

files_s_ci = [
        '../data/results/m38.49905230272549_m12.960541036813272_m38.47398437502447_m12.935229804750517_0_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.499613596916454_m12.961216812913838_m38.47548425277925_m12.934070088770925_1_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50194412971296_m12.9624676749896_m38.472997875909336_m12.93487294586209_2_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.498581450235484_m12.9619559499298_m38.475389747728904_m12.934784985867735_3_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.49996781691653_m12.95986050660711_m38.474784788561664_m12.933876269107426_4_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50102106363388_m12.960490752611433_m38.47530338641699_m12.935070144844953_5_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50130467830106_m12.961824509508324_m38.47401790429914_m12.931900743216616_6_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.49922134252434_m12.959719860966981_m38.47230805005746_m12.932265326057136_7_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.499023327452186_m12.96043952416794_m38.47288011285585_m12.935194971832598_8_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50157434253033_m12.960963430607745_m38.47367938539426_m12.934943284635198_9_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50173708534096_m12.961142864695704_m38.472735872376994_m12.934002867600155_10_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.501770300615625_m12.962923879056133_m38.47456776187294_m12.933458582758297_11_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.500350682125635_m12.962082099834404_m38.474252489838484_m12.933159784666088_12_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.499541957062846_m12.961275066314741_m38.47543065870227_m12.933077757489697_13_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50096584572687_m12.960054889071188_m38.47537633515103_m12.93494576442133_14_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.49992604759511_m12.96137329471482_m38.474439318456355_m12.934385438592946_15_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.501118552381065_m12.96079542837906_m38.47527163205215_m12.934807266431482_16_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.5002628268697_m12.96291845683024_m38.474969528890774_m12.935323121601408_17_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50148403583942_m12.959860721735883_m38.473738459371354_m12.932454395581454_18_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50449792282273_m12.960749843857812_m38.47312892278054_m12.934855166198494_19_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.501890924160584_m12.961519343957082_m38.474698888311465_m12.933784238917099_20_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.5007597052321_m12.959937832694857_m38.4746987632653_m12.934062022103753_21_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50140543268961_m12.962059262780658_m38.47465373021255_m12.933888947418161_22_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.502953641658266_m12.963948797656334_m38.473898022861405_m12.935715998602321_23_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50187151458964_m12.960561184183135_m38.47481398113283_m12.934620537016835_24_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.501402782516365_m12.96039753671852_m38.47361068224981_m12.93529938288262_25_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.49976769604373_m12.961496062259055_m38.474156963136124_m12.934301693944008_26_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.500486678608006_m12.959835378598493_m38.474758327361364_m12.936386705101464_27_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50066682622218_m12.960812050907476_m38.47216531424985_m12.934908879722355_28_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50234447884447_m12.962113594988761_m38.47520010149299_m12.935206277553998_29_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.501602450236554_m12.962836591132051_m38.47539177946605_m12.934754563384551_30_15_length_heuristic_SPFA_closest_insertion_coords_length_heuristic_SPFA'
        ]

files_a_ci = [
        '../data/results/m38.49905230272549_m12.960541036813272_m38.47398437502447_m12.935229804750517_0_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.499613596916454_m12.961216812913838_m38.47548425277925_m12.934070088770925_1_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50194412971296_m12.9624676749896_m38.472997875909336_m12.93487294586209_2_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.498581450235484_m12.9619559499298_m38.475389747728904_m12.934784985867735_3_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.49996781691653_m12.95986050660711_m38.474784788561664_m12.933876269107426_4_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50102106363388_m12.960490752611433_m38.47530338641699_m12.935070144844953_5_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50130467830106_m12.961824509508324_m38.47401790429914_m12.931900743216616_6_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.49922134252434_m12.959719860966981_m38.47230805005746_m12.932265326057136_7_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.499023327452186_m12.96043952416794_m38.47288011285585_m12.935194971832598_8_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50157434253033_m12.960963430607745_m38.47367938539426_m12.934943284635198_9_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50173708534096_m12.961142864695704_m38.472735872376994_m12.934002867600155_10_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.501770300615625_m12.962923879056133_m38.47456776187294_m12.933458582758297_11_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.500350682125635_m12.962082099834404_m38.474252489838484_m12.933159784666088_12_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.499541957062846_m12.961275066314741_m38.47543065870227_m12.933077757489697_13_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50096584572687_m12.960054889071188_m38.47537633515103_m12.93494576442133_14_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.49992604759511_m12.96137329471482_m38.474439318456355_m12.934385438592946_15_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.501118552381065_m12.96079542837906_m38.47527163205215_m12.934807266431482_16_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.5002628268697_m12.96291845683024_m38.474969528890774_m12.935323121601408_17_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50148403583942_m12.959860721735883_m38.473738459371354_m12.932454395581454_18_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50449792282273_m12.960749843857812_m38.47312892278054_m12.934855166198494_19_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.501890924160584_m12.961519343957082_m38.474698888311465_m12.933784238917099_20_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.5007597052321_m12.959937832694857_m38.4746987632653_m12.934062022103753_21_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50140543268961_m12.962059262780658_m38.47465373021255_m12.933888947418161_22_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.502953641658266_m12.963948797656334_m38.473898022861405_m12.935715998602321_23_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50187151458964_m12.960561184183135_m38.47481398113283_m12.934620537016835_24_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.501402782516365_m12.96039753671852_m38.47361068224981_m12.93529938288262_25_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.49976769604373_m12.961496062259055_m38.474156963136124_m12.934301693944008_26_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.500486678608006_m12.959835378598493_m38.474758327361364_m12.936386705101464_27_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50066682622218_m12.960812050907476_m38.47216531424985_m12.934908879722355_28_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50234447884447_m12.962113594988761_m38.47520010149299_m12.935206277553998_29_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar',
        '../data/results/m38.501602450236554_m12.962836591132051_m38.47539177946605_m12.934754563384551_30_15_length_heuristic_astar_closest_insertion_coords_length_heuristic_astar'
        ]

files_fi = [
        '../data/results/m38.49905230272549_m12.960541036813272_m38.47398437502447_m12.935229804750517_0_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.499613596916454_m12.961216812913838_m38.47548425277925_m12.934070088770925_1_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50194412971296_m12.9624676749896_m38.472997875909336_m12.93487294586209_2_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.498581450235484_m12.9619559499298_m38.475389747728904_m12.934784985867735_3_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.49996781691653_m12.95986050660711_m38.474784788561664_m12.933876269107426_4_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50102106363388_m12.960490752611433_m38.47530338641699_m12.935070144844953_5_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50130467830106_m12.961824509508324_m38.47401790429914_m12.931900743216616_6_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.49922134252434_m12.959719860966981_m38.47230805005746_m12.932265326057136_7_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.499023327452186_m12.96043952416794_m38.47288011285585_m12.935194971832598_8_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50157434253033_m12.960963430607745_m38.47367938539426_m12.934943284635198_9_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50173708534096_m12.961142864695704_m38.472735872376994_m12.934002867600155_10_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.501770300615625_m12.962923879056133_m38.47456776187294_m12.933458582758297_11_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.500350682125635_m12.962082099834404_m38.474252489838484_m12.933159784666088_12_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.499541957062846_m12.961275066314741_m38.47543065870227_m12.933077757489697_13_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50096584572687_m12.960054889071188_m38.47537633515103_m12.93494576442133_14_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.49992604759511_m12.96137329471482_m38.474439318456355_m12.934385438592946_15_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.501118552381065_m12.96079542837906_m38.47527163205215_m12.934807266431482_16_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.5002628268697_m12.96291845683024_m38.474969528890774_m12.935323121601408_17_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50148403583942_m12.959860721735883_m38.473738459371354_m12.932454395581454_18_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50449792282273_m12.960749843857812_m38.47312892278054_m12.934855166198494_19_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.501890924160584_m12.961519343957082_m38.474698888311465_m12.933784238917099_20_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.5007597052321_m12.959937832694857_m38.4746987632653_m12.934062022103753_21_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50140543268961_m12.962059262780658_m38.47465373021255_m12.933888947418161_22_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.502953641658266_m12.963948797656334_m38.473898022861405_m12.935715998602321_23_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50187151458964_m12.960561184183135_m38.47481398113283_m12.934620537016835_24_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.501402782516365_m12.96039753671852_m38.47361068224981_m12.93529938288262_25_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.49976769604373_m12.961496062259055_m38.474156963136124_m12.934301693944008_26_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.500486678608006_m12.959835378598493_m38.474758327361364_m12.936386705101464_27_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50066682622218_m12.960812050907476_m38.47216531424985_m12.934908879722355_28_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.50234447884447_m12.962113594988761_m38.47520010149299_m12.935206277553998_29_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra',
        '../data/results/m38.501602450236554_m12.962836591132051_m38.47539177946605_m12.934754563384551_30_15_length_heuristic_dijkstra_further_insertion_coords_length_heuristic_dijkstra'
]

files_s_fi = [
        '../data/results/m38.49905230272549_m12.960541036813272_m38.47398437502447_m12.935229804750517_0_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.499613596916454_m12.961216812913838_m38.47548425277925_m12.934070088770925_1_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50194412971296_m12.9624676749896_m38.472997875909336_m12.93487294586209_2_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.498581450235484_m12.9619559499298_m38.475389747728904_m12.934784985867735_3_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.49996781691653_m12.95986050660711_m38.474784788561664_m12.933876269107426_4_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50102106363388_m12.960490752611433_m38.47530338641699_m12.935070144844953_5_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50130467830106_m12.961824509508324_m38.47401790429914_m12.931900743216616_6_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.49922134252434_m12.959719860966981_m38.47230805005746_m12.932265326057136_7_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.499023327452186_m12.96043952416794_m38.47288011285585_m12.935194971832598_8_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50157434253033_m12.960963430607745_m38.47367938539426_m12.934943284635198_9_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50173708534096_m12.961142864695704_m38.472735872376994_m12.934002867600155_10_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.501770300615625_m12.962923879056133_m38.47456776187294_m12.933458582758297_11_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.500350682125635_m12.962082099834404_m38.474252489838484_m12.933159784666088_12_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.499541957062846_m12.961275066314741_m38.47543065870227_m12.933077757489697_13_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50096584572687_m12.960054889071188_m38.47537633515103_m12.93494576442133_14_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.49992604759511_m12.96137329471482_m38.474439318456355_m12.934385438592946_15_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.501118552381065_m12.96079542837906_m38.47527163205215_m12.934807266431482_16_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.5002628268697_m12.96291845683024_m38.474969528890774_m12.935323121601408_17_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50148403583942_m12.959860721735883_m38.473738459371354_m12.932454395581454_18_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50449792282273_m12.960749843857812_m38.47312892278054_m12.934855166198494_19_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.501890924160584_m12.961519343957082_m38.474698888311465_m12.933784238917099_20_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.5007597052321_m12.959937832694857_m38.4746987632653_m12.934062022103753_21_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50140543268961_m12.962059262780658_m38.47465373021255_m12.933888947418161_22_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.502953641658266_m12.963948797656334_m38.473898022861405_m12.935715998602321_23_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50187151458964_m12.960561184183135_m38.47481398113283_m12.934620537016835_24_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.501402782516365_m12.96039753671852_m38.47361068224981_m12.93529938288262_25_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.49976769604373_m12.961496062259055_m38.474156963136124_m12.934301693944008_26_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.500486678608006_m12.959835378598493_m38.474758327361364_m12.936386705101464_27_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50066682622218_m12.960812050907476_m38.47216531424985_m12.934908879722355_28_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.50234447884447_m12.962113594988761_m38.47520010149299_m12.935206277553998_29_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA',
        '../data/results/m38.501602450236554_m12.962836591132051_m38.47539177946605_m12.934754563384551_30_15_length_heuristic_SPFA_further_insertion_coords_length_heuristic_SPFA'
]

files_a_fi = [
        '../data/results/m38.49905230272549_m12.960541036813272_m38.47398437502447_m12.935229804750517_0_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.499613596916454_m12.961216812913838_m38.47548425277925_m12.934070088770925_1_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50194412971296_m12.9624676749896_m38.472997875909336_m12.93487294586209_2_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.498581450235484_m12.9619559499298_m38.475389747728904_m12.934784985867735_3_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.49996781691653_m12.95986050660711_m38.474784788561664_m12.933876269107426_4_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50102106363388_m12.960490752611433_m38.47530338641699_m12.935070144844953_5_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50130467830106_m12.961824509508324_m38.47401790429914_m12.931900743216616_6_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.49922134252434_m12.959719860966981_m38.47230805005746_m12.932265326057136_7_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.499023327452186_m12.96043952416794_m38.47288011285585_m12.935194971832598_8_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50157434253033_m12.960963430607745_m38.47367938539426_m12.934943284635198_9_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50173708534096_m12.961142864695704_m38.472735872376994_m12.934002867600155_10_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.501770300615625_m12.962923879056133_m38.47456776187294_m12.933458582758297_11_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.500350682125635_m12.962082099834404_m38.474252489838484_m12.933159784666088_12_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.499541957062846_m12.961275066314741_m38.47543065870227_m12.933077757489697_13_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50096584572687_m12.960054889071188_m38.47537633515103_m12.93494576442133_14_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.49992604759511_m12.96137329471482_m38.474439318456355_m12.934385438592946_15_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.501118552381065_m12.96079542837906_m38.47527163205215_m12.934807266431482_16_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.5002628268697_m12.96291845683024_m38.474969528890774_m12.935323121601408_17_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50148403583942_m12.959860721735883_m38.473738459371354_m12.932454395581454_18_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50449792282273_m12.960749843857812_m38.47312892278054_m12.934855166198494_19_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.501890924160584_m12.961519343957082_m38.474698888311465_m12.933784238917099_20_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.5007597052321_m12.959937832694857_m38.4746987632653_m12.934062022103753_21_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50140543268961_m12.962059262780658_m38.47465373021255_m12.933888947418161_22_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.502953641658266_m12.963948797656334_m38.473898022861405_m12.935715998602321_23_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50187151458964_m12.960561184183135_m38.47481398113283_m12.934620537016835_24_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.501402782516365_m12.96039753671852_m38.47361068224981_m12.93529938288262_25_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.49976769604373_m12.961496062259055_m38.474156963136124_m12.934301693944008_26_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.500486678608006_m12.959835378598493_m38.474758327361364_m12.936386705101464_27_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50066682622218_m12.960812050907476_m38.47216531424985_m12.934908879722355_28_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.50234447884447_m12.962113594988761_m38.47520010149299_m12.935206277553998_29_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar',
        '../data/results/m38.501602450236554_m12.962836591132051_m38.47539177946605_m12.934754563384551_30_15_length_heuristic_astar_further_insertion_coords_length_heuristic_astar'
]

todas_medias = []
todas_medias_s = []
todas_medias_a = []

todas_medias_ci = []
todas_medias_s_ci = []
todas_medias_a_ci = []

todas_medias_fi = []
todas_medias_s_fi = []
todas_medias_a_fi = []

for a in range(len(files)):

    dados_nn = dict(open_file(files[a]))
    dados_ci = dict(open_file(files_s[a]))
    dados_fi = dict(open_file(files_a[a]))

    todas_medias.append(float(dados_nn.get('total_time'))*1000)
    todas_medias_s.append(float(dados_ci.get('total_time'))*1000)
    todas_medias_a.append(float(dados_fi.get('total_time'))*1000)

    dados_ci_1 = dict(open_file(files_ci[a]))
    dados_ci_2 = dict(open_file(files_s_ci[a]))
    dados_ci_3 = dict(open_file(files_a_ci[a]))

    todas_medias_ci.append(float(dados_ci_1.get('total_time'))*1000)
    todas_medias_s_ci.append(float(dados_ci_2.get('total_time'))*1000)
    todas_medias_a_ci.append(float(dados_ci_3.get('total_time'))*1000)

    dados_fi_1 = dict(open_file(files_fi[a]))
    dados_fi_2 = dict(open_file(files_s_fi[a]))
    dados_fi_3 = dict(open_file(files_a_fi[a]))

    todas_medias_fi.append(float(dados_fi_1.get('total_time'))*1000)
    todas_medias_s_fi.append(float(dados_fi_2.get('total_time'))*1000)
    todas_medias_a_fi.append(float(dados_fi_3.get('total_time'))*1000)

m, h = mean_confidence_interval(todas_medias, 0.95)
m1, h1 = mean_confidence_interval(todas_medias_s, 0.95)
m2, h2 = mean_confidence_interval(todas_medias_a, 0.95)

m_ci, h_ci = mean_confidence_interval(todas_medias_ci, 0.95)
m1_ci, h1_ci = mean_confidence_interval(todas_medias_s_ci, 0.95)
m2_ci, h2_ci = mean_confidence_interval(todas_medias_a_ci, 0.95)

m_fi, h_fi = mean_confidence_interval(todas_medias_fi, 0.95)
m1_fi, h1_fi = mean_confidence_interval(todas_medias_s_fi, 0.95)
m2_fi, h2_fi = mean_confidence_interval(todas_medias_a_fi, 0.95)

medias = [m, m1, m2]
erros = [h, h1, h2]

medias_ci = [m_ci, m1_ci, m2_ci]
erros_ci = [h_ci, h1_ci, h2_ci]

medias_fi = [m_fi, m1_fi, m2_fi]
erros_fi = [h_fi, h1_fi, h2_fi]

labels = ['Bidirectional Dijkstra', 'SPFA', 'A-star']

x = np.arange(len(labels))  # the label locations
width = 0.45  # 0.35  # the width of the bars

print("medias",medias, "medias ci", medias_ci, "medias fi", medias_fi)

fig, ax = plt.subplots()
r1 = ax.bar(x - width/3, medias, width/3, yerr=erros, label='Nearest Neighbor', zorder=10)
r2 = ax.bar(x, medias_ci, width/3, yerr=erros_ci, label='Nearest Insertion', zorder=10)
r3 = ax.bar(x + width/3, medias_fi, width/3, yerr=erros_fi, label='Farthest Insertion', zorder=10)

plt.yscale('log')
# Add some text for labels, title and custom x-axis tick labels, etc.
#ax.set_ylabel('Potência média (W)', fontdict='bold')
plt.ylabel('Time [ms]', fontweight="bold", fontsize=11)
plt.ylim(10**(1), 10**(5)) #max(medias_ci) + 5)
plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0.5)
ax.set_xticks(x)
ax.set_xticklabels(labels)
#plt.xlabel([], )
ax.legend(numpoints=1, loc="upper right", ncol=3,  prop={'size': 9})

fig.tight_layout()

plt.show()