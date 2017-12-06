from functools import reduce
from itertools import cycle

PUZZLE_INPUT = 361527


def versors_generator():
    return cycle(((1, 0), (0, 1), (-1, 0), (0, -1)))


def multiply_coords(multiplier, coord2):
    return multiplier * coord2[0], multiplier * coord2[1]


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


def get_distance(number):
    a, b = get_coordinates(number)
    return abs(a) + abs(b)


if __name__ == '__main__':
    print(get_distance(PUZZLE_INPUT))
