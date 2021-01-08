from collections import defaultdict, Counter
from typing import Set, List, Dict
from itertools import product

task_input = '193651-649729'
test_input = [
    ['R8', 'U5', 'L5', 'D3'],
    ['U7', 'R6', 'D4', 'L4']
]

print(task_input)


def two_adjacent(number):
    num = str(number)
    for i in range(5):
        if num[i] == num[i + 1]:
            return True
    return False


def two_adjacent_2(number):
    num = str(number)
    return 2 in Counter(num).values()


def numbers_increase(number):
    num = str(number)
    return num == ''.join(sorted(num))


def part1(input_):
    a, b = input_.split('-')
    ran = range(int(a), int(b) + 1)
    # breakpoint()
    passwords = list(
        filter(lambda x: numbers_increase(x) and two_adjacent(x), ran))
    return len(passwords)


def part2(input_):
    a, b = input_.split('-')
    ran = range(int(a), int(b) + 1)
    # breakpoint()
    passwords = list(
        filter(lambda x: numbers_increase(x) and two_adjacent_2(x), ran))
    return len(passwords)


if __name__ == '__main__':
    print(part1(task_input))
    print(part2(task_input))
