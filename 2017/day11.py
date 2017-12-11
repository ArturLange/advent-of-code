# x = cos a
# y = sin a
import math
from functools import reduce
from math import cos, sin, tan

PI = math.pi

DIRECTIONS = {
    'n': (0, 1),
    's': (0, -1),
    'ne': (cos(PI / 6), sin(PI / 6)),
    'nw': (cos(5 * PI / 6), sin(5 * PI / 6)),
    'sw': (cos(7 * PI / 6), sin(7 * PI / 6)),
    'se': (cos(11 * PI / 6), sin(11 * PI / 6)),
}


def add_coords(coord1, coord2):
    return coord1[0] + coord2[0], coord1[1] + coord2[1]


def get_position(path):
    return reduce(add_coords, [DIRECTIONS[x] for x in path])


def distance(coords1, coords2):
    return abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1])


def get_path(path):
    position = get_position(path)
    steps = 0
    while distance(position, (0, 0)) >= 0.5:
        x, y = position
        if x == 0:
            if y < 0:
                position = add_coords(position, DIRECTIONS['n'])
            else:
                position = add_coords(position, DIRECTIONS['s'])
        else:
            a = y / x
            if x > 0 and y > 0:
                if 0 < a <= tan(PI / 3):
                    position = add_coords(position, DIRECTIONS['sw'])
                else:
                    position = add_coords(position, DIRECTIONS['s'])
            if x < 0 and y > 0:
                if a <= tan(2 * PI / 3):
                    position = add_coords(position, DIRECTIONS['s'])
                else:
                    position = add_coords(position, DIRECTIONS['se'])
            if x < 0 and y < 0:
                if a <= tan(4 * PI / 3):
                    position = add_coords(position, DIRECTIONS['ne'])
                else:
                    position = add_coords(position, DIRECTIONS['n'])
            if x > 0 and y < 0:
                if a <= tan(5 * PI / 3):
                    position = add_coords(position, DIRECTIONS['n'])
                else:
                    position = add_coords(position, DIRECTIONS['nw'])
        steps += 1
    return steps


if __name__ == '__main__':
    with open('inputs/day11', 'r') as input_file:
        path = input_file.readline().split(',')
        print(get_path(path))
