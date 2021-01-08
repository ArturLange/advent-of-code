import functools
import itertools
import string
from typing import Any, Dict, Iterable, List, Set, Tuple


def prod(args):
    return functools.reduce(lambda x, y: x * y, args)


with open('inputs/dayX') as input_file:
    input_values = [line.strip() for line in input_file.readlines()]


def part1(input_):
    values = [x.split() for x in input_]
    result = 0
    return result


def part2(input_):
    values = [x.split() for x in input_]
    result = 0
    return result


if __name__ == "__main__":
    print(part1(input_values))
    # print(part2(input_values))
