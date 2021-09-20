import json
import scipy.stats
import matplotlib.pyplot as plt
from decimal import Decimal, ROUND_HALF_UP
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


files = [
    '../data/results/m38.49905230272549_m12.960541036813272_m38.47398437502447_m12.935229804750517_0_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.499613596916454_m12.961216812913838_m38.47548425277925_m12.934070088770925_1_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.50194412971296_m12.9624676749896_m38.472997875909336_m12.93487294586209_2_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.498581450235484_m12.9619559499298_m38.475389747728904_m12.934784985867735_3_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.49996781691653_m12.95986050660711_m38.474784788561664_m12.933876269107426_4_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.50102106363388_m12.960490752611433_m38.47530338641699_m12.935070144844953_5_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.50130467830106_m12.961824509508324_m38.47401790429914_m12.931900743216616_6_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.49922134252434_m12.959719860966981_m38.47230805005746_m12.932265326057136_7_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.499023327452186_m12.96043952416794_m38.47288011285585_m12.935194971832598_8_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.50157434253033_m12.960963430607745_m38.47367938539426_m12.934943284635198_9_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.50173708534096_m12.961142864695704_m38.472735872376994_m12.934002867600155_10_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.501770300615625_m12.962923879056133_m38.47456776187294_m12.933458582758297_11_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.500350682125635_m12.962082099834404_m38.474252489838484_m12.933159784666088_12_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.499541957062846_m12.961275066314741_m38.47543065870227_m12.933077757489697_13_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.50096584572687_m12.960054889071188_m38.47537633515103_m12.93494576442133_14_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.49992604759511_m12.96137329471482_m38.474439318456355_m12.934385438592946_15_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.501118552381065_m12.96079542837906_m38.47527163205215_m12.934807266431482_16_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.5002628268697_m12.96291845683024_m38.474969528890774_m12.935323121601408_17_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.50148403583942_m12.959860721735883_m38.473738459371354_m12.932454395581454_18_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.50449792282273_m12.960749843857812_m38.47312892278054_m12.934855166198494_19_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.501890924160584_m12.961519343957082_m38.474698888311465_m12.933784238917099_20_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.5007597052321_m12.959937832694857_m38.4746987632653_m12.934062022103753_21_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.50140543268961_m12.962059262780658_m38.47465373021255_m12.933888947418161_22_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.502953641658266_m12.963948797656334_m38.473898022861405_m12.935715998602321_23_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.50187151458964_m12.960561184183135_m38.47481398113283_m12.934620537016835_24_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.501402782516365_m12.96039753671852_m38.47361068224981_m12.93529938288262_25_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.49976769604373_m12.961496062259055_m38.474156963136124_m12.934301693944008_26_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.500486678608006_m12.959835378598493_m38.474758327361364_m12.936386705101464_27_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.50066682622218_m12.960812050907476_m38.47216531424985_m12.934908879722355_28_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.50234447884447_m12.962113594988761_m38.47520010149299_m12.935206277553998_29_15_length_heuristic_SPFA_nearest_neighbor',
         '../data/results/m38.501602450236554_m12.962836591132051_m38.47539177946605_m12.934754563384551_30_15_length_heuristic_SPFA_nearest_neighbor'
]

