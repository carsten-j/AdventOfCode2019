import numpy as np


def total_fuel(modules):
    input = np.array(modules)
    output = np.sum(input // 3 - 2)
    return output


def total_fuel_incl_fuel(modules):
    fuel = 0
    for module in modules:
        tmp = module // 3 - 2
        while tmp > 0:
            fuel = fuel + tmp
            tmp = tmp // 3 - 2
    return fuel
