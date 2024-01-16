
from typing import Iterable

import regex as re

with open('inputs/day1.txt') as input_file:
    lines = tuple(line.strip() for line in input_file.readlines())

DIGIT_RE = re.compile(r'one|two|three|four|five|six|seven|eight|nine|\d')

DIGIT_MAPPING = {
    'one': 1, 
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def solve1(arg: Iterable[str]) -> int:
    sum_ = 0
    for line in arg:
        digits = []
        for char in line:
            if char.isdigit():
                if len(digits) <= 1:
                    digits.append(char)
                else:
                    digits[1] = char
        if len(digits) == 1:
            digits = digits * 2
        sum_ += int(''.join(digits))
    return sum_
        
def word_to_digit(word: str) -> str:
    if digit := DIGIT_MAPPING.get(word):
        return str(digit)
    else:
        return word
    
def line_to_digits(line: str) -> int:
    matches = DIGIT_RE.findall(line, overlapped=True) # overlapped is important here
    digits = [word_to_digit(matches[0]), word_to_digit(matches[-1])]
    return int(''.join(digits))

def solve2(arg: Iterable[str]) -> int:
    sum_ = 0
    for line in arg:
        sum_ += line_to_digits(line)
    return sum_

## Test 1
test_cases_1 = (
    (
        [
            '1abc2',
            'pqr3stu8vwx',
            'a1b2c3d4e5f',
            'treb7uchet',
        ], 142
    ),
)

for value, expected_result in test_cases_1:
    assert solve1(value) == expected_result

## Part 1

print(solve1(lines))

## Test 2

test_cases_2 = (
    (
        [
            'two1nine',
            'eightwothree',
            'abcone2threexyz',
            'xtwone3four',
            '4nineeightseven2',
            'zoneight234',
            '7pqrstsixteen',
        ], 281
    ),
)

for value, expected_result in test_cases_2:
    assert solve2(value) == expected_result

## Part 2

print(solve2(lines))