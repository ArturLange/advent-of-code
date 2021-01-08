import itertools
import string
from functools import lru_cache, reduce
from pprint import pprint
from typing import Any, Collection, Dict, Iterable, List, Set, Tuple

with open('inputs/day11') as input_file:
    input_values= [list(x.strip()) for x in input_file.readlines()]

FLOOR = '.'
EMPTY_SEAT = 'L'
OCCUPIED = '#'

def get_new_value(old_state, i, j):
    current_value = old_state[i][j]
    if current_value == FLOOR:
        return current_value

    adjacent = []
    if i < len(old_state)-1:
        adjacent.append(old_state[i+1][j])
        if j < len(old_state[i+1])-1:
            adjacent.append(old_state[i+1][j+1])
        if j > 0:
            adjacent.append(old_state[i+1][j-1])
    if i > 0:
        adjacent.append(old_state[i-1][j])
        if j < len(old_state[i-1])-1:
            adjacent.append(old_state[i-1][j+1])
        if j > 0:
            adjacent.append(old_state[i-1][j-1])
    if j < len(old_state[i])-1:
        adjacent.append(old_state[i][j+1])
    if j > 0:
        adjacent.append(old_state[i][j-1])
    
    if current_value == EMPTY_SEAT and OCCUPIED not in set(adjacent):
        return OCCUPIED
    if current_value == OCCUPIED and adjacent.count(OCCUPIED) >= 4:
        return EMPTY_SEAT
    return current_value


def get_new_state(old_state):
    return [[get_new_value(old_state, i, j) for j in range(len(old_state[i]))] for i in range(len(old_state))]

def part1(input_):
    
    old_state = list(input_)
    new_state = get_new_state(old_state)
    while new_state != old_state:
        old_state = new_state
        new_state = get_new_state(old_state)
    
    return sum([line.count(OCCUPIED) for line in new_state])
    


def get_new_value2(old_state, i, j):
    current_value = old_state[i][j]
    if current_value == FLOOR:
        return current_value

    adjacent = []

    i_range = range(len(old_state))
    j_range = range(len(old_state[0]))

    k = 1
    result = ''
    while i-k in i_range and not result:
        if old_state[i-k][j] == OCCUPIED:
            result = OCCUPIED
        else:
            k += 1
    result = result or EMPTY_SEAT
    adjacent.append(result)

    k = 1
    result = ''
    while i+k in i_range and not result:
        if old_state[i+k][j] == OCCUPIED:
            result = OCCUPIED
        else:
            k += 1
    result = result or EMPTY_SEAT
    adjacent.append(result)

    k = 1
    result = ''
    while j+k in j_range and not result:
        if old_state[i][j+k] == OCCUPIED:
            result = OCCUPIED
        else:
            k += 1
    result = result or EMPTY_SEAT
    adjacent.append(result)

    k = 1
    result = ''
    while j-k in j_range and not result:
        if old_state[i][j-k] == OCCUPIED:
            result = OCCUPIED
        else:
            k += 1
    result = result or EMPTY_SEAT
    adjacent.append(result)

    k = 1
    result = ''
    while i-k in i_range and j-k in j_range and not result:
        if old_state[i-k][j-k] == OCCUPIED:
            result = OCCUPIED
        else:
            k += 1
    result = result or EMPTY_SEAT
    adjacent.append(result)

    if current_value == OCCUPIED and adjacent.count(OCCUPIED) >= 5:
        return EMPTY_SEAT

    k = 1
    result = ''
    while i-k in i_range and j+k in j_range and not result:
        if old_state[i-k][j+k] == OCCUPIED:
            result = OCCUPIED
        else:
            k += 1
    result = result or EMPTY_SEAT
    adjacent.append(result)

    if current_value == OCCUPIED and adjacent.count(OCCUPIED) >= 5:
        return EMPTY_SEAT

    k = 1
    result = ''
    while i+k in i_range and j-k in j_range and not result:
        if old_state[i+k][j-k] == OCCUPIED:
            result = OCCUPIED
        else:
            k += 1
    result = result or EMPTY_SEAT
    adjacent.append(result)

    if current_value == OCCUPIED and adjacent.count(OCCUPIED) >= 5:
        return EMPTY_SEAT

    k = 1
    result = ''
    while i+k in i_range and j+k in j_range and not result:
        if old_state[i+k][j+k] == OCCUPIED:
            result = OCCUPIED
        else:
            k += 1
    result = result or EMPTY_SEAT
    adjacent.append(result)
    
    if current_value == EMPTY_SEAT and OCCUPIED not in set(adjacent):
        return OCCUPIED
    if current_value == OCCUPIED and adjacent.count(OCCUPIED) >= 5:
        return EMPTY_SEAT
    return current_value


def get_new_state2(old_state):
    return [[get_new_value2(old_state, i, j) for j in range(len(old_state[i]))] for i in range(len(old_state))]

def part2(input_):
    old_state = list(input_)
    new_state = get_new_state2(old_state)
    while new_state != old_state:
        old_state = new_state
        new_state = get_new_state2(old_state)
    
    return sum([line.count(OCCUPIED) for line in new_state])


if __name__ == "__main__":
    # print(part1(input_values))
    # print(part2(input_values))

    import cProfile as profile
    profile.run('print(part2(input_values))')
