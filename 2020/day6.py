import itertools
import string
from typing import Any, Dict, List, Set, Tuple

with open('inputs/day6') as input_file:
    groups: List[List[str]] = []
    group: List[str] = []
    input_values = [x.replace('\n', '') for x in input_file.readlines()]
    for line in input_values:
        if line == '':
            groups.append(group)
            group = []
        else:
            group.append(line)
    groups.append(group)


def part1(input_: List[List[str]]) -> int:
    result = 0
    for group in input_:
        letters = set()
        for answers in group:
            letters |= set(answers)
        result += len(letters)
    return result


def part2(input_):
    result = 0
    for group in input_:
        letters = set(string.ascii_lowercase)
        for answers in group:
            letters &= set(answers)
        result += len(letters)
    return result


if __name__ == "__main__":
    print(part1(groups))
    print(part2(groups))
