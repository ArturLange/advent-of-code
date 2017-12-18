import re
import string
from typing import List


def execute(operations: List[str]):
    played = 0
    sounds = {x: 0 for x in string.ascii_lowercase}

    def get_value(value):
        try:
            return int(value)
        except ValueError:
            return sounds[value]

    i = 0
    while i < len(operations):
        operation = operations[i]
        if re.compile(r'snd (?P<sound>[a-z])').fullmatch(operation):
            sound = re.compile(r'snd (?P<sound>[a-z])').fullmatch(operation).group('sound')
            played = sounds[sound]
        elif re.compile(r'set (?P<sound>[a-z]) (?P<value>-?[a-z0-9]+)').fullmatch(operation):
            match = re.compile(r'set (?P<sound>[a-z]) (?P<value>-?[a-z0-9]+)').fullmatch(operation)
            sound = match.group('sound')
            value = match.group('value')
            sounds[sound] = get_value(value)
        elif re.compile(r'add (?P<sound>[a-z]) (?P<value>-?[a-z0-9]+)').fullmatch(operation):
            match = re.compile(r'add (?P<sound>[a-z]) (?P<value>-?[a-z0-9]+)').fullmatch(operation)
            sound = match.group('sound')
            value = match.group('value')
            sounds[sound] += get_value(value)
        elif re.compile(r'mul (?P<sound>[a-z]) (?P<value>-?[a-z0-9]+)').fullmatch(operation):
            match = re.compile(r'mul (?P<sound>[a-z]) (?P<value>-?[a-z0-9]+)').fullmatch(operation)
            sound = match.group('sound')
            value = match.group('value')
            sounds[sound] *= get_value(value)
        elif re.compile(r'mod (?P<sound>[a-z]) (?P<value>-?[a-z0-9]+)').fullmatch(operation):
            match = re.compile(r'mod (?P<sound>[a-z]) (?P<value>-?[a-z0-9]+)').fullmatch(operation)
            sound = match.group('sound')
            value = match.group('value')
            sounds[sound] %= get_value(value)
        elif re.compile(r'jgz (?P<sound>[a-z]) (?P<value>-?[a-z0-9]+)').fullmatch(operation):
            match = re.compile(r'jgz (?P<sound>[a-z]) (?P<value>-?[a-z0-9]+)').fullmatch(operation)
            sound = match.group('sound')
            value = match.group('value')
            if sounds[sound] > 0:
                i += get_value(value)
                i -= 1
        elif re.compile(r'rcv (?P<sound>[a-z])').fullmatch(operation):
            sound = re.compile(r'rcv (?P<sound>[a-z])').fullmatch(operation).group('sound')
            if sounds[sound] > 0:
                return played
        i += 1


if __name__ == '__main__':
    with open('inputs/day18', 'r') as input_file:
        operations = input_file.readlines()
        operations = [operation.replace('\n', '') for operation in operations]
        print(execute(operations))
