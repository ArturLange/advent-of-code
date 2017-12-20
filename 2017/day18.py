import re
import string
from typing import List


class Execution:
    def __init__(self, operations: List[str]):
        self.operations = operations
        self.sounds = {x: 0 for x in string.ascii_lowercase}
        self.snd_re = re.compile(r'snd (?P<sound>[a-z])')
        self.set_re = re.compile(r'set (?P<sound>[a-z]) (?P<value>-?[a-z0-9]+)')
        self.add_re = re.compile(r'add (?P<sound>[a-z]) (?P<value>-?[a-z0-9]+)')
        self.mul_re = re.compile(r'mul (?P<sound>[a-z]) (?P<value>-?[a-z0-9]+)')
        self.mod_re = re.compile(r'mod (?P<sound>[a-z]) (?P<value>-?[a-z0-9]+)')
        self.jgz_re = re.compile(r'jgz (?P<sound>[a-z]) (?P<value>-?[a-z0-9]+)')
        self.rcv_re = re.compile(r'rcv (?P<sound>[a-z])')

    def get_value(self, value):
        try:
            return int(value)
        except ValueError:
            return self.sounds[value]

    def execute(self):
        played = 0

        i = 0
        while i < len(self.operations):
            operation = self.operations[i]
            if self.snd_re.fullmatch(operation):
                sound = self.snd_re.fullmatch(operation).group('sound')
                played = self.sounds[sound]
            elif self.set_re.fullmatch(operation):
                match = self.set_re.fullmatch(
                    operation)
                sound = match.group('sound')
                value = match.group('value')
                self.sounds[sound] = self.get_value(value)
            elif self.add_re.fullmatch(operation):
                match = self.add_re.fullmatch(
                    operation)
                sound = match.group('sound')
                value = match.group('value')
                self.sounds[sound] += self.get_value(value)
            elif self.mul_re.fullmatch(operation):
                match = self.mul_re.fullmatch(
                    operation)
                sound = match.group('sound')
                value = match.group('value')
                self.sounds[sound] *= self.get_value(value)
            elif self.mod_re.fullmatch(operation):
                match = self.mod_re.fullmatch(
                    operation)
                sound = match.group('sound')
                value = match.group('value')
                self.sounds[sound] %= self.get_value(value)
            elif self.jgz_re.fullmatch(operation):
                match = self.jgz_re.fullmatch(
                    operation)
                sound = match.group('sound')
                value = match.group('value')
                if self.sounds[sound] > 0:
                    i += self.get_value(value)
                    i -= 1
            elif self.rcv_re.fullmatch(operation):
                sound = self.rcv_re.fullmatch(operation).group('sound')
                if self.sounds[sound] > 0:
                    return played
            i += 1


if __name__ == '__main__':
    with open('inputs/day18', 'r') as input_file:
        operations = input_file.readlines()
        operations = [operation.replace('\n', '') for operation in operations]
        execution = Execution(operations)
        print(execution.execute())
