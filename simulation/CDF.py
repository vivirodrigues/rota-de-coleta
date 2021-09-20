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
    '../data/results/m38.49999603681327_m12.962358080558504_m38.47398437502447_m12.932893255527242_0_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.500671812913836_m12.96339552158351_m38.47352508877093_m12.932765988234031_1_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50194412971296_m12.961982380453897_m38.472997875909336_m12.933973466644028_2_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.5014109499298_m12.960872502034725_m38.47423998586774_m12.935033565792027_3_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50102106363388_m12.962638092503209_m38.474525144844954_m12.932374557163948_4_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.49922134252434_m12.962995897766534_m38.47172032605714_m12.933032796134958_5_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.49989452416794_m12.961981434109553_m38.47288011285585_m12.932171368514155_6_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50237887905613_m12.960648819826947_m38.472913582758295_m12.934273386456828_7_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.5015370998344_m12.962186005531471_m38.47261478466609_m12.934002015361491_8_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50073006631474_m12.961333960783888_m38.4725327574897_m12.932373724953635_9_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50096584572687_m12.96121100042776_m38.47440076442133_m12.934017719276726_10_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50082829471482_m12.960720017172312_m38.47384043859295_m12.933596799909374_11_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.501118552381065_m12.962947784137462_m38.47426226643149_m12.932564078786635_12_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.502373456830234_m12.962333491657414_m38.47477812160141_m12.93271906374045_13_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50148403583942_m12.965290796965846_m38.471909395581456_m12.932729360653218_14_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.501890924160584_m12.961062102765782_m38.4732392389171_m12.933884816602236_15_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.5007597052321_m12.961099590741043_m38.473517022103756_m12.933269493665131_16_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50151426278066_m12.96224952417061_m38.473343947418165_m12.932595128870267_17_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50340379765633_m12.963068504924866_m38.473898022861405_m12.932939179700924_18_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.501402782516365_m12.962743981859667_m38.47361068224981_m12.929892203606808_19_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.500951062259055_m12.964628446152132_m38.47375669394401_m12.93455351878407_20_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.500486678608006_m12.963212145332431_m38.474758327361364_m12.933328833777356_21_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50234447884447_m12.961648999633914_m38.474661277554_m12.93489642987398_22_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50229159113205_m12.961490473565357_m38.474209563384555_m12.933428060221484_23_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.500568338650666_m12.963562146885746_m38.47357849097421_m12.93225101151055_24_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50115701483925_m12.9612635544437_m38.47509217365817_m12.933188948092502_25_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50186554346796_m12.961718758432754_m38.47355380440904_m12.934289622568668_26_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50165434807298_m12.96187628063375_m38.47332172286755_m12.933277161490693_27_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50177737556065_m12.962596650290932_m38.472904517360526_m12.933331456516722_28_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50009702898103_m12.96036292373261_m38.47412281703678_m12.934711892250165_29_30_length_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.500734794836475_m12.961295117029927_m38.473498428492356_m12.932937589096973_30_30_length_heuristic_SPFA_nearest_neighbor'
]

files_i = [
    '../data/results/m38.49999603681327_m12.962358080558504_m38.47398437502447_m12.932893255527242_0_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.500671812913836_m12.96339552158351_m38.47352508877093_m12.932765988234031_1_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50194412971296_m12.961982380453897_m38.472997875909336_m12.933973466644028_2_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.5014109499298_m12.960872502034725_m38.47423998586774_m12.935033565792027_3_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50102106363388_m12.962638092503209_m38.474525144844954_m12.932374557163948_4_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.49922134252434_m12.962995897766534_m38.47172032605714_m12.933032796134958_5_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.49989452416794_m12.961981434109553_m38.47288011285585_m12.932171368514155_6_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50237887905613_m12.960648819826947_m38.472913582758295_m12.934273386456828_7_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.5015370998344_m12.962186005531471_m38.47261478466609_m12.934002015361491_8_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50073006631474_m12.961333960783888_m38.4725327574897_m12.932373724953635_9_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50096584572687_m12.96121100042776_m38.47440076442133_m12.934017719276726_10_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50082829471482_m12.960720017172312_m38.47384043859295_m12.933596799909374_11_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.501118552381065_m12.962947784137462_m38.47426226643149_m12.932564078786635_12_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.502373456830234_m12.962333491657414_m38.47477812160141_m12.93271906374045_13_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50148403583942_m12.965290796965846_m38.471909395581456_m12.932729360653218_14_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.501890924160584_m12.961062102765782_m38.4732392389171_m12.933884816602236_15_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.5007597052321_m12.961099590741043_m38.473517022103756_m12.933269493665131_16_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50151426278066_m12.96224952417061_m38.473343947418165_m12.932595128870267_17_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50340379765633_m12.963068504924866_m38.473898022861405_m12.932939179700924_18_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.501402782516365_m12.962743981859667_m38.47361068224981_m12.929892203606808_19_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.500951062259055_m12.964628446152132_m38.47375669394401_m12.93455351878407_20_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.500486678608006_m12.963212145332431_m38.474758327361364_m12.933328833777356_21_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50234447884447_m12.961648999633914_m38.474661277554_m12.93489642987398_22_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50229159113205_m12.961490473565357_m38.474209563384555_m12.933428060221484_23_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.500568338650666_m12.963562146885746_m38.47357849097421_m12.93225101151055_24_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50115701483925_m12.9612635544437_m38.47509217365817_m12.933188948092502_25_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50186554346796_m12.961718758432754_m38.47355380440904_m12.934289622568668_26_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50165434807298_m12.96187628063375_m38.47332172286755_m12.933277161490693_27_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50177737556065_m12.962596650290932_m38.472904517360526_m12.933331456516722_28_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.50009702898103_m12.96036292373261_m38.47412281703678_m12.934711892250165_29_30_length_heuristic_SPFA_closest_insertion',
    '../data/results/m38.500734794836475_m12.961295117029927_m38.473498428492356_m12.932937589096973_30_30_length_heuristic_SPFA_closest_insertion'

]

