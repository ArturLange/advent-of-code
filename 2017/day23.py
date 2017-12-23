import re
from collections import deque
from typing import List, Union


class Execution:
    def __init__(self, operations: List[str]):
        self.operations = operations
        self.sounds = {x: 0 for x in 'abcdefgh'}
        self.set_re = re.compile(r'set (?P<sound>[a-z]) (?P<value>-?[a-z0-9]+)')
        self.sub_re = re.compile(r'sub (?P<sound>[a-z]) (?P<value>-?[a-z0-9]+)')
        self.mul_re = re.compile(r'mul (?P<sound>[a-z]) (?P<value>-?[a-z0-9]+)')
        self.jnz_re = re.compile(r'jnz (?P<sound>[a-z0-9]) (?P<value>-?[a-z0-9]+)')
        self.mul_counter = 0

    def get_value(self, value):
        try:
            return int(value)
        except ValueError:
            return self.sounds[value]

    def execute(self):
        i = 0
        while i < len(self.operations):
            operation = self.operations[i]
            if self.set_re.fullmatch(operation):
                match = self.set_re.fullmatch(
                    operation)
                sound: str = match.group('sound')
                value: Union[str, int] = match.group('value')
                self.sounds[sound] = self.get_value(value)
            elif self.sub_re.fullmatch(operation):
                match = self.sub_re.fullmatch(
                    operation)
                sound = match.group('sound')
                value = match.group('value')
                self.sounds[sound] -= self.get_value(value)
            elif self.mul_re.fullmatch(operation):
                match = self.mul_re.fullmatch(
                    operation)
                sound = match.group('sound')
                value = match.group('value')
                self.sounds[sound] *= self.get_value(value)
                self.mul_counter += 1
            elif self.jnz_re.fullmatch(operation):
                match = self.jnz_re.fullmatch(
                    operation)
                sound = match.group('sound')
                value = match.group('value')
                if self.get_value(sound) != 0:
                    i += self.get_value(value)
                    i -= 1
            i += 1


if __name__ == '__main__':
    with open('inputs/day23', 'r') as input_file:
        operations = input_file.readlines()
        operations = [operation.replace('\n', '') for operation in operations]
        execution = Execution(operations)
        execution.execute()
        print(execution.mul_counter)
