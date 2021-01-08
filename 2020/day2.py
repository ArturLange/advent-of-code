import itertools
from typing import Any, Dict, List, Set, Tuple

with open('inputs/day2') as input_file:
    input_values: List[str] = [x.replace('\n', '') for x in input_file.readlines()]


def part1(input_: List[str]):
    values: List[List[str]] = [x.split() for x in input_]
    result = 0
    for args in values:
        min_, max_ = [int(x) for x in args[0].split('-')]
        letter = args[1].replace(':', '')
        password = args[2]
        if min_ <= password.count(letter) <= max_:
            result += 1
    return result


def part2(input_: List[str]):
    values: List[List[str]]  = [x.split() for x in input_]
    result = 0
    for args in values:
        min_, max_ = [int(x) for x in args[0].split('-')]
        letter = args[1].replace(':', '')
        password = args[2]
        set_: Set[str] = set((password[min_-1], password[max_-1]))
        if len(set_) > 1 and letter in set_:
            result += 1
    return result


if __name__ == "__main__":
    print(part1(input_values))
    print(part2(input_values))
