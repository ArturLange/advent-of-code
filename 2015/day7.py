import re
from functools import lru_cache
from typing import List, Tuple

RE_IDENTIFIER = r'[a-zA-Z0-9]'

RE_NOT = re.compile(f'NOT\s{RE_IDENTIFIER}+')
RE_LSHIFT = re.compile(f'{RE_IDENTIFIER}+\sLSHIFT\s{RE_IDENTIFIER}+')
RE_RSHIFT = re.compile(f'{RE_IDENTIFIER}+\sRSHIFT\s{RE_IDENTIFIER}+')
RE_AND = re.compile(f'{RE_IDENTIFIER}+\sAND\s{RE_IDENTIFIER}+')
RE_OR = re.compile(f'{RE_IDENTIFIER}+\sOR\s{RE_IDENTIFIER}+')

tree = dict()


def initial_signals(circuit):
    result = {}
    for operation in circuit:
        pattern = re.compile(f'[a-z]*')
        for identifier in operation.split():
            if pattern.fullmatch(identifier):
                result[identifier] = None
    return result


def parse_operation(operation: str) -> Tuple[str, str, List[str]]:
    value, name = operation.split('-> ')
    if len(value.split()) == 3:
        func = value.split()[1]
        arguments = [value.split()[0], value.split()[2]]
    if len(value.split()) == 2:
        func = value.split()[0]
        arguments = [value.split()[1]]
    if len(value.split()) == 1:
        func = ''
        arguments = [value.split()[0]]
    return name, func, arguments


class Wire:
    def __init__(self, operation, tree):
        self.operation = operation
        self.name, self.func, self.arguments = parse_operation(operation)
        self.tree = tree


@lru_cache(2048)
def get_value(name: str):
    if name.isnumeric():
        return int(name)
    arguments = tree[name].arguments
    if tree[name].func == '':
        argument = arguments[0]
        return get_value(argument)
    if tree[name].func == 'NOT':
        argument = arguments[0]
        return 65535 - get_value(argument)
    if tree[name].func == 'OR':
        return get_value(arguments[0]) | get_value(arguments[1])
    if tree[name].func == 'AND':
        return get_value(arguments[0]) & get_value(arguments[1])
    if tree[name].func == 'LSHIFT':
        return get_value(arguments[0]) << get_value(arguments[1])
    if tree[name].func == 'RSHIFT':
        return get_value(arguments[0]) >> get_value(arguments[1])


if __name__ == "__main__":
    with open('day7input') as input_file:
        operations = list(map(lambda x: x.replace(
            '\n', ''), input_file.readlines()))
    tree = initial_signals(operations)
    for op in operations:
        wire = Wire(op, tree)
        tree[wire.name] = wire
    result_tree = {
        x: get_value(x) for x in tree
    }
    from pprint import pprint
    pprint(result_tree)