files_i = [
    '../data/results/m38.49905230272549_m12.960541036813272_m38.47398437502447_m12.935229804750517_0_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.499613596916454_m12.961216812913838_m38.47548425277925_m12.934070088770925_1_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.50194412971296_m12.9624676749896_m38.472997875909336_m12.93487294586209_2_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.498581450235484_m12.9619559499298_m38.475389747728904_m12.934784985867735_3_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.49996781691653_m12.95986050660711_m38.474784788561664_m12.933876269107426_4_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.50102106363388_m12.960490752611433_m38.47530338641699_m12.935070144844953_5_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.50130467830106_m12.961824509508324_m38.47401790429914_m12.931900743216616_6_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.49922134252434_m12.959719860966981_m38.47230805005746_m12.932265326057136_7_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.499023327452186_m12.96043952416794_m38.47288011285585_m12.935194971832598_8_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.50157434253033_m12.960963430607745_m38.47367938539426_m12.934943284635198_9_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.50173708534096_m12.961142864695704_m38.472735872376994_m12.934002867600155_10_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.501770300615625_m12.962923879056133_m38.47456776187294_m12.933458582758297_11_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.500350682125635_m12.962082099834404_m38.474252489838484_m12.933159784666088_12_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.499541957062846_m12.961275066314741_m38.47543065870227_m12.933077757489697_13_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.50096584572687_m12.960054889071188_m38.47537633515103_m12.93494576442133_14_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.49992604759511_m12.96137329471482_m38.474439318456355_m12.934385438592946_15_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.501118552381065_m12.96079542837906_m38.47527163205215_m12.934807266431482_16_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.5002628268697_m12.96291845683024_m38.474969528890774_m12.935323121601408_17_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.50148403583942_m12.959860721735883_m38.473738459371354_m12.932454395581454_18_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.50449792282273_m12.960749843857812_m38.47312892278054_m12.934855166198494_19_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.501890924160584_m12.961519343957082_m38.474698888311465_m12.933784238917099_20_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.5007597052321_m12.959937832694857_m38.4746987632653_m12.934062022103753_21_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.50140543268961_m12.962059262780658_m38.47465373021255_m12.933888947418161_22_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.502953641658266_m12.963948797656334_m38.473898022861405_m12.935715998602321_23_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.50187151458964_m12.960561184183135_m38.47481398113283_m12.934620537016835_24_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.501402782516365_m12.96039753671852_m38.47361068224981_m12.93529938288262_25_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.49976769604373_m12.961496062259055_m38.474156963136124_m12.934301693944008_26_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.500486678608006_m12.959835378598493_m38.474758327361364_m12.936386705101464_27_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.50066682622218_m12.960812050907476_m38.47216531424985_m12.934908879722355_28_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.50234447884447_m12.962113594988761_m38.47520010149299_m12.935206277553998_29_15_length_heuristic_SPFA_closest_insertion',
   '../data/results/m38.501602450236554_m12.962836591132051_m38.47539177946605_m12.934754563384551_30_15_length_heuristic_SPFA_closest_insertion'
]

files_d = [
     '../data/results/m38.49905230272549_m12.960541036813272_m38.47398437502447_m12.935229804750517_0_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.499613596916454_m12.961216812913838_m38.47548425277925_m12.934070088770925_1_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50194412971296_m12.9624676749896_m38.472997875909336_m12.93487294586209_2_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.498581450235484_m12.9619559499298_m38.475389747728904_m12.934784985867735_3_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.49996781691653_m12.95986050660711_m38.474784788561664_m12.933876269107426_4_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50102106363388_m12.960490752611433_m38.47530338641699_m12.935070144844953_5_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50130467830106_m12.961824509508324_m38.47401790429914_m12.931900743216616_6_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.49922134252434_m12.959719860966981_m38.47230805005746_m12.932265326057136_7_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.499023327452186_m12.96043952416794_m38.47288011285585_m12.935194971832598_8_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50157434253033_m12.960963430607745_m38.47367938539426_m12.934943284635198_9_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50173708534096_m12.961142864695704_m38.472735872376994_m12.934002867600155_10_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.501770300615625_m12.962923879056133_m38.47456776187294_m12.933458582758297_11_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.500350682125635_m12.962082099834404_m38.474252489838484_m12.933159784666088_12_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.499541957062846_m12.961275066314741_m38.47543065870227_m12.933077757489697_13_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50096584572687_m12.960054889071188_m38.47537633515103_m12.93494576442133_14_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.49992604759511_m12.96137329471482_m38.474439318456355_m12.934385438592946_15_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.501118552381065_m12.96079542837906_m38.47527163205215_m12.934807266431482_16_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.5002628268697_m12.96291845683024_m38.474969528890774_m12.935323121601408_17_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50148403583942_m12.959860721735883_m38.473738459371354_m12.932454395581454_18_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50449792282273_m12.960749843857812_m38.47312892278054_m12.934855166198494_19_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.501890924160584_m12.961519343957082_m38.474698888311465_m12.933784238917099_20_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.5007597052321_m12.959937832694857_m38.4746987632653_m12.934062022103753_21_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50140543268961_m12.962059262780658_m38.47465373021255_m12.933888947418161_22_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.502953641658266_m12.963948797656334_m38.473898022861405_m12.935715998602321_23_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50187151458964_m12.960561184183135_m38.47481398113283_m12.934620537016835_24_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.501402782516365_m12.96039753671852_m38.47361068224981_m12.93529938288262_25_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.49976769604373_m12.961496062259055_m38.474156963136124_m12.934301693944008_26_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.500486678608006_m12.959835378598493_m38.474758327361364_m12.936386705101464_27_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50066682622218_m12.960812050907476_m38.47216531424985_m12.934908879722355_28_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50234447884447_m12.962113594988761_m38.47520010149299_m12.935206277553998_29_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.501602450236554_m12.962836591132051_m38.47539177946605_m12.934754563384551_30_15_length_heuristic_SPFA_further_insertion'
]


