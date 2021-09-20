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
         '../data/results/m38.49999603681327_m12.962358080558504_m38.47398437502447_m12.932893255527242_0_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.500671812913836_m12.96339552158351_m38.47352508877093_m12.932765988234031_1_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50194412971296_m12.961982380453897_m38.472997875909336_m12.933973466644028_2_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.5014109499298_m12.960872502034725_m38.47423998586774_m12.935033565792027_3_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50102106363388_m12.962638092503209_m38.474525144844954_m12.932374557163948_4_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.49922134252434_m12.962995897766534_m38.47172032605714_m12.933032796134958_5_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.49989452416794_m12.961981434109553_m38.47288011285585_m12.932171368514155_6_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50237887905613_m12.960648819826947_m38.472913582758295_m12.934273386456828_7_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.5015370998344_m12.962186005531471_m38.47261478466609_m12.934002015361491_8_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50073006631474_m12.961333960783888_m38.4725327574897_m12.932373724953635_9_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50096584572687_m12.96121100042776_m38.47440076442133_m12.934017719276726_10_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50082829471482_m12.960720017172312_m38.47384043859295_m12.933596799909374_11_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.501118552381065_m12.962947784137462_m38.47426226643149_m12.932564078786635_12_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.502373456830234_m12.962333491657414_m38.47477812160141_m12.93271906374045_13_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50148403583942_m12.965290796965846_m38.471909395581456_m12.932729360653218_14_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.501890924160584_m12.961062102765782_m38.4732392389171_m12.933884816602236_15_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.5007597052321_m12.961099590741043_m38.473517022103756_m12.933269493665131_16_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50151426278066_m12.96224952417061_m38.473343947418165_m12.932595128870267_17_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50340379765633_m12.963068504924866_m38.473898022861405_m12.932939179700924_18_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.501402782516365_m12.962743981859667_m38.47361068224981_m12.929892203606808_19_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.500951062259055_m12.964628446152132_m38.47375669394401_m12.93455351878407_20_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.500486678608006_m12.963212145332431_m38.474758327361364_m12.933328833777356_21_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50234447884447_m12.961648999633914_m38.474661277554_m12.93489642987398_22_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50229159113205_m12.961490473565357_m38.474209563384555_m12.933428060221484_23_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.500568338650666_m12.963562146885746_m38.47357849097421_m12.93225101151055_24_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50115701483925_m12.9612635544437_m38.47509217365817_m12.933188948092502_25_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50186554346796_m12.961718758432754_m38.47355380440904_m12.934289622568668_26_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50165434807298_m12.96187628063375_m38.47332172286755_m12.933277161490693_27_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50177737556065_m12.962596650290932_m38.472904517360526_m12.933331456516722_28_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50009702898103_m12.96036292373261_m38.47412281703678_m12.934711892250165_29_30_length_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.500734794836475_m12.961295117029927_m38.473498428492356_m12.932937589096973_30_30_length_heuristic_SPFA_nearest_neighbor.xml'
         ]

