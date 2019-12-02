import numpy as np
import utilities


@utilities.timer
def total_fuel(modules):
    input = np.array(modules)
    output = np.sum(input // 3 - 2)
    return output


@utilities.timer
def total_fuel_incl_fuel(modules):
    total = 0
    for module in modules:
        fuel = module // 3 - 2
        while fuel > 0:
            total += fuel
            fuel = fuel // 3 - 2
    return total
