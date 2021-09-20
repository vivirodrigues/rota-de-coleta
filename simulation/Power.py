import json
import scipy.stats
import matplotlib.pyplot as plt
import scipy.stats as st
from decimal import Decimal, ROUND_HALF_UP
from xml.dom import minidom
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


#files_i_b = ['../../data/results/m43.96267779776494_m19.944747838679202_m43.929659815391865_m19.905049264605925_0_weight_heuristic_SPFA_ci_weight']
#files_d_b = ['../../data/results/m43.96267779776494_m19.944747838679202_m43.929659815391865_m19.905049264605925_0_weight_heuristic_SPFA_fi_weight']

todas_medias_t = []
todas_medias_i = []
todas_medias_d = []

todas_medias_t_b = []
todas_medias_i_b = []
todas_medias_d_b = []

for a in range(len(files)):

    media_power_t = 0
    media_power_i = 0
    media_power_d = 0

    media_power_t_b = 0
    media_power_i_b = 0
    media_power_d_b = 0

    dados_t = dict(open_file(files[a]))
    dados_i = dict(open_file(files_i[a]))
    dados_d = dict(open_file(files_d[a]))

    dados_t_b = dict(open_file(files_b[a]))
    dados_i_b = dict(open_file(files_i_b[a]))
    dados_d_b = dict(open_file(files_d_b[a]))

    for i in list(dados_t.keys()):
        media_power_t += int(dados_t.get(str(i)))
    for i in list(dados_i.keys()):
        media_power_i += int(dados_i.get(str(i)))
    for i in list(dados_d.keys()):
        media_power_d += int(dados_d.get(str(i)))

    for i in list(dados_t_b.keys()):
        media_power_t_b += int(dados_t_b.get(str(i)))
    for i in list(dados_i_b.keys()):
        media_power_i_b += int(dados_i_b.get(str(i)))
    for i in list(dados_d_b.keys()):
        media_power_d_b += int(dados_d_b.get(str(i)))

    media_power_t = media_power_t / len(list(dados_t.keys()))
    media_power_i = media_power_i / len(list(dados_i.keys()))
    media_power_d = media_power_d / len(list(dados_d.keys()))

    media_power_t_b = media_power_t_b / len(list(dados_t_b.keys()))
    media_power_i_b = media_power_i_b / len(list(dados_i_b.keys()))
    media_power_d_b = media_power_d_b / len(list(dados_d_b.keys()))

    todas_medias_t.append(media_power_t)
    todas_medias_i.append(media_power_i)
    todas_medias_d.append(media_power_d)

    todas_medias_t_b.append(media_power_t_b)
    todas_medias_i_b.append(media_power_i_b)
    todas_medias_d_b.append(media_power_d_b)

m, h = mean_confidence_interval(todas_medias_t, 0.95)
m1, h1 = mean_confidence_interval(todas_medias_i, 0.95)
m2, h2 = mean_confidence_interval(todas_medias_d, 0.95)

print("media BH", m, m1, m2)

m_b, h_b = mean_confidence_interval(todas_medias_t_b, 0.95)
m1_b, h1_b = mean_confidence_interval(todas_medias_i_b, 0.95)
m2_b, h2_b = mean_confidence_interval(todas_medias_d_b, 0.95)

medias = [m, m1, m2]
erros = [h, h1, h2]

medias_b = [m_b, m1_b, m2_b]
erros_b = [h_b, h1_b, h2_b]

print("medias, SDP", medias)
print('Nearest Neighbor', 'Nearest Insertion', 'Farthest Insertion')
print("medias, LWP", medias_b)
print("erros, SDP", erros)
print("erros, LWP", erros_b)

print(erros, erros_b)

# define sample ../data
# ../data = values  # [12, 12, 13, 13, 15, 16, 17, 22, 23, 25, 26, 27, 28, 28, 29]

# create 95% confidence interval for population mean weight
# print(st.t.interval(alpha=0.95, df=len(../data) - 1, loc=np.mean(../data), scale=st.sem(../data)))

labels = ['Nearest Neighbor', 'Closest Insertion', 'Further Insertion']

x = np.arange(len(labels))  # the label locations
width = 0.25  # 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, medias, width, yerr=erros, label='SDP', zorder=10)
r2 = ax.bar(x + width/2, medias_b, width, yerr=erros_b, label='LWP', zorder=10)

# Add some text for labels, title and custom x-axis tick labels, etc.
#ax.set_ylabel('Potência média (W)', fontdict='bold')
plt.ylabel('Power [W]', fontweight="bold", fontsize=11)
plt.ylim(0, max(medias_b) + 18)
plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(numpoints=1, loc="upper left", ncol=2, prop={'size': 10})

fig.tight_layout()

plt.show()