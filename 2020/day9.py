import itertools
import string
from typing import Any, Dict, Iterable, List, Set, Tuple

with open('inputs/day9') as input_file:
    input_values: List[int] = [int(x.strip()) for x in input_file.readlines()]


def is_number_valid(number: int, preamble: Iterable[int]):
    preamble_2 = sorted(filter(lambda x: x<= number, preamble))
    for num_1 in preamble_2:
        if number - num_1 in preamble_2:
            return True
    return False

def part1(input_) -> int:
    for i in range(25, len(input_)):
        value = input_[i]
        if not is_number_valid(value, input_[:i]):
            return value

def part2(input_: List[int], error_number: int):
    for i in range(len(input_)):
        j = i
        value = input_[i]
        while value < error_number:
            j += 1
            value += input_[j]
        if value == error_number:
            range_ = input_[i:j+1]
            print(min(range_), max(range_))
            return min(range_) + max(range_)


if __name__ == "__main__":
    print(part2(input_values, part1(input_values)))
