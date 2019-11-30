import re
from collections import Counter
from typing import Dict, Tuple

initial_rx = re.compile(f'initial state: ([.#]*)')

with open('day12_input') as input_file:
    initial_state = initial_rx.match(input_file.readline()).groups()[0]
    input_file.readline()

    operations = {line.split()[0]: line.split()[2] for line in input_file.readlines()}


def part1(initial_state, operations, generations):
    plants = {i: initial_state[i] for i in range(len(initial_state))}
    start, end = -len(initial_state), len(initial_state) * 2
    for i in range(start, end):
        if not plants.get(i):
            plants[i] = '.'

    old_state = dict(plants)
    for _ in range(generations):
        new_state = dict(plants)
        for i in range(start + 2, end - 2):
            current = ''.join(old_state[x] for x in range(i-2, i+3))
            for operation in operations:
                if current == operation:
                    new_state[i] = operations[operation]
        old_state = dict(new_state)
    
    # print(''.join((old_state[i] for i in sorted(old_state.keys()))))
    # print([index for index in old_state.keys() if old_state[index] == '#'])
    return sum((index for index in old_state.keys() if old_state[index] == '#'))


def char_to_bool(char: str) -> bool:
    return True if char == '#' else False


class State:
    def __init__(self, initial_state: str, mapping: Dict[str, str]):
        self.plants = set()
        for index, char in enumerate(initial_state):
            if char == '#':
                self.plants.add(index)
        self._init_mapping(mapping)

    def _init_mapping(self, mapping: Dict[str, str]):
        self.mapping: Dict[Tuple[bool], bool] = {}
        for key, value in mapping.items():
            new_key = tuple(char_to_bool(x) for x in key)
            self.mapping[new_key] = char_to_bool(value)

    def __str__(self):
        result = []
        for i in range(min(self.plants), max(self.plants)+1):
            if i in self.plants:
                result.append('#')
            else:
                result.append('.')
        return ''.join(result)

    def process(self):
        new_plants = set()
        for i in range(min(self.plants) - 2, max(self.plants) + 3):
            current = tuple(x in self.plants for x in range(i-2, i+3))
            has_plant = self.mapping[current]
            if has_plant:
                new_plants.add(i)
        self.plants = new_plants
        print(self, sum(self.plants), min(self.plants), max(self.plants))

    def process_generations(self, generations: int):
        for _ in range(generations):
            self.process()
        return sum(self.plants)


# print(part1(initial_state, operations, generations=20))

state = State(initial_state, operations)
result500 = state.process_generations(500)
result1000 = state.process_generations(500)
print((result1000 - result500)/500)

print((50000000000 - 1000)*78 + result1000)
