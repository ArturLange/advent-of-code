import string
import itertools
import re
from collections import deque
from copy import deepcopy
from pathlib import PurePosixPath as Path
from typing import Iterable, Collection
import operator
from collections import defaultdict
import math

with open('inputs/day4.txt') as input_file:
    input_lines = tuple(line.strip() for line in input_file.readlines())

def get_score(winning: set[int], mine: set[int]) -> int:
    correct_numbers = len(winning & mine)
    if correct_numbers == 0:
        return 0
    return int(math.pow(2, correct_numbers - 1))


def solve1(lines: Iterable[str]) -> int:
    summed_points = 0
    for line in lines:
        card_number, rest = line.split(':')
        card_id: int = int(card_number[5:])
        split_numbers = rest.strip().split('|')
        winning_numbers = set(int(number) for number in split_numbers[0].strip().split(' ') if number != '')
        my_numbers = set(int(number) for number in split_numbers[1].strip().split(' ') if number != '')
        summed_points += get_score(winning_numbers, my_numbers)
    return summed_points
    
def solve2(lines: Iterable[str]) -> int:
    summed_points = 0
    for line in lines:
        card_number, rest = line.split(':')
        card_id: int = int(card_number[5:])
        split_numbers = rest.strip().split('|')
        winning_numbers = set(int(number) for number in split_numbers[0].strip().split(' ') if number != '')
        my_numbers = set(int(number) for number in split_numbers[1].strip().split(' ') if number != '')
        summed_points += get_score(winning_numbers, my_numbers)
    return summed_points

## Test 1
test_cases_1 = (
    (
        [
            'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
            'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
            'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
            'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
            'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
            'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
        ], 13
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
            '$ cd /',
        ], 95437
    ),
)

# for value, expected_result in test_cases_2:
#     assert solve2(value) == expected_result

## Part 2

print(solve2(input_lines))