files_b = [
    '../data/results/m38.49905230272549_m12.960541036813272_m38.47398437502447_m12.935229804750517_0_15_length_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.499613596916454_m12.961216812913838_m38.47548425277925_m12.934070088770925_1_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.50194412971296_m12.9624676749896_m38.472997875909336_m12.93487294586209_2_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.498581450235484_m12.9619559499298_m38.475389747728904_m12.934784985867735_3_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.49996781691653_m12.95986050660711_m38.474784788561664_m12.933876269107426_4_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.50102106363388_m12.960490752611433_m38.47530338641699_m12.935070144844953_5_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.50130467830106_m12.961824509508324_m38.47401790429914_m12.931900743216616_6_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.49922134252434_m12.959719860966981_m38.47230805005746_m12.932265326057136_7_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.499023327452186_m12.96043952416794_m38.47288011285585_m12.935194971832598_8_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.50157434253033_m12.960963430607745_m38.47367938539426_m12.934943284635198_9_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.50173708534096_m12.961142864695704_m38.472735872376994_m12.934002867600155_10_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.501770300615625_m12.962923879056133_m38.47456776187294_m12.933458582758297_11_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.500350682125635_m12.962082099834404_m38.474252489838484_m12.933159784666088_12_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.499541957062846_m12.961275066314741_m38.47543065870227_m12.933077757489697_13_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.50096584572687_m12.960054889071188_m38.47537633515103_m12.93494576442133_14_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.49992604759511_m12.96137329471482_m38.474439318456355_m12.934385438592946_15_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.501118552381065_m12.96079542837906_m38.47527163205215_m12.934807266431482_16_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.5002628268697_m12.96291845683024_m38.474969528890774_m12.935323121601408_17_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.50148403583942_m12.959860721735883_m38.473738459371354_m12.932454395581454_18_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.50449792282273_m12.960749843857812_m38.47312892278054_m12.934855166198494_19_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.501890924160584_m12.961519343957082_m38.474698888311465_m12.933784238917099_20_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.5007597052321_m12.959937832694857_m38.4746987632653_m12.934062022103753_21_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.50140543268961_m12.962059262780658_m38.47465373021255_m12.933888947418161_22_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.502953641658266_m12.963948797656334_m38.473898022861405_m12.935715998602321_23_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.50187151458964_m12.960561184183135_m38.47481398113283_m12.934620537016835_24_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.501402782516365_m12.96039753671852_m38.47361068224981_m12.93529938288262_25_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.49976769604373_m12.961496062259055_m38.474156963136124_m12.934301693944008_26_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.500486678608006_m12.959835378598493_m38.474758327361364_m12.936386705101464_27_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.50066682622218_m12.960812050907476_m38.47216531424985_m12.934908879722355_28_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.50234447884447_m12.962113594988761_m38.47520010149299_m12.935206277553998_29_15_weight_heuristic_SPFA_nearest_neighbor',
    '../data/results/m38.501602450236554_m12.962836591132051_m38.47539177946605_m12.934754563384551_30_15_weight_heuristic_SPFA_nearest_neighbor'
    ]

