import string
import itertools
import re
from collections import deque
from copy import deepcopy
from pathlib import PurePosixPath as Path
from typing import Iterable, Collection
import operator
from collections import defaultdict

with open('inputs/day3.txt') as input_file:
    input_lines = tuple(line.strip() for line in input_file.readlines())

LINE_RE = re.compile(r'^[.+@$*%/#&=-]*(?:(\d+)+[.+@$*%/#&=-]*)*$')
NUMBER_RE = re.compile(r'(\d+)')

DIGITS = set(string.digits)

def solve1(lines: Collection[str]) -> int:
    sum_ = 0
    for line_number, line in enumerate(lines):
        pos = 0
        while match := NUMBER_RE.search(line, pos=pos):
            number = int(match.group())
            start, end = match.start(), match.end()
            pos = end
            y_start = max((line_number - 1, 0))
            y_end = min((line_number + 1, len(lines)-1))
            x_start = max((start - 1, 0))
            x_end = min((end + 1, len(line)-1))
            neighbours_set = set()
            for y in range(y_start, y_end+1):
                neighbours_set |= set(lines[y][x_start:x_end])
            if neighbours_set - DIGITS != {'.'}:
                sum_ += number
    return sum_
    
def solve2(lines: Collection[str]) -> int:
    gears = defaultdict(list)
    for line_number, line in enumerate(lines):
        pos = 0
        while match := NUMBER_RE.search(line, pos=pos):
            number = int(match.group())
            start, end = match.start(), match.end()
            pos = end
            y_start = max((line_number - 1, 0))
            y_end = min((line_number + 1, len(lines)-1))
            x_start = max((start - 1, 0))
            x_end = min((end + 1, len(line)-1))
            for y in range(y_start, y_end+1):
                for x in range(x_start, x_end):
                    if lines[y][x] == '*':
                        gears[(y, x)].append(number)
    real_gears = (numbers for numbers in gears.values() if len(numbers) == 2)
    return sum(x*y for x, y in real_gears)

## Test 1
test_cases_1 = (
    (
        [
            '467..114..',
            '...*......',
            '..35..633.',
            '......#...',
            '617*......',
            '.....+.58.',
            '..592.....',
            '......755.',
            '...$.*....',
            '.664.598..',
        ], 4361
    ),
)

for value, expected_result in test_cases_1:
    assert solve1(value) == expected_result

## Part 1

print(solve1(input_lines))

## Test 2

test_cases_2 = (
    (
        [
            '467..114..',
            '...*......',
            '..35..633.',
            '......#...',
            '617*......',
            '.....+.58.',
            '..592.....',
            '......755.',
            '...$.*....',
            '.664.598..',
        ], 467835
    ),
)

for value, expected_result in test_cases_2:
    assert solve2(value) == expected_result

## Part 2

print(solve2(input_lines))