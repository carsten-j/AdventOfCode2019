import day4
import pytest


def test_answer1():
    assert 1625 == day4.number_of_valid_passwords()


def test_answer2():
    assert 1111 == day4.number_of_valid_adjacent_matching_passwords()
