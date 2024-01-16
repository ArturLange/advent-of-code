import string
import itertools
import re
from collections import deque
from copy import deepcopy

with open('inputs/day6.txt') as input_file:
    values = input_file.readline()

test_cases_1 = (
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
    ('nppdvjthqldpwncqszvftbrmjlhg', 6),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11)
)

def solve1(val):
    for i in range(4, len(val)):
        substring = val[i-4:i]
        if len(set(substring)) == 4:
            return i
        
def solve2(val):
    for i in range(14, len(val)):
        substring = val[i-14:i]
        if len(set(substring)) == 14:
            return i
        
## Test 1

for value, expected_result in test_cases_1:
    assert solve1(value) == expected_result

## Part 1

print(solve1(values))

## Test 2

test_cases_2 = (
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
    ('nppdvjthqldpwncqszvftbrmjlhg', 23),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26)
)

for value, expected_result in test_cases_2:
    assert solve2(value) == expected_result

## Part 2

print(solve2(values))