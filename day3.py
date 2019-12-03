import utilities


def read_input(filename):
    with open(filename) as f:
        array = []
        for line in f:
            line = line.rstrip(",\n")
            array.append([str(x) for x in line.split(",")])
    return array


def manhattan_distance(wire1, wire2):
    postions_wire1, _ = generate_wire(wire1)
    postions_wire2, _ = generate_wire(wire2)

    intersections = postions_wire1.intersection(postions_wire2)

    dist = list()
    for elem in intersections:
        dist.append(abs(elem[0]) + abs(elem[1]))

    return min(dist)


def intersection_distance(wire1, wire2):
    postions_wire1, steps_wire1 = generate_wire(wire1)
    postions_wire2, steps_wire2 = generate_wire(wire2)

    intersections = postions_wire1.intersection(postions_wire2)

    dist = list()
    for elem in intersections:
        dist.append(steps_wire1[elem] + steps_wire2[elem])

    return min(dist)


def generate_wire(wire):
    positions = set()
    last_pos = (0, 0)
    steps = dict()
    number_steps = 0
    for w in wire:
        pos = last_pos
        for i in range(1, int(w[1:]) + 1):
            number_steps += 1
            if w.startswith("R"):
                new_pos = (pos[0] + i, pos[1])
            elif w.startswith("L"):
                new_pos = (pos[0] - i, pos[1])
            elif w.startswith("U"):
                new_pos = (pos[0], pos[1] + i)
            elif w.startswith("D"):
                new_pos = (pos[0], pos[1] - i)
            steps[new_pos] = number_steps
            last_pos = new_pos
            positions.add(new_pos)
    return positions, steps


@utilities.timer
def distance_exercise1():
    paths = read_input("input_day3.txt")
    dist = manhattan_distance(paths[0], paths[1])
    return dist


@utilities.timer
def distance_exercise2():
    paths = read_input("input_day3.txt")
    dist = intersection_distance(paths[0], paths[1])
    return dist


print(f"Result: {distance_exercise1()}")

print(f"Result: {distance_exercise2()}")
