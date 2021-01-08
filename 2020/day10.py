import itertools
import string
from functools import lru_cache, reduce
from pprint import pprint
from typing import Any, Collection, Dict, Iterable, List, Set, Tuple

with open('inputs/day10') as input_file:
    input_values: List[int] = [int(x.strip()) for x in input_file.readlines()]


test_input = [28,
33,
18,
42,
31,
14,
46,
20,
48,
47,
24,
23,
49,
45,
19,
38,
39,
11,
1,
32,
25,
35,
8,
17,
7,
9,
4,
2,
34,
10,
3]


def part1(input_: List[int]):
    current = 0
    ones, threes = 0, 0
    joltages: List[int] = sorted(input_)
    for joltage in joltages:
        if joltage - current == 1:
            ones += 1
        if joltage - current == 3:
            threes += 1
        current = joltage
    return ones * (threes+1)


@lru_cache(maxsize=4096)
def is_valid_path(path: Collection[int]) -> bool:
    return all((path[i+1]-path[i] <=3 for i in range(len(path)-1)))


def generate_options(joltages: List[int]) -> int:
    skippables = []
    for index in range(len(joltages)):
        if 0 < index < len(joltages)-1 and joltages[index+1] - joltages[index-1] <= 3:
            skippables.append(index)
    print(skippables)
    max_to_skip = min((len(skippables), max(joltages)//3)) # not to skip more than possible
    options = itertools.product((True, False), repeat=len(skippables))
    for to_be_skipped in options:
        to_be_skipped = tuple(itertools.compress(skippables, to_be_skipped))
        if len(to_be_skipped) <= max_to_skip and not does_contain_three_consecutive(to_be_skipped):
            option = tuple(joltages[i] for i in range(len(joltages)) if i not in to_be_skipped)
            if is_valid_path(option):
                print(option)
                yield option

def generate_options2(joltages: List[int]) -> int:
    skippables = []
    element_2before = 0
    element_before = 0
    for element in joltages[1:-1]:
        if element_before != 0 and element - element_2before <= 3:
            skippables.append(element_before)
        element_2before, element_before = element_before, element
    print(skippables)
    joltages_set = set(joltages)
    max_to_skip = min((len(skippables), max(joltages_set)//3))

    for length in range(max_to_skip):
        for to_be_skipped in itertools.combinations(skippables, length):
            if not does_contain_three_consecutive(to_be_skipped):
                option = tuple(joltages_set.difference(to_be_skipped))
                if is_valid_path(option):
                    yield option


def does_contain_three_consecutive(option):
    if len(option) < 3:
        return False
    for i in range(len(option)-2):
        if option[i] +2 == option[i+1] + 1 == option[i+2]:
            return True

def simplify(joltages):
    result = list(joltages)
    for i in reversed(range(len(result))):
        if result[i] - result[i-1] == 3:
            result = result[:i-1] + [x-3 for x in result[i:]]
    return joltages

def part2(input_):
    input_ = sorted(input_)[:40]
    # input_ = test_input
    input_ = [1,2,3,4, 5, 6, 7]
    output_joltage = max(input_) + 3
    joltages: List[int] = sorted(input_ + [0, output_joltage])

    print(joltages)
    possible_variations = len(set(generate_options(joltages)))
    return possible_variations


# def part2(input_):
#     result = 0
#     input_ = sorted(input_)
#     output_joltage = max(input_) + 3
#     input_ = [0] + input_ + [output_joltage]
#     print(input_)
#     (a, b, c, d, *_) = input_

#     breakpoint()
#     return result


if __name__ == "__main__":
    # print(part1(input_values))
    print(part2(input_values))

    # import cProfile as profile
    # profile.run('print(part2(input_values))')
