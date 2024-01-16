import string
import itertools
import re
from collections import deque
from copy import deepcopy
from pathlib import PurePosixPath as Path
from typing import Iterable
import operator
import math

GAMES_RE = re.compile(r'Game (\d+)')

CUBES_MAX = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open('inputs/day2.txt') as input_file:
    lines = tuple(line.strip() for line in input_file.readlines())

def get_games_minimums(lines: Iterable[str]) -> dict[int, dict[str, int]]:
    games = {}
    for line in lines:
        prefix, game_progress = line.split(':')
        game_id = int(GAMES_RE.match(prefix.strip()).groups()[0])
        game_steps = (turn.strip() for turn in game_progress.strip().split(';'))
        max_numbers = {}
        for step in game_steps:
            colours_numbers = step.split(', ')
            for entry in colours_numbers:
                split_entry = entry.split(' ')
                colour, number = split_entry[1], int(split_entry[0])
                if not max_numbers.get(colour):
                    max_numbers[colour] = number
                else:
                    max_numbers[colour] = max((max_numbers[colour], number))
        games[game_id] = max_numbers
    return games

def is_game_possible(max_numbers: dict[str, int]) -> bool:
    for colour, value in max_numbers.items():
        if value > CUBES_MAX[colour]:
            return False
    return True

def get_possible_games(lines: Iterable[str]) -> set[int]:
    games = get_games_minimums(lines)
    return {game_id for game_id, game_progress in games.items() if is_game_possible(game_progress)}

def solve1(lines: Iterable[str]) -> int:
    return sum(get_possible_games(lines))
        
    
def solve2(lines: Iterable[str]) -> int:
    games = get_games_minimums(lines)
    sum_ = 0
    for game in games.values():
        sum_ += math.prod(game.values())
    return sum_


## Test 1
test_cases_1 = (
    (
        [
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
        ], 8
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
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
        ], 2286
    ),
)

for value, expected_result in test_cases_2:
    assert solve2(value) == expected_result

## Part 2

print(solve2(lines))