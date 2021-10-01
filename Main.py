import random
import Configuration
import Simulation


def get_seed(seed_id):
    """
    This function provides the random seed.

    :param seed_id:     int
                        the seed_id is the 'seeds' vector index
    :return:
    """

    seeds = [1859168769, 1598189534, 1871883252,
             2125204119, 358485174,
             1695858027, 762772169, 437720306,
             939612284, 1998078925, 981631283, # 2041095833
             1024155645, 558746720, 1349341884,
             678622600, 722594620,
             1700738670, 1995749838, 346983590,
             565528207, 513791680, 2081634991,
             1769370802, 349544396, 1996610406,
             1973272912,1972392646, 188312339,
             934100682, 2101442385, 222735214,
             2009044369, 1895218768, 701857417,
             89865291, 144443207, 720236707,
             822780843, 898723423, 1644999263,
             985046914, 1859531344, 1024155645,
             764283187, 778794064, 683102175,
             1334983095, 1072664641, 999157082,
             1277478588, 960703545, 186872697,
             425414105, 694388766, 773370613,
             1384311643, 1000004583, 1147024708,
             538474442, 1936856304, 1996632795,
             1936856304, 1822174485, 1859168769,
             605846893, 2041095833, 1319566104,
             1996610406]
    return seeds[seed_id]


def main():
    """
    This function executes the experiments on the SUMO simulator.
    First of all, it sets the characteristics of the scenario:
    number of collect points, values of vehicle weight increment,
    city of the scenario, number of repetitions of the simulations, etc.
    Then, it creates pseudo-random collect points/stop points of the
    scenario. Finally, the function calls the 'create_route' function.
    """

    # number of collect points
    n_points = 18

    # maximum increment of vehicle weight at the collect point (material mass)
    max_mass_material = 5

    # random seed of mass increment
    random.seed(get_seed(0))

    # scenarios: 'Belo Horizonte' and 'Belem'
    city = 'Sao Paulo'

    # mean of the gaussian function
    if city == 'Belo Horizonte':
        mean_lon = [-43.9438]
        mean_lat = [-19.9202]
    elif city == 'Belem':
        mean_lon = [-48.47000]
        mean_lat = [-1.46000]
    elif city == 'Salvador':
        mean_lon = [-38.487310]
        mean_lat = [-12.947855]
    else:
        mean_lon = [-46.64842]
        mean_lat = [-23.56363]

    # standard deviation of the gaussian function
    sigma = 0.002 #0.005

    # vector with vehicle weight increment in the collect points
    mass_increments = [random.randint(0, max_mass_material) for i in range(n_points-2)]

    # add unit of measurement of vehicle weight increment in the collect points
    material_weights = [(mass_increments[i], 'Kg') for i in range(n_points-2)]

    # the arrival point must not increment the vehicle weight
    material_weights.append((0, 'Kg'))

    # the starting point must not increment the vehicle weight
    material_weights.insert(0, (0, 'Kg'))

    # number of repetitions of the simulations
    n_seeds = 1

    json_files = []
    materials = {}

    for a in range(0, n_seeds):

        random.seed(get_seed(a))
        print(get_seed(a))
        longitudes = [random.gauss(mean_lon[0], sigma) for i in range(n_points)]
        latitudes = [random.gauss(mean_lat[0], sigma) for i in range(n_points)]
        stop_points = [(float(latitudes[i]), float(longitudes[i])) for i in range(len(latitudes))]
        [materials.update([((latitudes[i], longitudes[i]), material_weights[i])]) for i in range(len(latitudes))]
        json_files = Configuration.create_route(stop_points, materials, json_files, get_seed(a), a, n_points)

    Simulation.write_json(json_files, str(n_points) + '_points')
    print(json_files)


if __name__ == "__main__":
    main()