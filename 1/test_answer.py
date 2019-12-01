import fuel
import pytest


@pytest.fixture
def read_modules():
    with open("1/input.txt") as f:
        modules = [int(line) for line in f]
    return modules


def test_answer1(read_modules):
    assert fuel.fuel_total(read_modules) == 3235550


def test_answer2(read_modules):
    assert fuel.fuel_total_incl_fuel(read_modules) == 4850462
