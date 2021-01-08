import itertools
import string
from typing import Any, Dict, List, Set, Tuple

with open('inputs/day14') as input_file:
    input_values= [line.strip() for line in input_file.readlines()]

def sum_with_mask(value:int, mask:str) -> int:
    format_str = 'value:0{0}b'.format(len(mask))
    format_str = '{' + format_str + '}'
    value_bytes = format_str.format(value=value)
    result = ''
    for i in range(1, len(mask)+1):
        if mask[-i] == '0':
            result += '0'
        elif mask[-i] == '1':
            result += '1'
        else:
            result += value_bytes[-i]
    return int(result[::-1], base=2)


def part1(input_):
    memory = {}
    mask = 0
    for line in input_:
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
        elif line.startswith('mem'):
            mem, value = line.split(' = ')
            memory_index = int(mem[4:-1])
            memory[memory_index] = sum_with_mask(int(value), mask)
    return sum(memory.values())


def get_address(masked_address: str, combination: List[bool]) -> int:
    result = masked_address
    for value in combination:
        result = result.replace('X', str(int(value)), 1)
    return int(result, base=2)

def mask_addresses(address: int, mask: str) -> Set[int]:
    format_str = 'value:0{0}b'.format(len(mask))
    format_str = '{' + format_str + '}'
    address_bytes = format_str.format(value=address)
    result = ''
    for i in range(1, len(mask)+1):
        if mask[-i] == '0':
            result += address_bytes[-i]
        elif mask[-i] == '1':
            result += '1'
        else:
            result += 'X'
    return {
        get_address(result[::-1], option) for option in itertools.product((True, False), repeat=result.count('X'))
    }

def part2(input_):
    memory = {}
    mask = ''
    for line in input_:
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
        elif line.startswith('mem'):
            mem, value = line.split(' = ')
            memory_index = int(mem[4:-1])
            for address in mask_addresses(memory_index, mask):
                memory[address] = int(value)
    return sum(memory.values())


if __name__ == "__main__":
    print(part1(input_values))
    print(part2(input_values))
