import itertools
import string
from typing import Any, Dict, List, Set, Tuple

with open('inputs/day8') as input_file:
    input_values = list(map(lambda x: (x[0], int(x[1])), [x.strip().split(' ') for x in input_file.readlines()]))


def part1(input_: List[Tuple[str, int]]):
    accumulator = 0
    instructions_ran = [0] * len(input_)
    index = 0
    while True:
        operation, value = input_[index]
        instructions_ran[index] += 1
        if instructions_ran[index] >= 2:
            return accumulator
        if operation == 'acc':
            accumulator += value
            index += 1
        elif operation == 'jmp':
            index += value
        elif operation == 'nop':
            index += 1


def run_instructions(input_: List[Tuple[str, int]]) -> Tuple[int, bool]:
    terminated_normally = False
    accumulator = 0
    instructions_ran = [0] * len(input_)
    index = 0
    while True:
        if index >= len(input_):
            terminated_normally = True
            return accumulator, terminated_normally
        operation, value = input_[index]
        instructions_ran[index] += 1
        if instructions_ran[index] >= 2:
            return accumulator, terminated_normally
        if operation == 'acc':
            accumulator += value
            index += 1
        elif operation == 'jmp':
            index += value
        elif operation == 'nop':
            index += 1

def part2(input_: List[Tuple[str, int]]):
    for index in range(len(input_)):
        new_input = list(input_)
        if input_[index][0] == 'jmp':
            new_input[index] = 'nop', new_input[index][1]
        elif input_[index][0] == 'nop':
            new_input[index] = 'jmp', new_input[index][1]
        
        value, terminated_normally = run_instructions(new_input)
        if terminated_normally:
            return value


if __name__ == "__main__":
    # print(part1(input_values))
    print(part2(input_values))
