import itertools
import string
from pprint import pprint
from typing import Any, Dict, List, Set, Tuple

with open('inputs/day4') as input_file:
    lines: List[Dict[str, str]] = []
    result = {}
    for line in input_file.readlines():
        if line != '\n':
            for field in line.replace('\n', '').split(' '):
                name, value = field.split(':')
                result[name] = value
        else:
            lines.append(result)
            result = {}
    if result:
        lines.append(result)
        result = {}

def is_height_valid(height):
    if height[-2:] == 'cm':
        return  150 <= int(height[:-2]) <= 193
    if height[-2:] == 'in':
        return  59 <= int(height[:-2]) <= 76

def is_hcl_valid(hcl: str) -> bool:
    if len(hcl) != 7:
        return False
    return hcl[0] == '#' and all(char in string.ascii_lowercase + string.digits for char in hcl[1:])

def is_pid_valid(pid: str) -> bool:
    return len(pid) == 9 and set(pid).issubset(string.digits)

def is_valid(passport: dict):
    fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    return all(
        passport.get(field) for field in fields
        ) and all((
        1920 <= int(passport['byr']) <= 2002,
        2010 <= int(passport['iyr']) <= 2020,
        2020 <= int(passport['eyr']) <= 2030,
        is_height_valid(passport['hgt']),
        is_hcl_valid(passport['hcl']),
        passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        is_pid_valid(passport['pid']),
        ))

def part1(passports: List[Dict[str, str]]):
    results = [passport for passport in passports if is_valid(passport)]
    return len(results)


def part2(input_):
    values = [x.split() for x in input_]
    result = 0
    return result


if __name__ == "__main__":
    pprint([(line, is_valid(line)) for line in lines])
    print(part1(lines))
    # print(part2(input_values))