files_i_b = [
    '../data/results/m38.49905230272549_m12.960541036813272_m38.47398437502447_m12.935229804750517_0_15_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.499613596916454_m12.961216812913838_m38.47548425277925_m12.934070088770925_1_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50194412971296_m12.9624676749896_m38.472997875909336_m12.93487294586209_2_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.498581450235484_m12.9619559499298_m38.475389747728904_m12.934784985867735_3_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.49996781691653_m12.95986050660711_m38.474784788561664_m12.933876269107426_4_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50102106363388_m12.960490752611433_m38.47530338641699_m12.935070144844953_5_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50130467830106_m12.961824509508324_m38.47401790429914_m12.931900743216616_6_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.49922134252434_m12.959719860966981_m38.47230805005746_m12.932265326057136_7_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.499023327452186_m12.96043952416794_m38.47288011285585_m12.935194971832598_8_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50157434253033_m12.960963430607745_m38.47367938539426_m12.934943284635198_9_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50173708534096_m12.961142864695704_m38.472735872376994_m12.934002867600155_10_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.501770300615625_m12.962923879056133_m38.47456776187294_m12.933458582758297_11_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.500350682125635_m12.962082099834404_m38.474252489838484_m12.933159784666088_12_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.499541957062846_m12.961275066314741_m38.47543065870227_m12.933077757489697_13_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50096584572687_m12.960054889071188_m38.47537633515103_m12.93494576442133_14_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.49992604759511_m12.96137329471482_m38.474439318456355_m12.934385438592946_15_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.501118552381065_m12.96079542837906_m38.47527163205215_m12.934807266431482_16_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.5002628268697_m12.96291845683024_m38.474969528890774_m12.935323121601408_17_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50148403583942_m12.959860721735883_m38.473738459371354_m12.932454395581454_18_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50449792282273_m12.960749843857812_m38.47312892278054_m12.934855166198494_19_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.501890924160584_m12.961519343957082_m38.474698888311465_m12.933784238917099_20_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.5007597052321_m12.959937832694857_m38.4746987632653_m12.934062022103753_21_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50140543268961_m12.962059262780658_m38.47465373021255_m12.933888947418161_22_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.502953641658266_m12.963948797656334_m38.473898022861405_m12.935715998602321_23_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50187151458964_m12.960561184183135_m38.47481398113283_m12.934620537016835_24_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.501402782516365_m12.96039753671852_m38.47361068224981_m12.93529938288262_25_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.49976769604373_m12.961496062259055_m38.474156963136124_m12.934301693944008_26_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.500486678608006_m12.959835378598493_m38.474758327361364_m12.936386705101464_27_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50066682622218_m12.960812050907476_m38.47216531424985_m12.934908879722355_28_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50234447884447_m12.962113594988761_m38.47520010149299_m12.935206277553998_29_15_weight_heuristic_SPFA_closest_insertion',
    '../data/results/m38.501602450236554_m12.962836591132051_m38.47539177946605_m12.934754563384551_30_15_weight_heuristic_SPFA_closest_insertion'
]

files_d_b = [
    '../data/results/m38.49905230272549_m12.960541036813272_m38.47398437502447_m12.935229804750517_0_15_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.499613596916454_m12.961216812913838_m38.47548425277925_m12.934070088770925_1_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50194412971296_m12.9624676749896_m38.472997875909336_m12.93487294586209_2_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.498581450235484_m12.9619559499298_m38.475389747728904_m12.934784985867735_3_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.49996781691653_m12.95986050660711_m38.474784788561664_m12.933876269107426_4_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50102106363388_m12.960490752611433_m38.47530338641699_m12.935070144844953_5_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50130467830106_m12.961824509508324_m38.47401790429914_m12.931900743216616_6_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.49922134252434_m12.959719860966981_m38.47230805005746_m12.932265326057136_7_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.499023327452186_m12.96043952416794_m38.47288011285585_m12.935194971832598_8_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50157434253033_m12.960963430607745_m38.47367938539426_m12.934943284635198_9_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50173708534096_m12.961142864695704_m38.472735872376994_m12.934002867600155_10_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.501770300615625_m12.962923879056133_m38.47456776187294_m12.933458582758297_11_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.500350682125635_m12.962082099834404_m38.474252489838484_m12.933159784666088_12_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.499541957062846_m12.961275066314741_m38.47543065870227_m12.933077757489697_13_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50096584572687_m12.960054889071188_m38.47537633515103_m12.93494576442133_14_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.49992604759511_m12.96137329471482_m38.474439318456355_m12.934385438592946_15_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.501118552381065_m12.96079542837906_m38.47527163205215_m12.934807266431482_16_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.5002628268697_m12.96291845683024_m38.474969528890774_m12.935323121601408_17_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50148403583942_m12.959860721735883_m38.473738459371354_m12.932454395581454_18_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50449792282273_m12.960749843857812_m38.47312892278054_m12.934855166198494_19_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.501890924160584_m12.961519343957082_m38.474698888311465_m12.933784238917099_20_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.5007597052321_m12.959937832694857_m38.4746987632653_m12.934062022103753_21_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50140543268961_m12.962059262780658_m38.47465373021255_m12.933888947418161_22_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.502953641658266_m12.963948797656334_m38.473898022861405_m12.935715998602321_23_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50187151458964_m12.960561184183135_m38.47481398113283_m12.934620537016835_24_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.501402782516365_m12.96039753671852_m38.47361068224981_m12.93529938288262_25_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.49976769604373_m12.961496062259055_m38.474156963136124_m12.934301693944008_26_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.500486678608006_m12.959835378598493_m38.474758327361364_m12.936386705101464_27_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50066682622218_m12.960812050907476_m38.47216531424985_m12.934908879722355_28_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50234447884447_m12.962113594988761_m38.47520010149299_m12.935206277553998_29_15_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.501602450236554_m12.962836591132051_m38.47539177946605_m12.934754563384551_30_15_weight_heuristic_SPFA_further_insertion'
]

