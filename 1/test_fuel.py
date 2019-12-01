import fuel


def test_fuel_1():
    assert fuel.fuel_total([12]) == 2


def test_fuel_2():
    assert fuel.fuel_total([14.0]) == 2


def test_fuel_3():
    assert fuel.fuel_total([1969]) == 654


def test_fuel_4():
    assert fuel.fuel_total([100756]) == 33583


def test_total_fuel_2():
    modules = [12, 14, 1969, 100756]
    assert fuel.fuel_total(modules) == (2 + 2 + 654 + 33583)


def test_total_fuel_fuel_1():
    assert fuel.fuel_incl_fuel(0, 14) == 2


def test_total_fuel_fuel_2():
    assert fuel.fuel_incl_fuel(0, 1969) == 966


def test_total_fuel_fuel_3():
    assert fuel.fuel_incl_fuel(0, 100756) == 50346
