import itertools
import math
import string
from typing import Any, Dict, List, Set, Tuple

with open('inputs/day12') as input_file:
    input_values= [line.strip() for line in input_file.readlines()]

test_data = [
    'F10',
    'N3',
    'F7',
    'R90',
    'F11',
]

class Vector:
    def __init__(self, values):
        self.values = tuple(values)
    
    def __add__(self, other):
        return Vector(self.values[index] + other[index] for index in range(len(self.values)))
    
    def __sub__(self, other):
        return Vector(self.values[index] - other[index] for index in range(len(self.values)))
    
    def __mul__(self, other):
        return Vector(self.values[index] * other for index in range(len(self.values)))

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, index):
        return self.values[index]
    
    def __len__(self):
        return len(self.values)
    
    def distance(self, other):
        return ((self.values[0] - other[0]) ** 2 + (self.values[1] - other[1]) ** 2) ** 0.5

def cur_direction(degrees: int) -> Vector:
    radians = math.radians(degrees)
    return Vector((
        round(math.cos(radians)),
        round(math.sin(radians))
    ))

def part1(input_):
    coords: Vector = Vector((0, 0))
    current_degree: int = 0
    for line in input_:
        direction, value = line[:1], int(line[1:])
        if direction == 'N':
            coords += Vector((0, value))
        if direction == 'S':
            coords -= Vector((0, value))
        if direction == 'W':
            coords -= Vector((value, 0))
        if direction == 'E':
            coords += Vector((value, 0))
        if direction == 'F':
            coords += cur_direction(current_degree) * value
        if direction == 'R':
            current_degree -= value
        if direction == 'L':
            current_degree += value
    return abs(coords[0]) + abs(coords[1])

def rotate_waypoint(waypoint: Vector, degrees: int) -> Vector:
    if degrees == 180:
        return waypoint * -1
    distance = waypoint.distance(Vector((0, 0)))
    if waypoint[0] != 0:
        tangent = waypoint[1] / waypoint[0]
        current_degrees = math.degrees(math.atan(tangent)) % 360
        current_degrees =  (current_degrees + degrees) % 360 
    else:
        if waypoint[1] > 0:
            current_degrees = 90
        else:
            current_degrees = 270
    radians = math.radians(current_degrees)
    return Vector((
        round(math.cos(radians) * distance),
        round(math.sin(radians) * distance)
    ))



def part2(input_):
    coords = Vector((0, 0))
    waypoint = Vector((10, 1))
    for line in input_:
        direction, value = line[:1], int(line[1:])
        if direction == 'N':
            waypoint += Vector((0, value))
        if direction == 'S':
            waypoint -= Vector((0, value))
        if direction == 'W':
            waypoint -= Vector((value, 0))
        if direction == 'E':
            waypoint += Vector((value, 0))
        if direction == 'F':
            coords += waypoint * value
        if direction == 'R':
            waypoint = rotate_waypoint(waypoint, -value)
        if direction == 'L':
            waypoint = rotate_waypoint(waypoint, value)
    return abs(coords[0]) + abs(coords[1])


if __name__ == "__main__":
    # print(part1(input_values))
    print(part2(input_values))