files_d = [
    '../data/results/m38.49999603681327_m12.962358080558504_m38.47398437502447_m12.932893255527242_0_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.500671812913836_m12.96339552158351_m38.47352508877093_m12.932765988234031_1_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50194412971296_m12.961982380453897_m38.472997875909336_m12.933973466644028_2_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.5014109499298_m12.960872502034725_m38.47423998586774_m12.935033565792027_3_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50102106363388_m12.962638092503209_m38.474525144844954_m12.932374557163948_4_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.49922134252434_m12.962995897766534_m38.47172032605714_m12.933032796134958_5_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.49989452416794_m12.961981434109553_m38.47288011285585_m12.932171368514155_6_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50237887905613_m12.960648819826947_m38.472913582758295_m12.934273386456828_7_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.5015370998344_m12.962186005531471_m38.47261478466609_m12.934002015361491_8_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50073006631474_m12.961333960783888_m38.4725327574897_m12.932373724953635_9_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50096584572687_m12.96121100042776_m38.47440076442133_m12.934017719276726_10_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50082829471482_m12.960720017172312_m38.47384043859295_m12.933596799909374_11_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.501118552381065_m12.962947784137462_m38.47426226643149_m12.932564078786635_12_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.502373456830234_m12.962333491657414_m38.47477812160141_m12.93271906374045_13_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50148403583942_m12.965290796965846_m38.471909395581456_m12.932729360653218_14_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.501890924160584_m12.961062102765782_m38.4732392389171_m12.933884816602236_15_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.5007597052321_m12.961099590741043_m38.473517022103756_m12.933269493665131_16_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50151426278066_m12.96224952417061_m38.473343947418165_m12.932595128870267_17_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50340379765633_m12.963068504924866_m38.473898022861405_m12.932939179700924_18_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.501402782516365_m12.962743981859667_m38.47361068224981_m12.929892203606808_19_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.500951062259055_m12.964628446152132_m38.47375669394401_m12.93455351878407_20_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.500486678608006_m12.963212145332431_m38.474758327361364_m12.933328833777356_21_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50234447884447_m12.961648999633914_m38.474661277554_m12.93489642987398_22_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50229159113205_m12.961490473565357_m38.474209563384555_m12.933428060221484_23_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.500568338650666_m12.963562146885746_m38.47357849097421_m12.93225101151055_24_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50115701483925_m12.9612635544437_m38.47509217365817_m12.933188948092502_25_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50186554346796_m12.961718758432754_m38.47355380440904_m12.934289622568668_26_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50165434807298_m12.96187628063375_m38.47332172286755_m12.933277161490693_27_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50177737556065_m12.962596650290932_m38.472904517360526_m12.933331456516722_28_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.50009702898103_m12.96036292373261_m38.47412281703678_m12.934711892250165_29_30_length_heuristic_SPFA_further_insertion',
    '../data/results/m38.500734794836475_m12.961295117029927_m38.473498428492356_m12.932937589096973_30_30_length_heuristic_SPFA_further_insertion'
]