files_i = [
            #'../../data/results/m43.96267779776494_m19.944747838679202_m43.929659815391865_m19.905049264605925_0_distance_heuristic_SPFA_ci_distance',
           '../data/results/m38.49999603681327_m12.962358080558504_m38.47398437502447_m12.932893255527242_0_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.500671812913836_m12.96339552158351_m38.47352508877093_m12.932765988234031_1_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.50194412971296_m12.961982380453897_m38.472997875909336_m12.933973466644028_2_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.5014109499298_m12.960872502034725_m38.47423998586774_m12.935033565792027_3_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.50102106363388_m12.962638092503209_m38.474525144844954_m12.932374557163948_4_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.49922134252434_m12.962995897766534_m38.47172032605714_m12.933032796134958_5_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.49989452416794_m12.961981434109553_m38.47288011285585_m12.932171368514155_6_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.50237887905613_m12.960648819826947_m38.472913582758295_m12.934273386456828_7_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.5015370998344_m12.962186005531471_m38.47261478466609_m12.934002015361491_8_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.50073006631474_m12.961333960783888_m38.4725327574897_m12.932373724953635_9_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.50096584572687_m12.96121100042776_m38.47440076442133_m12.934017719276726_10_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.50082829471482_m12.960720017172312_m38.47384043859295_m12.933596799909374_11_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.501118552381065_m12.962947784137462_m38.47426226643149_m12.932564078786635_12_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.502373456830234_m12.962333491657414_m38.47477812160141_m12.93271906374045_13_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.50148403583942_m12.965290796965846_m38.471909395581456_m12.932729360653218_14_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.501890924160584_m12.961062102765782_m38.4732392389171_m12.933884816602236_15_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.5007597052321_m12.961099590741043_m38.473517022103756_m12.933269493665131_16_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.50151426278066_m12.96224952417061_m38.473343947418165_m12.932595128870267_17_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.50340379765633_m12.963068504924866_m38.473898022861405_m12.932939179700924_18_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.501402782516365_m12.962743981859667_m38.47361068224981_m12.929892203606808_19_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.500951062259055_m12.964628446152132_m38.47375669394401_m12.93455351878407_20_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.500486678608006_m12.963212145332431_m38.474758327361364_m12.933328833777356_21_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.50234447884447_m12.961648999633914_m38.474661277554_m12.93489642987398_22_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.50229159113205_m12.961490473565357_m38.474209563384555_m12.933428060221484_23_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.500568338650666_m12.963562146885746_m38.47357849097421_m12.93225101151055_24_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.50115701483925_m12.9612635544437_m38.47509217365817_m12.933188948092502_25_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.50186554346796_m12.961718758432754_m38.47355380440904_m12.934289622568668_26_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.50165434807298_m12.96187628063375_m38.47332172286755_m12.933277161490693_27_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.50177737556065_m12.962596650290932_m38.472904517360526_m12.933331456516722_28_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.50009702898103_m12.96036292373261_m38.47412281703678_m12.934711892250165_29_30_length_heuristic_SPFA_closest_insertion.xml',
            '../data/results/m38.500734794836475_m12.961295117029927_m38.473498428492356_m12.932937589096973_30_30_length_heuristic_SPFA_closest_insertion.xml'
           ]

files_d = [#'../../data/results/m43.96267779776494_m19.944747838679202_m43.929659815391865_m19.905049264605925_0_distance_heuristic_SPFA_fi_distance'
            '../data/results/m38.49999603681327_m12.962358080558504_m38.47398437502447_m12.932893255527242_0_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.500671812913836_m12.96339552158351_m38.47352508877093_m12.932765988234031_1_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.50194412971296_m12.961982380453897_m38.472997875909336_m12.933973466644028_2_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.5014109499298_m12.960872502034725_m38.47423998586774_m12.935033565792027_3_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.50102106363388_m12.962638092503209_m38.474525144844954_m12.932374557163948_4_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.49922134252434_m12.962995897766534_m38.47172032605714_m12.933032796134958_5_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.49989452416794_m12.961981434109553_m38.47288011285585_m12.932171368514155_6_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.50237887905613_m12.960648819826947_m38.472913582758295_m12.934273386456828_7_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.5015370998344_m12.962186005531471_m38.47261478466609_m12.934002015361491_8_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.50073006631474_m12.961333960783888_m38.4725327574897_m12.932373724953635_9_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.50096584572687_m12.96121100042776_m38.47440076442133_m12.934017719276726_10_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.50082829471482_m12.960720017172312_m38.47384043859295_m12.933596799909374_11_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.501118552381065_m12.962947784137462_m38.47426226643149_m12.932564078786635_12_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.502373456830234_m12.962333491657414_m38.47477812160141_m12.93271906374045_13_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.50148403583942_m12.965290796965846_m38.471909395581456_m12.932729360653218_14_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.501890924160584_m12.961062102765782_m38.4732392389171_m12.933884816602236_15_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.5007597052321_m12.961099590741043_m38.473517022103756_m12.933269493665131_16_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.50151426278066_m12.96224952417061_m38.473343947418165_m12.932595128870267_17_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.50340379765633_m12.963068504924866_m38.473898022861405_m12.932939179700924_18_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.501402782516365_m12.962743981859667_m38.47361068224981_m12.929892203606808_19_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.500951062259055_m12.964628446152132_m38.47375669394401_m12.93455351878407_20_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.500486678608006_m12.963212145332431_m38.474758327361364_m12.933328833777356_21_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.50234447884447_m12.961648999633914_m38.474661277554_m12.93489642987398_22_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.50229159113205_m12.961490473565357_m38.474209563384555_m12.933428060221484_23_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.500568338650666_m12.963562146885746_m38.47357849097421_m12.93225101151055_24_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.50115701483925_m12.9612635544437_m38.47509217365817_m12.933188948092502_25_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.50186554346796_m12.961718758432754_m38.47355380440904_m12.934289622568668_26_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.50165434807298_m12.96187628063375_m38.47332172286755_m12.933277161490693_27_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.50177737556065_m12.962596650290932_m38.472904517360526_m12.933331456516722_28_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.50009702898103_m12.96036292373261_m38.47412281703678_m12.934711892250165_29_30_length_heuristic_SPFA_further_insertion.xml',
            '../data/results/m38.500734794836475_m12.961295117029927_m38.473498428492356_m12.932937589096973_30_30_length_heuristic_SPFA_further_insertion.xml'
        ]

