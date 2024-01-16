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


def solve1(arg: Iterable[str]) -> int:
    pass
    
def solve2(arg: Iterable[str]) -> int:
    pass

## Test 1
test_cases_1 = (
    (
        [
            '$ cd /',
        ], 95437
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
            '$ cd /',
        ], 95437
    ),
)

# for value, expected_result in test_cases_2:
#     assert solve2(value) == expected_result

## Part 2

print(solve2(lines))