power_t = []
power_i = []
power_d = []

power_t_b = []
power_i_b = []
power_d_b = []

for a in range(len(files)):

    dados_t = dict(open_file(files[a]))
    dados_i = dict(open_file(files_i[a]))
    dados_d = dict(open_file(files_d[a]))

    dados_t_b = dict(open_file(files_b[a]))
    dados_i_b = dict(open_file(files_i_b[a]))
    dados_d_b = dict(open_file(files_d_b[a]))

    for i in list(dados_t.keys()):
        power_t.append(dados_t.get(str(i)))
    for i in list(dados_i.keys()):
        power_i.append(dados_i.get(str(i)))
    for i in list(dados_d.keys()):
        power_d.append(dados_d.get(str(i)))

    for i in list(dados_t_b.keys()):
        power_t_b.append(dados_t_b.get(str(i)))
    for i in list(dados_i_b.keys()):
        power_i_b.append(dados_i_b.get(str(i)))
    for i in list(dados_d_b.keys()):
        power_d_b.append(dados_d_b.get(str(i)))

pdf_power_t = [0] * (int(max(power_t)) + 10)
cdf_t = [0] * (int(max(power_t)) + 10)

for i in power_t:
    num = Decimal(float(i)).quantize(0, ROUND_HALF_UP)
    pdf_power_t[int(num)] += 1

x1 = []
cumulative_t = 0

for i in range(len(pdf_power_t)):
    cumulative_t += (pdf_power_t[i] / len(power_t)) * 100
    #print("NN sdp", i, cumulative_t)
    x1.append(i)
    cdf_t[i] = cumulative_t

#######
pdf_power_i = [0] * (int(max(power_i)) + 10)
cdf_i = [0] * (int(max(power_i)) + 10)

for i in power_i:
    num = Decimal(float(i)).quantize(0, ROUND_HALF_UP)
    pdf_power_i[int(num)] += 1

x2 = []
cumulative_i = 0

for i in range(len(pdf_power_i)):
    cumulative_i += (pdf_power_i[i] / len(power_i)) * 100
    #print("NI sdp", i, cumulative_i)
    cdf_i[i] = cumulative_i
    x2.append(i)

#######
pdf_power_d = [0] * (int(max(power_d)) + 10)
cdf_d = [0] * (int(max(power_d)) + 10)

for i in power_d:
    num = Decimal(float(i)).quantize(0, ROUND_HALF_UP)
    pdf_power_d[int(num)] += 1

x3 = []
cumulative_d = 0

for i in range(len(pdf_power_d)):
    cumulative_d += (pdf_power_d[i] / len(power_d)) * 100
    #print("FI", i, cumulative_d)
    cdf_d[i] = cumulative_d
    x3.append(i)

