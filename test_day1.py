import day1
import pytest


@pytest.fixture
def read_modules():
    with open("input_day1.txt") as file:
        modules = [int(line) for line in file]
    return modules


def test_answer1(read_modules):
    assert day1.total_fuel(read_modules) == 3235550


def test_answer2(read_modules):
    assert day1.total_fuel_incl_fuel(read_modules) == 4850462


@pytest.mark.parametrize(
    "input, expected", [([12], 2), ([14.0], 2), ([1969], 654), ([100756], 33583), ([12, 14, 1969, 100756], (2 + 2 + 654 + 33583))]
)
def test_fuel_1(input, expected):
    assert day1.total_fuel(input) == expected


@pytest.mark.parametrize(
    "input, expected", [([14], 2), ([1969], 966), ([100756], 50346)]
)
def test_total_fuel_fuel_1(input, expected):
    assert day1.total_fuel_incl_fuel(input) == expected
