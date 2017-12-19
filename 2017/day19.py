import string
from typing import Tuple

DIRECTIONS = {
    'down': (1, 0),
    'up:': (-1, 0),
    'right': (0, 1),
    'left': (0, -1)
}


def get_starting_point(path_map) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    for cell_index in range(len(path_map[0])):
        if path_map[0][cell_index] in '-|':
            return (0, cell_index), DIRECTIONS['down']
    for cell_index in range(len(path_map[-1])):
        if path_map[-1][cell_index] in '-|':
            return (len(path_map), cell_index), DIRECTIONS['up']
    for cell_index in range(len(path_map)):
        if path_map[cell_index][0] in '-|':
            return (cell_index, 0), DIRECTIONS['right']
        if path_map[cell_index][-1] in '-|':
            return (cell_index, len(path_map[cell_index])), DIRECTIONS['left']


def get_position_cell(coords: Tuple[int, int], path_map) -> str:
    return path_map[coords[0]][coords[1]]


def get_opposite_direction(direction: Tuple[int, int]) -> Tuple[int, int]:
    x, y = direction
    return (x, -y) if x == 0 else (-x, y)


def get_new_direction(
        coords: Tuple[int, int],
        path_map,
        direction: Tuple[int, int]):
    for dir_ in [dir_ for dir_ in DIRECTIONS.values() if
                 dir_ not in (direction, get_opposite_direction(direction))]:
        position = coords[0] + dir_[0], coords[1] + dir_[1]
        if get_position_cell(position, path_map) != ' ':
            return dir_
    return None


def walk_the_path(path_map):
    location, direction = get_starting_point(path_map)
    steps = 0
    letters = []
    while True:
        cell: str = get_position_cell(location, path_map)
        if cell in string.ascii_uppercase:
            letters.append(cell)
            if get_position_cell((location[0] + direction[0], location[1] + direction[1]),
                                 path_map) == ' ':
                return letters, steps
        if cell == '+':
            direction = get_new_direction(location, path_map, direction)
            if not direction:
                return letters
        if direction:
            location = location[0] + direction[0], location[1] + direction[1]
            steps += 1


if __name__ == '__main__':
    with open('inputs/day19', 'r') as input_file:
        path_map = [line.replace('\n', '') for line in input_file.readlines()]
        result = walk_the_path(path_map)
        print(''.join(result[0]), result[1])
