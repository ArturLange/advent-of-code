import functools
import itertools
import re
import string
from typing import Any, Dict, Iterable, List, Set, Tuple


def prod(args):
    return functools.reduce(lambda x, y: x * y, args)


with open('inputs/day19') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

    # TEST_INPUT
    # lines = [
    #     '0: 4 1 5',
    #     '1: 2 3 | 3 2',
    #     '2: 4 4 | 5 5',
    #     '3: 4 5 | 5 4',
    #     '4: "a"',
    #     '5: "b"',
    #     '',
    #     'ababbb',
    #     'bababa',
    #     'abbbab',
    #     'aaabbb',
    #     'aaaabbb',
    # ]
    index = 0
    messages, rule_lines = [], []
    rules = {}
    while lines[index] != '':
        key, value = lines[index].split(': ')
        rules[int(key)] = value.strip('"')
        index += 1
    index += 1
    for line in lines[index:]:
        messages.append(line)


def is_rule_complete(rule: str):
    return set(rule).issubset(set(' |()' + string.ascii_lowercase))


def part1(rules: Dict[int, str], messages: Iterable[str]):
    @functools.lru_cache(maxsize=512)
    def complete_rule(rule):
        if is_rule_complete(rule):
            return rule
        subrules = (x for x in rule.split(' ')
                    if set(x).issubset(set(string.digits)))
        for subrule in subrules:
            rule = rule.replace(subrule, complete_rule(rules[int(subrule)]), 1)
        rule = rule.replace(' ', '')
        if '|' in rule:
            rule = f'({rule})'
        return rule

    while not all(is_rule_complete(rule) for rule in rules.values()):
        for key, rule in rules.items():
            rules[key] = complete_rule(rule)
    regexes = {index: re.compile(rule) for index, rule in rules.items()}
    re_0 = regexes[0]
    messages_matched = tuple(message for message in messages
                             if re_0.fullmatch(message))
    return len(messages_matched)


def part2(input_):
    values = [x.split() for x in input_]
    result = 0
    return result


if __name__ == "__main__":
    print(part1(rules, messages))
    # print(part2(input_values))
