from collections import deque
from pprint import pprint
from typing import List

DIRECTIONS = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}


def add_coords(coords1, coords2):
    return (
        coords1[0] + coords2[0],
        coords1[1] + coords2[1]
    )


def enlarge_map(map_: List[List], rows: int):
    new_size = len(map_[0]) + rows
    new_map = deque()
    for row in map_:
        new_map.append(deque(row))
    for row in new_map:
        for _ in range(rows // 2):
            row.appendleft('.')
            row.append('.')
    for _ in range(rows // 2):
        new_map.appendleft(['.'] * new_size)
    for _ in range(rows // 2):
        new_map.append(['.'] * new_size)
    return [list(row) for row in new_map]


class Grid:
    def __init__(self, map_: List[List]):
        self.map = map_
        self.virus_position = ((len(map_) // 2), (len(map_) // 2))
        self.infected_count = 0
        self.direction = 0

    def burst(self):
        if self.is_infected():
            self.direction = (self.direction + 1) % 4
            self.clean()
        else:
            self.direction = (self.direction - 1) % 4
            self.infect()
            self.infected_count += 1
        self.virus_position = add_coords(
            self.virus_position, DIRECTIONS[self.direction])

    def is_infected(self):
        position = self.virus_position
        cell = self.map[position[0]][position[1]]
        if cell == '#':
            return True
        else:
            return False

    def infect(self):
        self.map[self.virus_position[0]][self.virus_position[1]] = '#'

    def clean(self):
        self.map[self.virus_position[0]][self.virus_position[1]] = '.'


class GridImproved(Grid):
    STATES = {
        '.': 0,  # CLEAN
        'W': 1,  # WEAKENED
        '#': 2,  # INFECTED
        'F': 3  # FLAGGED
    }

    def __init__(self, map_):
        super().__init__(map_)
        self.infected_initially = set()
        for i in range(len(map_)):
            for j in range(len(map_)):
                if map_[i][j] == '#':
                    self.infected_initially.add((i, j))

    def burst(self):
        state = self.get_state()
        if state == 0:
            self.direction = (self.direction - 1) % 4
            self.weaken()
        if state == 1:
            self.infect()
            if self.virus_position not in self.infected_initially:
                self.infected_count += 1
        if state == 2:
            self.direction = (self.direction + 1) % 4
            self.clean()
        if state == 3:
            self.direction = (self.direction + 2) % 4
            self.clean()
        self.virus_position = add_coords(
            self.virus_position, DIRECTIONS[self.direction])

    def get_state(self):
        return self.STATES[self.map[self.virus_position[0]][self.virus_position[1]]]

    def weaken(self):
        self.map[self.virus_position[0]][self.virus_position[1]] = 'W'

    def flag(self):
        self.map[self.virus_position[0]][self.virus_position[1]] = 'F'


if __name__ == '__main__':
    with open('inputs/day22', 'r') as input_file:
        map_ = input_file.readlines()
        map_ = [operation.replace('\n', '') for operation in map_]
        map_ = [list(row) for row in map_]
        map_ = enlarge_map(map_, 100)
        grid = Grid(map_)
        for _ in range(10000):
            grid.burst()
        print(grid.infected_count)

        map_ = enlarge_map(map_, 400)
        grid_v2 = GridImproved(map_)
        for _ in range(10000000):
            grid_v2.burst()
        print(grid_v2.infected_count)
        # pprint([''.join(row) for row in grid_v2.map])
