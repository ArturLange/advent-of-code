import string
import itertools
import re
from collections import deque
from copy import deepcopy

with open('inputs/day5.txt') as input_file:
    lines = tuple(line for line in input_file.readlines())

RE_CRANE_LOADS = re.compile(r'^(\s*\[[A-Z]\])+$')

RE_CRANE_NUMBERS = re.compile(r'^ (\d   )+\d $')

RE_MOVES = re.compile(r'move (\d+) from (\d+) to (\d+)')

crane_loads = []
crane_numbers = ''
moves = []
cranes = dict()

for line in lines:
    if RE_CRANE_LOADS.match(line):
        crane_loads.append(line)
    elif RE_CRANE_NUMBERS.match(line):
        crane_numbers = line
    elif RE_MOVES.match(line):
        moves.append(line)

for number in crane_numbers.split('   '):
    cranes[int(number)] = deque()

for line in crane_loads:
    loads = line[1::4]
    for index, letter in enumerate(loads):
        if letter != ' ':
            cranes[index + 1].append(letter)

cranes1 = cranes
cranes2 = deepcopy(cranes)

## Part 1

for move in moves:
    count, start_crane, end_crane = (int(x) for x in RE_MOVES.match(move).groups())
    for _ in range(count):
        cranes1[end_crane].appendleft(cranes1[start_crane].popleft())

print(''.join(x[0] for x in cranes1.values()))

## Part 2

for move in moves:
    count, start_crane, end_crane = (int(x) for x in RE_MOVES.match(move).groups())
    values = deque()
    for _ in range(count):
        values.append(cranes2[start_crane].popleft())
    cranes2[end_crane] = values + cranes2[end_crane]

print(''.join(x[0] for x in cranes2.values()))