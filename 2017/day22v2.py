from enum import Enum
from typing import List, Set, Tuple

import numpy as np
from scipy.sparse import coo_matrix, dok_matrix


class CellStatus(Enum):
    CLEAN = 0
    WEAKENED = 1
    INFECTED = 2
    FLAGGED = 3


class Grid:
    def __init__(self, map_: List[List[str]]):
        self.matrix = self._init_table(map_)
        self.position: Tuple[int, int] = (12, 12)
        self.direction: Tuple[int, int] = (-1, 0)

    def turn_right(self):
        if self.direction == (-1, 0):
            self.direction = 0, -1
        elif self.direction == (0, -1):
            self.direction = 1, 0
        elif self.direction == (1, 0):
            self.direction = 0, 1
        elif self.direction == (0, 1):
            self.direction = -1, 0

    def turn_left(self):
        self.turn_right()
        self.turn_right()
        self.turn_right()

    def turn_back(self):
        self.turn_right()
        self.turn_right()

    def _init_table(self, map_: List[List[str]]):
        size = len(map_)
        entry_array = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                if map_[i][j] == '#':
                    entry_array[i][j] = CellStatus.INFECTED.value

        return dok_matrix(entry_array, np.int8)

    def process_turn(self):
        print(self.direction)
        value = self.matrix[self.position]

        if value == CellStatus.CLEAN.value:
            self.turn_left()
        if value == CellStatus.INFECTED.value:
            self.turn_right()
        if value == CellStatus.FLAGGED.value:
            self.turn_back()

        self.matrix[self.position] = (self.matrix[self.position] + 1) % 4

        self.position = self.position[0] + \
            self.direction[0], self.position[1] + self.direction[1]

    def process_all(self):
        for i in range(10000000):
            if i % 10000 == 0:
                print(self.direction)
            self.process_turn()


class GridV2:
    infected: Set[Tuple[int, int]] = set()
    weakened: Set[Tuple[int, int]] = set()
    flagged: Set[Tuple[int, int]] = set()

    def __init__(self, map_: List[List[str]]):
        self.size = len(map_)
        self._init_table(map_)
        center = self.size // 2
        self.position: Tuple[int, int] = (center, center)
        self.direction: Tuple[int, int] = (-1, 0)

        self.infection_count = 0

    def _init_table(self, map_: List[List[str]]):
        size = len(map_)
        for i in range(size):
            for j in range(size):
                if map_[i][j] == '#':
                    self.infected.add((i, j))

    def turn_left(self):
        if self.direction == (-1, 0):
            self.direction = 0, -1
        elif self.direction == (0, -1):
            self.direction = 1, 0
        elif self.direction == (1, 0):
            self.direction = 0, 1
        elif self.direction == (0, 1):
            self.direction = -1, 0

    def turn_right(self):
        self.turn_left()
        self.turn_left()
        self.turn_left()

    def turn_back(self):
        self.turn_left()
        self.turn_left()

    def process_turn(self):
        if self.position in self.infected:
            self.turn_right()
            self.infected.remove(self.position)
            self.flagged.add(self.position)
        elif self.position in self.flagged:
            self.turn_back()
            self.flagged.remove(self.position)
        elif self.position in self.weakened:
            self.weakened.remove(self.position)
            self.infected.add(self.position)
            self.infection_count += 1
        else:
            self.turn_left()
            self.weakened.add(self.position)

        self.position = (
            self.position[0] + self.direction[0],
            self.position[1] + self.direction[1]
        )

    def process_all(self):

        for i in range(10):
            self.print_map()
            if i % 1000 == 0:
                print(self)
            self.process_turn()
        print(self.infection_count)

    def __str__(self):
        return f'{self.direction}, F:{len(self.flagged)}, #:{len(self.infected)}, W:{len(self.weakened)}, Infections:{self.infection_count}'

    def print_map(self):
        map_result = [
            ['.' for _ in range(self.size)]
            for _ in range(self.size)
        ]
        for pos in self.infected:
            map_result[pos[0]][pos[1]] = '#'
        for pos in self.weakened:
            map_result[pos[0]][pos[1]] = 'W'
        for pos in self.flagged:
            map_result[pos[0]][pos[1]] = 'F'
        print('+++++++++++++++')
        for row in map_result:
            print(' '.join(row))


if __name__ == "__main__":
    with open('inputs/day22test', 'r') as input_file:
        map_: List[str] = input_file.readlines()
        map_ = [operation.replace('\n', '') for operation in map_]
        map_ = [list(row) for row in map_]

        grid = GridV2(map_)
        grid.process_all()