######################################

pdf_power_t_b = [0] * (int(max(power_t_b)) + 10)
cdf_t_b = [0] * (int(max(power_t_b)) + 10)

for i in power_t_b:
    num = Decimal(float(i)).quantize(0, ROUND_HALF_UP)
    pdf_power_t_b[int(num)] += 1

x1_b = []
cumulative_t_b = 0

for i in range(len(pdf_power_t_b)):
    cumulative_t_b += (pdf_power_t_b[i] / len(power_t_b)) * 100
    x1_b.append(i)
    #print("NN LWP", i, cumulative_t_b)
    cdf_t_b[i] = cumulative_t_b

#######
pdf_power_i_b = [0] * (int(max(power_i_b)) + 10)
cdf_i_b = [0] * (int(max(power_i_b)) + 10)

for i in power_i_b:
    num = Decimal(float(i)).quantize(0, ROUND_HALF_UP)
    pdf_power_i_b[int(num)] += 1

x2_b = []
cumulative_i_b = 0

for i in range(len(pdf_power_i_b)):
    cumulative_i_b += (pdf_power_i_b[i] / len(power_i_b)) * 100
    cdf_i_b[i] = cumulative_i_b
    #print("NI LWP", i, cumulative_i_b)
    x2_b.append(i)

#######
pdf_power_d_b = [0] * (int(max(power_d_b)) + 10)
cdf_d_b = [0] * (int(max(power_d_b)) + 10)

for i in power_d_b:
    num = Decimal(float(i)).quantize(0, ROUND_HALF_UP)
    pdf_power_d_b[int(num)] += 1

x3_b = []
cumulative_d_b = 0

for i in range(len(pdf_power_d_b)):
    cumulative_d_b += (pdf_power_d_b[i] / len(power_d_b)) * 100
    cdf_d_b[i] = cumulative_d_b
    print("FI LWP", i, cumulative_d_b)
    x3_b.append(i)

######################################

fig = plt.figure()
plt.xlim(-7, 140)
plt.xticks(size=13)
plt.yticks(size=13)
plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)

plt.errorbar(x1, cdf_t, label='Nearest Neighbor SDP', color='tab:orange', ls="-", linewidth=1.1)
plt.errorbar(x2, cdf_i, label='Nearest Insertion SDP', color='tab:blue', ls="-", linewidth=1.1)
plt.errorbar(x3, cdf_d, label='Farthest Insertion SDP', color='tab:green', ls="-", linewidth=1.1)  # marker='P'
plt.errorbar(x1_b, cdf_t_b, label='Nearest Neighbor LWP', color='tab:pink', ls="-", linewidth=1.1)
plt.errorbar(x2_b, cdf_i_b, label='Nearest Insertion LWP', color='tab:red', ls="-", linewidth=1.1)
plt.errorbar(x3_b, cdf_d_b, label='Farthest Insertion LWP', color='k', ls="-", linewidth=1.1)

ylabel = 'Empirical Cumulative Distribution Function [%]'
xlabel = 'Instant Power [W]'

plt.ylabel(ylabel, fontweight="bold", fontsize=11)
plt.xlabel(xlabel, fontweight="bold", fontsize=11)

plt.legend(numpoints=1, loc="lower right", ncol=1, prop={'size': 10})
plt.show()

###########################################
"""
fig = plt.figure()
plt.xlim(-3, 140)
plt.xticks(size=13)
plt.yticks(size=13)

plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)

plt.errorbar(x1_b, cdf_t_b, label='PMT', color='tab:orange', ls="-", linewidth=1.1)
plt.errorbar(x2_b, cdf_i_b, label='PMI', color='tab:blue', ls="-", linewidth=1.1)
plt.errorbar(x3_b, cdf_d_b, label='PMD', color='tab:green', ls="-", linewidth=1.1)  # marker='P'

ylabel = 'Função de Distribuição Acumulada Empírica (%)'
xlabel = 'Potência instantânea (W)'

plt.ylabel(ylabel, fontweight="bold", fontsize=10.5)
plt.xlabel(xlabel, fontweight="bold", fontsize=10.5)

plt.legend(numpoints=1, loc="lower right", ncol=1, prop={'size': 11})
plt.show()

"""