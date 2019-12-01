import numpy as np


def fuel_total(modules):
    input = np.array(modules)
    output = np.sum(input // 3 - 2)
    return output


def fuel_incl_fuel(total, mass):
    fuel = fuel_total([mass])
    if fuel < 0:
        return total
    else:
        total = total + fuel
        return fuel_incl_fuel(total, fuel)


def fuel_total_incl_fuel(modules):
    fuel = 0
    for module in modules:
        fuel = fuel + fuel_incl_fuel(0, module)
    return fuel
