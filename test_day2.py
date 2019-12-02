import day2
import pytest
import utilities


@pytest.fixture
def read_input():
    with open("input_day2.txt") as f:
        array = []
        for line in f:
            array = array + [int(x) for x in line.split(",")]
    return array


def test_answer_1(read_input):
    result = day2.computer_v1(read_input, 12, 2)
    assert result == 5482655


def test_answer_2(read_input):
    result = day2.computer_v2(read_input)
    assert result == 4967


def test_computer():
    program = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    result = day2.compute(program)
    expected = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    utilities.compare_lists(result, expected)


@pytest.mark.parametrize(
    "input, expected",
    [
        ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
        ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
        ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
        ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
    ],
)
def test_compute(input, expected):
    result = day2.compute(input)
    utilities.compare_lists(result, expected)