files_b = [
    '../data/results/m38.49999603681327_m12.962358080558504_m38.47398437502447_m12.932893255527242_0_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.500671812913836_m12.96339552158351_m38.47352508877093_m12.932765988234031_1_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50194412971296_m12.961982380453897_m38.472997875909336_m12.933973466644028_2_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.5014109499298_m12.960872502034725_m38.47423998586774_m12.935033565792027_3_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50102106363388_m12.962638092503209_m38.474525144844954_m12.932374557163948_4_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.49922134252434_m12.962995897766534_m38.47172032605714_m12.933032796134958_5_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.49989452416794_m12.961981434109553_m38.47288011285585_m12.932171368514155_6_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50237887905613_m12.960648819826947_m38.472913582758295_m12.934273386456828_7_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.5015370998344_m12.962186005531471_m38.47261478466609_m12.934002015361491_8_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50073006631474_m12.961333960783888_m38.4725327574897_m12.932373724953635_9_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50096584572687_m12.96121100042776_m38.47440076442133_m12.934017719276726_10_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50082829471482_m12.960720017172312_m38.47384043859295_m12.933596799909374_11_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.501118552381065_m12.962947784137462_m38.47426226643149_m12.932564078786635_12_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.502373456830234_m12.962333491657414_m38.47477812160141_m12.93271906374045_13_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50148403583942_m12.965290796965846_m38.471909395581456_m12.932729360653218_14_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.501890924160584_m12.961062102765782_m38.4732392389171_m12.933884816602236_15_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.5007597052321_m12.961099590741043_m38.473517022103756_m12.933269493665131_16_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50151426278066_m12.96224952417061_m38.473343947418165_m12.932595128870267_17_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50340379765633_m12.963068504924866_m38.473898022861405_m12.932939179700924_18_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.501402782516365_m12.962743981859667_m38.47361068224981_m12.929892203606808_19_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.500951062259055_m12.964628446152132_m38.47375669394401_m12.93455351878407_20_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.500486678608006_m12.963212145332431_m38.474758327361364_m12.933328833777356_21_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50234447884447_m12.961648999633914_m38.474661277554_m12.93489642987398_22_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50229159113205_m12.961490473565357_m38.474209563384555_m12.933428060221484_23_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.500568338650666_m12.963562146885746_m38.47357849097421_m12.93225101151055_24_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50115701483925_m12.9612635544437_m38.47509217365817_m12.933188948092502_25_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50186554346796_m12.961718758432754_m38.47355380440904_m12.934289622568668_26_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50165434807298_m12.96187628063375_m38.47332172286755_m12.933277161490693_27_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50177737556065_m12.962596650290932_m38.472904517360526_m12.933331456516722_28_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.50009702898103_m12.96036292373261_m38.47412281703678_m12.934711892250165_29_30_weight_heuristic_SPFA_nearest_neighbor',
        '../data/results/m38.500734794836475_m12.961295117029927_m38.473498428492356_m12.932937589096973_30_30_weight_heuristic_SPFA_nearest_neighbor'
    ]

files_i_b = [
    '../data/results/m38.49999603681327_m12.962358080558504_m38.47398437502447_m12.932893255527242_0_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.500671812913836_m12.96339552158351_m38.47352508877093_m12.932765988234031_1_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.50194412971296_m12.961982380453897_m38.472997875909336_m12.933973466644028_2_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.5014109499298_m12.960872502034725_m38.47423998586774_m12.935033565792027_3_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.50102106363388_m12.962638092503209_m38.474525144844954_m12.932374557163948_4_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.49922134252434_m12.962995897766534_m38.47172032605714_m12.933032796134958_5_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.49989452416794_m12.961981434109553_m38.47288011285585_m12.932171368514155_6_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.50237887905613_m12.960648819826947_m38.472913582758295_m12.934273386456828_7_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.5015370998344_m12.962186005531471_m38.47261478466609_m12.934002015361491_8_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.50073006631474_m12.961333960783888_m38.4725327574897_m12.932373724953635_9_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.50096584572687_m12.96121100042776_m38.47440076442133_m12.934017719276726_10_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.50082829471482_m12.960720017172312_m38.47384043859295_m12.933596799909374_11_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.501118552381065_m12.962947784137462_m38.47426226643149_m12.932564078786635_12_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.502373456830234_m12.962333491657414_m38.47477812160141_m12.93271906374045_13_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.50148403583942_m12.965290796965846_m38.471909395581456_m12.932729360653218_14_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.501890924160584_m12.961062102765782_m38.4732392389171_m12.933884816602236_15_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.5007597052321_m12.961099590741043_m38.473517022103756_m12.933269493665131_16_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.50151426278066_m12.96224952417061_m38.473343947418165_m12.932595128870267_17_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.50340379765633_m12.963068504924866_m38.473898022861405_m12.932939179700924_18_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.501402782516365_m12.962743981859667_m38.47361068224981_m12.929892203606808_19_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.500951062259055_m12.964628446152132_m38.47375669394401_m12.93455351878407_20_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.500486678608006_m12.963212145332431_m38.474758327361364_m12.933328833777356_21_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.50234447884447_m12.961648999633914_m38.474661277554_m12.93489642987398_22_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.50229159113205_m12.961490473565357_m38.474209563384555_m12.933428060221484_23_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.500568338650666_m12.963562146885746_m38.47357849097421_m12.93225101151055_24_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.50115701483925_m12.9612635544437_m38.47509217365817_m12.933188948092502_25_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.50186554346796_m12.961718758432754_m38.47355380440904_m12.934289622568668_26_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.50165434807298_m12.96187628063375_m38.47332172286755_m12.933277161490693_27_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.50177737556065_m12.962596650290932_m38.472904517360526_m12.933331456516722_28_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.50009702898103_m12.96036292373261_m38.47412281703678_m12.934711892250165_29_30_weight_heuristic_SPFA_closest_insertion',
        '../data/results/m38.500734794836475_m12.961295117029927_m38.473498428492356_m12.932937589096973_30_30_weight_heuristic_SPFA_closest_insertion'
]

