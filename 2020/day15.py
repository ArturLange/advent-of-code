import itertools
import string
from typing import Any, Dict, List, Set, Tuple

input_values = [6,3,15,13,1,0]


def rindex(value: int, list_: List[int]) -> int:
    for i in range(2, len(list_)+1):
        if list_[-i] == value:
            return len(list_) - i
    return len(list_) - 1

def part1(input_):
    return find_number_2(input_, 2020)

def find_number(input_, limit):
    index = len(input_)-1 # index of last value
    while len(input_) < limit:
        last_time = rindex(input_[index], input_)
        input_.append(index - last_time)
        index += 1
    return input_[limit-1]

def find_number_2(input_, limit):
    numbers = {value: index for index, value in enumerate(input_[:-1])}
    last_index = len(input_)
    last_value = input_[-1]
    while last_index < limit:
        if numbers.get(last_value) is not None:
            value = last_index - numbers[last_value] -1 
        else:
            value = 0
        numbers[last_value] = last_index -1 
        last_index += 1
        last_value = value

    return last_value


def part2(input_):
    return find_number_2(input_, 30000000)


if __name__ == "__main__":
    print(part1(input_values))
    print(part2(input_values))
