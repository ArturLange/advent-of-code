import string
import itertools
import re
from collections import deque
from copy import deepcopy
from pathlib import PurePosixPath as Path
from typing import Iterable
import operator

with open('inputs/day8.txt') as input_file:
    lines = tuple(line.strip() for line in input_file.readlines())

def get_visibility_grid(tree_grid: Iterable[str]):
    pass

class Grid:
    def __init__(self, lists_of_rows: Iterable[Iterable]) -> None:
        self.lists_of_rows = tuple(tuple(x) for x in lists_of_rows)

    def element(self, x: int, y: int):
        return self.lists_of_rows[y][x]
    
    @property
    def elements_count(self) -> int:
        return len(self.lists_of_rows) * len(self.lists_of_rows[0])
    
    @property
    def len_x(self) -> int:
        return len(self.lists_of_rows[0])
    
    @property
    def len_y(self) -> int:
        return len(self.lists_of_rows)
    
    def element_neighbours(self, x: int, y: int) -> tuple:
        result = []
        if y > 0:
            result.append(self.lists_of_rows[y-1][x])
        if x > 0:
            result.append(self.lists_of_rows[y][x-1])
        if x < self.len_x - 1:
            result.append(self.lists_of_rows[y][x+1])
        if y < self.len_y - 1:
            result.append(self.lists_of_rows[y+1][x])
        return tuple(result)

    def is_element_hidden(self, x: int, y: int) -> bool:
        if x == 0 or y == 0:
            return False
        value = self.element(x, y)
        for i in range(1, x+1):
            if value <= self.element(x-i, y):
                break
        else:
            return False
        
        for i in range(1, y+1):
            if value <= self.element(x, y-i):
                break
        else:
            return False
        
        for i in range(1, self.len_x - x):
            if value <= self.element(x+i, y):
                break
        else:
            return False
        
        for i in range(1, self.len_y - y):
            if value <= self.element(x, y+1):
                break
        else:
            return False
        return True


    @property
    def hidden_elements(self) -> int:
        hiddens = tuple(
            (x, y)
            for x in range(len(self.lists_of_rows[0])) for y in range(len(self.lists_of_rows))
            if self.is_element_hidden(x, y)
        )
        return tuple(element for element in hiddens if element)

def solve1(lines: Iterable[str]) -> int:
    values = tuple((int(x) for x in list(line)) for line in lines)
    grid = Grid(values)
    print(f"Grid has {grid.elements_count} elements - {len(grid.hidden_elements)} hidden and {grid.elements_count - len(grid.hidden_elements)} visible")
    return grid.elements_count - len(grid.hidden_elements)
    
def solve2(arg: Iterable[str]) -> int:
    pass

## Test 1
test_cases_1 = (
    (
        [
            '30373',
            '25512',
            '65332',
            '33549',
            '35390'
        ], 21
    ),
)

for value, expected_result in test_cases_1:
    assert solve1(value) == expected_result

## Part 1

print(solve1(lines))

## Test 2

test_cases_2 = (
    (
        [
            '30373',
            '25512',
            '65332',
            '33549',
            '35390'
        ], 21
    ),
)

# for value, expected_result in test_cases_2:
#     assert solve2(value) == expected_result

## Part 2

# print(solve2(lines))