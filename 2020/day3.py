import itertools
from functools import reduce
from typing import Any, Dict, List, Set, Tuple

with open('inputs/day3') as input_file:
    input_values= [x.replace('\n', '') for x in input_file.readlines()]


def part1(input_map):
    result = 0
    index = 0
    for row in input_map:
        if row[index] == '#':
            result = result + 1
        index = (index + 3 )% len(row)
    return result


def part2(input_map):
    results = []
    index = 0
    result = 0

    for row in input_map:
        if row[index] == '#':
            result = result + 1
        index = (index + 1 )% len(row)
    results.append(result)
    result = 0
    index = 0
    for row in input_map:
        if row[index] == '#':
            result = result + 1
        index = (index + 3 )% len(row)
    results.append(result)
    result = 0
    index = 0
    for row in input_map:
        if row[index] == '#':
            result = result + 1
        index = (index + 5 )% len(row)
    results.append(result)
    result = 0
    index = 0
    for row in input_map:
        if row[index] == '#':
            result = result + 1
        index = (index + 7 )% len(row)
    results.append(result)
    result = 0
    index = 0
    for row in input_map[0::2]:
        if row[index] == '#':
            result = result + 1
        index = (index + 1 )% len(row)
    results.append(result)
    result = 0
    index = 0

    print(results)
    return reduce(lambda x, y: x*y, results)


if __name__ == "__main__":
    print(part1(input_values))
    print(part2(input_values))