files_d_b = [
    '../data/results/m38.49999603681327_m12.962358080558504_m38.47398437502447_m12.932893255527242_0_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.500671812913836_m12.96339552158351_m38.47352508877093_m12.932765988234031_1_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50194412971296_m12.961982380453897_m38.472997875909336_m12.933973466644028_2_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.5014109499298_m12.960872502034725_m38.47423998586774_m12.935033565792027_3_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50102106363388_m12.962638092503209_m38.474525144844954_m12.932374557163948_4_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.49922134252434_m12.962995897766534_m38.47172032605714_m12.933032796134958_5_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.49989452416794_m12.961981434109553_m38.47288011285585_m12.932171368514155_6_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50237887905613_m12.960648819826947_m38.472913582758295_m12.934273386456828_7_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.5015370998344_m12.962186005531471_m38.47261478466609_m12.934002015361491_8_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50073006631474_m12.961333960783888_m38.4725327574897_m12.932373724953635_9_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50096584572687_m12.96121100042776_m38.47440076442133_m12.934017719276726_10_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50082829471482_m12.960720017172312_m38.47384043859295_m12.933596799909374_11_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.501118552381065_m12.962947784137462_m38.47426226643149_m12.932564078786635_12_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.502373456830234_m12.962333491657414_m38.47477812160141_m12.93271906374045_13_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50148403583942_m12.965290796965846_m38.471909395581456_m12.932729360653218_14_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.501890924160584_m12.961062102765782_m38.4732392389171_m12.933884816602236_15_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.5007597052321_m12.961099590741043_m38.473517022103756_m12.933269493665131_16_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50151426278066_m12.96224952417061_m38.473343947418165_m12.932595128870267_17_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50340379765633_m12.963068504924866_m38.473898022861405_m12.932939179700924_18_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.501402782516365_m12.962743981859667_m38.47361068224981_m12.929892203606808_19_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.500951062259055_m12.964628446152132_m38.47375669394401_m12.93455351878407_20_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.500486678608006_m12.963212145332431_m38.474758327361364_m12.933328833777356_21_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50234447884447_m12.961648999633914_m38.474661277554_m12.93489642987398_22_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50229159113205_m12.961490473565357_m38.474209563384555_m12.933428060221484_23_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.500568338650666_m12.963562146885746_m38.47357849097421_m12.93225101151055_24_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50115701483925_m12.9612635544437_m38.47509217365817_m12.933188948092502_25_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50186554346796_m12.961718758432754_m38.47355380440904_m12.934289622568668_26_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50165434807298_m12.96187628063375_m38.47332172286755_m12.933277161490693_27_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50177737556065_m12.962596650290932_m38.472904517360526_m12.933331456516722_28_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.50009702898103_m12.96036292373261_m38.47412281703678_m12.934711892250165_29_30_weight_heuristic_SPFA_further_insertion',
    '../data/results/m38.500734794836475_m12.961295117029927_m38.473498428492356_m12.932937589096973_30_30_weight_heuristic_SPFA_further_insertion'
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
    #print("NN SDP", i, cumulative_t)
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
    #print("NI SDP", i, cumulative_i)
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
    #print("FI SDP", i, cumulative_d)
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
    print("NI LWP", i, cumulative_i_b)
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
    #print("FI LWP", i, cumulative_d_b)
    x3_b.append(i)

######################################

fig = plt.figure()
plt.xlim(-7, 190)
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