files_b = [#'../../data/results/m43.957018117658315_m19.931545102455843_m43.931890481507786_m19.907162672548026_0_distance_heuristic_SPFA_nn'
        '../data/results/m38.49999603681327_m12.962358080558504_m38.47398437502447_m12.932893255527242_0_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.500671812913836_m12.96339552158351_m38.47352508877093_m12.932765988234031_1_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50194412971296_m12.961982380453897_m38.472997875909336_m12.933973466644028_2_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.5014109499298_m12.960872502034725_m38.47423998586774_m12.935033565792027_3_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50102106363388_m12.962638092503209_m38.474525144844954_m12.932374557163948_4_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.49922134252434_m12.962995897766534_m38.47172032605714_m12.933032796134958_5_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.49989452416794_m12.961981434109553_m38.47288011285585_m12.932171368514155_6_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50237887905613_m12.960648819826947_m38.472913582758295_m12.934273386456828_7_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.5015370998344_m12.962186005531471_m38.47261478466609_m12.934002015361491_8_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50073006631474_m12.961333960783888_m38.4725327574897_m12.932373724953635_9_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50096584572687_m12.96121100042776_m38.47440076442133_m12.934017719276726_10_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50082829471482_m12.960720017172312_m38.47384043859295_m12.933596799909374_11_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.501118552381065_m12.962947784137462_m38.47426226643149_m12.932564078786635_12_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.502373456830234_m12.962333491657414_m38.47477812160141_m12.93271906374045_13_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50148403583942_m12.965290796965846_m38.471909395581456_m12.932729360653218_14_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.501890924160584_m12.961062102765782_m38.4732392389171_m12.933884816602236_15_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.5007597052321_m12.961099590741043_m38.473517022103756_m12.933269493665131_16_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50151426278066_m12.96224952417061_m38.473343947418165_m12.932595128870267_17_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50340379765633_m12.963068504924866_m38.473898022861405_m12.932939179700924_18_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.501402782516365_m12.962743981859667_m38.47361068224981_m12.929892203606808_19_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.500951062259055_m12.964628446152132_m38.47375669394401_m12.93455351878407_20_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.500486678608006_m12.963212145332431_m38.474758327361364_m12.933328833777356_21_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50234447884447_m12.961648999633914_m38.474661277554_m12.93489642987398_22_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50229159113205_m12.961490473565357_m38.474209563384555_m12.933428060221484_23_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.500568338650666_m12.963562146885746_m38.47357849097421_m12.93225101151055_24_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50115701483925_m12.9612635544437_m38.47509217365817_m12.933188948092502_25_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50186554346796_m12.961718758432754_m38.47355380440904_m12.934289622568668_26_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50165434807298_m12.96187628063375_m38.47332172286755_m12.933277161490693_27_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50177737556065_m12.962596650290932_m38.472904517360526_m12.933331456516722_28_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.50009702898103_m12.96036292373261_m38.47412281703678_m12.934711892250165_29_30_weight_heuristic_SPFA_nearest_neighbor.xml',
        '../data/results/m38.500734794836475_m12.961295117029927_m38.473498428492356_m12.932937589096973_30_30_weight_heuristic_SPFA_nearest_neighbor.xml'
        ]

