from functools import reduce
from itertools import cycle

PUZZLE_INPUT = 361527


def versors_generator():
    return cycle(((1, 0), (0, 1), (-1, 0), (0, -1)))


def multiply_coords(multiplier, coord2):
    return multiplier * coord2[0], multiplier * coord2[1]


def add_coords(coords1, coords2):
    return coords1[0] + coords2[0], coords1[1] + coords2[1]


def counts_generator(number):
    i = 1
    first = True
    for _ in range(number - 1):
        yield i
        if not first:
            i += 1
        first = not first


def road_generator(number):
    road_count = 1
    versors = versors_generator()
    counts = counts_generator(number)
    while True:
        count = next(counts)
        versor = next(versors)
        i = 0
        while i < count:
            road_count += 1
            if road_count > number:
                return
            yield versor
            i += 1


def get_coordinates(number):
    if number == 1:
        return 0, 0

    def add_coords(coord1, coord2):
        return coord1[0] + coord2[0], coord1[1] + coord2[1]

    return reduce(add_coords,
                  road_generator(number))


def distance(coords1, coords2):
    return abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1])


def get_distance_from_zero(number):
    a, b = get_coordinates(number)
    return distance((0, 0), (a, b))


def is_neighbour(coords1, coords2):
    return (abs(coords1[0] - coords2[0]) == 1 or abs(coords1[1] - coords2[1]) == 1) and distance(
        coords2, coords1) <= 2


def get_larger_than(limit):
    count = 1
    numbers = [(1, (0, 0))]
    current_value = 1
    while current_value <= limit:
        count += 1
        coords = reduce(add_coords, road_generator(count))
        current_value = sum((number[0] for number in numbers if is_neighbour(number[1], coords)))
        numbers.append((current_value, coords))
    return current_value


if __name__ == '__main__':
    print(get_distance_from_zero(PUZZLE_INPUT))
    print(get_larger_than(PUZZLE_INPUT))
