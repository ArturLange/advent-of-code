import itertools
import re
import string
from functools import lru_cache
from typing import Any, Dict, List, Set, Tuple

input_values = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''.split('\n')

with open('inputs/day7') as input_file:
    input_values= [x.replace('\n', '') for x in input_file.readlines()]
    key_re = r'(\w* \w*) bags'
    values_re = r'(\d* \w* \w*)'
    bags_dict = {}
    for line in input_values:
        key, value = line.split('contain')
        key_string = re.match(key_re, key).string.rstrip()[:-5]
        values: List[List[str]] = [value.split()[:-1] for value in re.match(values_re, value).string.strip(' .').split(',')]
        for value in values:
            if f'{value[0]} {value[1]}' != 'no other':
                if not bags_dict.get(key_string):
                    bags_dict[key_string] = {}
                bags_dict[key_string] |= {f'{value[1]} {value[2]}': int(value[0])}

def get_bags_inside(bags_dict, bag_name: str):
    if bags_dict.get(bag_name) is None:
        return set()
    result = set()
    result |= bags_dict.get(bag_name).keys()
    for bag_ in bags_dict[bag_name]:
        result |= get_bags_inside(bags_dict, bag_)
    return result



def part1(input_: Dict[str, Dict[str, int]]):
    target = 'shiny gold'
    bags_containing_target = set()
    for bag_name in input_:
        bags_inside_current_bag = get_bags_inside(input_, bag_name)
        if target in bags_inside_current_bag:
            bags_containing_target.add(bag_name)
    print(len(bags_containing_target))


def get_bags_inside_number(bags_dict, bag_name: str):
    if bags_dict.get(bag_name) is None:
        return 1
    return sum(amount * get_bags_inside_number(bags_dict, name) for name, amount in bags_dict[bag_name].items())+1


# @lru_cache(maxsize=512)
def part2(input_: Dict[str, Dict[str, int]]):
    return get_bags_inside_number(input_, 'shiny gold') - 1

if __name__ == "__main__":
    print(part1(bags_dict))
    print(part2(bags_dict))