files_i_b = [#'../../data/results/m43.957018117658315_m19.931545102455843_m43.931890481507786_m19.907162672548026_0_distance_heuristic_SPFA_nn'
        '../data/results/m38.49999603681327_m12.962358080558504_m38.47398437502447_m12.932893255527242_0_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.500671812913836_m12.96339552158351_m38.47352508877093_m12.932765988234031_1_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.50194412971296_m12.961982380453897_m38.472997875909336_m12.933973466644028_2_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.5014109499298_m12.960872502034725_m38.47423998586774_m12.935033565792027_3_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.50102106363388_m12.962638092503209_m38.474525144844954_m12.932374557163948_4_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.49922134252434_m12.962995897766534_m38.47172032605714_m12.933032796134958_5_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.49989452416794_m12.961981434109553_m38.47288011285585_m12.932171368514155_6_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.50237887905613_m12.960648819826947_m38.472913582758295_m12.934273386456828_7_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.5015370998344_m12.962186005531471_m38.47261478466609_m12.934002015361491_8_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.50073006631474_m12.961333960783888_m38.4725327574897_m12.932373724953635_9_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.50096584572687_m12.96121100042776_m38.47440076442133_m12.934017719276726_10_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.50082829471482_m12.960720017172312_m38.47384043859295_m12.933596799909374_11_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.501118552381065_m12.962947784137462_m38.47426226643149_m12.932564078786635_12_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.502373456830234_m12.962333491657414_m38.47477812160141_m12.93271906374045_13_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.50148403583942_m12.965290796965846_m38.471909395581456_m12.932729360653218_14_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.501890924160584_m12.961062102765782_m38.4732392389171_m12.933884816602236_15_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.5007597052321_m12.961099590741043_m38.473517022103756_m12.933269493665131_16_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.50151426278066_m12.96224952417061_m38.473343947418165_m12.932595128870267_17_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.50340379765633_m12.963068504924866_m38.473898022861405_m12.932939179700924_18_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.501402782516365_m12.962743981859667_m38.47361068224981_m12.929892203606808_19_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.500951062259055_m12.964628446152132_m38.47375669394401_m12.93455351878407_20_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.500486678608006_m12.963212145332431_m38.474758327361364_m12.933328833777356_21_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.50234447884447_m12.961648999633914_m38.474661277554_m12.93489642987398_22_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.50229159113205_m12.961490473565357_m38.474209563384555_m12.933428060221484_23_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.500568338650666_m12.963562146885746_m38.47357849097421_m12.93225101151055_24_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.50115701483925_m12.9612635544437_m38.47509217365817_m12.933188948092502_25_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.50186554346796_m12.961718758432754_m38.47355380440904_m12.934289622568668_26_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.50165434807298_m12.96187628063375_m38.47332172286755_m12.933277161490693_27_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.50177737556065_m12.962596650290932_m38.472904517360526_m12.933331456516722_28_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.50009702898103_m12.96036292373261_m38.47412281703678_m12.934711892250165_29_30_weight_heuristic_SPFA_closest_insertion.xml',
        '../data/results/m38.500734794836475_m12.961295117029927_m38.473498428492356_m12.932937589096973_30_30_weight_heuristic_SPFA_closest_insertion.xml'
        ]

files_d_b = [#'../../data/results/m43.957018117658315_m19.931545102455843_m43.931890481507786_m19.907162672548026_0_distance_heuristic_SPFA_nn'
        '../data/results/m38.49999603681327_m12.962358080558504_m38.47398437502447_m12.932893255527242_0_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.500671812913836_m12.96339552158351_m38.47352508877093_m12.932765988234031_1_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.50194412971296_m12.961982380453897_m38.472997875909336_m12.933973466644028_2_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.5014109499298_m12.960872502034725_m38.47423998586774_m12.935033565792027_3_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.50102106363388_m12.962638092503209_m38.474525144844954_m12.932374557163948_4_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.49922134252434_m12.962995897766534_m38.47172032605714_m12.933032796134958_5_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.49989452416794_m12.961981434109553_m38.47288011285585_m12.932171368514155_6_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.50237887905613_m12.960648819826947_m38.472913582758295_m12.934273386456828_7_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.5015370998344_m12.962186005531471_m38.47261478466609_m12.934002015361491_8_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.50073006631474_m12.961333960783888_m38.4725327574897_m12.932373724953635_9_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.50096584572687_m12.96121100042776_m38.47440076442133_m12.934017719276726_10_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.50082829471482_m12.960720017172312_m38.47384043859295_m12.933596799909374_11_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.501118552381065_m12.962947784137462_m38.47426226643149_m12.932564078786635_12_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.502373456830234_m12.962333491657414_m38.47477812160141_m12.93271906374045_13_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.50148403583942_m12.965290796965846_m38.471909395581456_m12.932729360653218_14_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.501890924160584_m12.961062102765782_m38.4732392389171_m12.933884816602236_15_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.5007597052321_m12.961099590741043_m38.473517022103756_m12.933269493665131_16_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.50151426278066_m12.96224952417061_m38.473343947418165_m12.932595128870267_17_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.50340379765633_m12.963068504924866_m38.473898022861405_m12.932939179700924_18_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.501402782516365_m12.962743981859667_m38.47361068224981_m12.929892203606808_19_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.500951062259055_m12.964628446152132_m38.47375669394401_m12.93455351878407_20_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.500486678608006_m12.963212145332431_m38.474758327361364_m12.933328833777356_21_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.50234447884447_m12.961648999633914_m38.474661277554_m12.93489642987398_22_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.50229159113205_m12.961490473565357_m38.474209563384555_m12.933428060221484_23_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.500568338650666_m12.963562146885746_m38.47357849097421_m12.93225101151055_24_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.50115701483925_m12.9612635544437_m38.47509217365817_m12.933188948092502_25_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.50186554346796_m12.961718758432754_m38.47355380440904_m12.934289622568668_26_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.50165434807298_m12.96187628063375_m38.47332172286755_m12.933277161490693_27_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.50177737556065_m12.962596650290932_m38.472904517360526_m12.933331456516722_28_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.50009702898103_m12.96036292373261_m38.47412281703678_m12.934711892250165_29_30_weight_heuristic_SPFA_further_insertion.xml',
        '../data/results/m38.500734794836475_m12.961295117029927_m38.473498428492356_m12.932937589096973_30_30_weight_heuristic_SPFA_further_insertion.xml'
        ]

