from functools import reduce
from itertools import cycle


def versors_generator():
    return cycle(((1, 0), (0, 1), (-1, 0), (0, -1)))


def multiply_coords(multiplier, coord2):
    return multiplier * coord2[0], multiplier * coord2[1]


def counts_generator(number):
    road = []
    for i in range(1, number):
        road.extend([i, i])

    return road[:number - 1]


def road_generator(number):
    versors = versors_generator()
    road = []
    for count in counts_generator(number):
        versor = next(versors)
        i = 0
        while i < count:
            road.append(versor)
            i += 1
    return road[:number - 1]


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
    print(get_distance(10240))
