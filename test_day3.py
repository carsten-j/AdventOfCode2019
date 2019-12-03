import day3


def test_answer1():
    dist = day3.distance_exercise1()
    assert dist == 2180


def test_answer2():
    dist = day3.distance_exercise2()
    assert dist == 112316


def test_intersection_distance():
    path1 = ["R8", "U5", "L5", "D3"]
    path2 = ["U7", "R6", "D4", "L4"]

    res = day3.intersection_distance(path1, path2)

    assert res == 30


def test_manhattan_distance():
    path1 = ["R8", "U5", "L5", "D3"]
    path2 = ["U7", "R6", "D4", "L4"]

    res = day3.manhattan_distance(path1, path2)

    assert res == 6


def test_longer_manhattan_distance():
    path1 = ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
    path2 = ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]

    res = day3.manhattan_distance(path1, path2)

    assert res == 159