values_t = []
values_i = []
values_d = []

values_t_b = []
values_i_b = []
values_d_b = []

for a in range(len(files)):

    file = minidom.parse(files[a])
    tag = file.getElementsByTagName('tripinfo')
    duration = [float(node.attributes['routeLength'].value) for node in tag]
    values_t.append(duration[0] / 1000)

    file = minidom.parse(files_i[a])
    tag = file.getElementsByTagName('tripinfo')
    duration = [float(node.attributes['routeLength'].value) for node in tag]
    values_i.append(duration[0] / 1000)
    # 1, 13

    file = minidom.parse(files_d[a])
    tag = file.getElementsByTagName('tripinfo')
    duration = [float(node.attributes['routeLength'].value) for node in tag]
    values_d.append(duration[0] / 1000)

    file = minidom.parse(files_b[a])
    tag = file.getElementsByTagName('tripinfo')
    duration = [float(node.attributes['routeLength'].value) for node in tag]
    values_t_b.append(duration[0] / 1000)

    file = minidom.parse(files_i_b[a])
    tag = file.getElementsByTagName('tripinfo')
    duration = [float(node.attributes['routeLength'].value) for node in tag]
    values_i_b.append(duration[0] / 1000)

    file = minidom.parse(files_d_b[a])
    tag = file.getElementsByTagName('tripinfo')
    duration = [float(node.attributes['routeLength'].value) for node in tag]
    values_d_b.append(duration[0] / 1000)

m, h = mean_confidence_interval(values_t, 0.95)
m1, h1 = mean_confidence_interval(values_i, 0.95)
m2, h2 = mean_confidence_interval(values_d, 0.95)

m_b, h_b = mean_confidence_interval(values_t_b, 0.95)
m1_b, h1_b = mean_confidence_interval(values_i_b, 0.95)
m2_b, h2_b = mean_confidence_interval(values_d_b, 0.95)

medias = [m, m1, m2]
erros = [h, h1, h2]

medias_b = [m_b, m1_b, m2_b]
erros_b = [h_b, h1_b, h2_b]

print("medias, SDP", medias)
print('Nearest Neighbor', 'Closest Insertion', 'Further Insertion')
print("medias, LWP", medias_b)
print("erros, SDP", erros)
print("erros, LWP", erros_b)

# define sample data
# data = values  # [12, 12, 13, 13, 15, 16, 17, 22, 23, 25, 26, 27, 28, 28, 29]

# create 95% confidence interval for population mean weight
# print(st.t.interval(alpha=0.95, df=len(data) - 1, loc=np.mean(data), scale=st.sem(data)))

labels = ['Nearest Neighbor', 'Closest Insertion', 'Further Insertion']

x = np.arange(len(labels))  # the label locations
width = 0.25  # 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, medias, width, yerr=erros, label='SDP', zorder=10)
r2 = ax.bar(x + width / 2, medias_b, width, yerr=erros_b, label='LWP', zorder=10)

# Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Potência média (W)', fontdict='bold')
plt.ylabel('Time [h]', fontweight="bold", fontsize=11)
plt.ylim(0, max(medias) + 2)
plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(numpoints=1, loc="upper left", ncol=2, prop={'size': 10})

fig.tight_layout()

plt.show()
