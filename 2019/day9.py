from collections import defaultdict, Counter, deque
from enum import Enum, IntEnum
from typing import Set, List, Dict
from itertools import permutations

with open('inputs/day9') as input_file:
    task_input = [int(x) for x in input_file.readline().split(',')]

test_input = [
    1102, 34915192, 34915192, 7, 4, 7, 99, 0
]


class InstructionList:
    def __init__(self, values: List):
        self.values_dict: Dict[int, int] = defaultdict(int)
        self.values_dict.update({x: values[x] for x in range(len(values))})

    def __getitem__(self, item):
        if type(item) == slice:
            if item.step:
                range_ = range(item.start, item.stop, item.step)
            elif item.stop:
                range_ = range(item.start, item.stop)
            else:
                range_ = range(item.start, len(self.values_dict))
            return [self.values_dict[i] for i in range_]
        return self.values_dict[item]

    def __setitem__(self, key, value):
        self.values_dict[key] = value

    def __repr__(self):
        max_index = max(self.values_dict.keys())
        result = [self.values_dict[x] for x in range(max_index + 1)]
        return str(result)


class InputMode(IntEnum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class Execution:
    def __init__(self, input_: List[int], input_value: int):
        self.input_value = input_value
        self.instructions = InstructionList(input_)
        self.index = 0
        self.done = False
        self.outputs: List[str] = []
        self.relative_base = 0

    def input(self):
        return self.input_value

    def get_value(self, value: int, mode: int):
        if mode == InputMode.POSITION:
            return self.instructions[value]
        if mode == InputMode.IMMEDIATE:
            return value
        if mode == InputMode.RELATIVE:
            return self.instructions[self.relative_base + value]

        raise Exception('Invalid InputMode')

    def get_index(self, index: int, mode: int):
        if mode == InputMode.POSITION:
            return index
        if mode == InputMode.IMMEDIATE:
            raise Exception('Invalid InputMode')
        if mode == InputMode.RELATIVE:
            return self.relative_base + index

    def multiply(self, c: int, b: int, a: int):
        self.index += 1
        parameters = self.instructions[self.index:self.index + 3]
        self.index += 3
        index = self.get_index(parameters[2], a)
        result = (
            self.get_value(parameters[0], c) * self.get_value(parameters[1], b)
        )

        self.instructions[index] = result

    def jump_if_zero(self, c: int, b: int):
        parameters = self.instructions[self.index + 1:self.index + 3]
        jump_value = self.get_value(parameters[0], c)

        if jump_value == 0:
            self.index = self.get_value(parameters[1], b)
        else:
            self.index += 3

    def jump_if_non_zero(self, c: int, b: int):
        parameters = self.instructions[self.index + 1:self.index + 3]
        jump_value = self.get_value(parameters[0], c)

        if jump_value != 0:
            self.index = self.get_value(parameters[1], b)
        else:
            self.index += 3

    def less_than(self, c: int, b: int, a: int):
        parameters = self.instructions[self.index + 1:self.index + 4]
        index = self.get_index(parameters[2], a)
        first_value = self.get_value(parameters[0], c)
        second_value = self.get_value(parameters[1], b)

        self.instructions[index] = int(first_value < second_value)

        self.index += 4

    def equal(self, c: int, b: int, a: int):
        parameters = self.instructions[self.index + 1:self.index + 4]
        self.index += 4
        index = self.get_index(parameters[2], a)
        first_value = self.get_value(parameters[0], c)
        second_value = self.get_value(parameters[1], b)

        self.instructions[index] = int(first_value == second_value)

    def add(self, c: int, b: int, a: int):
        parameters = self.instructions[self.index + 1:self.index + 4]
        self.index += 4
        index = self.get_index(parameters[2], a)
        result = (
            self.get_value(parameters[0], c) + self.get_value(parameters[1], b)
        )

        self.instructions[index] = result

    def adjust_relative_base(self, c: int):
        self.index += 1
        parameter = self.instructions[self.index]
        self.index += 1
        self.relative_base += self.get_value(parameter, c)

    def printout(self, param: int):
        if param == 0:
            self.outputs.append(
                str(self.instructions[self.instructions[self.index + 1]])
            )
        elif param == 1:
            self.outputs.append(str(self.instructions[self.index + 1]))
        elif param == 2:
            parameter = self.instructions[self.index + 1]
            self.outputs.append(
                str(self.instructions[self.relative_base + parameter])
            )
        self.index += 2

    def store_input(self, param: int):
        index = self.instructions[self.index + 1]
        if param == InputMode.POSITION:
            pass
        elif param == InputMode.RELATIVE:
            index = self.relative_base + index
        else:
            raise Exception('Wrong mode for input')
        self.instructions[index] = self.input()

    def process(self):
        # print(self.index, self.instructions)
        # print(self.index, end=', ')
        if self.instructions[self.index] == 99:
            self.done = True
            return self.outputs

        instruction = str(self.instructions[self.index]).rjust(5, '0')
        opcode = int(instruction[-2:])
        mode_c = int(instruction[-3])
        mode_b = int(instruction[-4])
        mode_a = int(instruction[-5])
        if opcode == 1:
            self.add(mode_c, mode_b, mode_a)
        elif opcode == 2:
            self.multiply(mode_c, mode_b, mode_a)
        elif opcode == 3:
            self.store_input(mode_c)
            self.index += 2
        elif opcode == 4:
            self.printout(mode_c)
        elif opcode == 5:
            self.jump_if_non_zero(mode_c, mode_b)
        elif opcode == 6:
            self.jump_if_zero(mode_c, mode_b)
        elif opcode == 7:
            self.less_than(mode_c, mode_b, mode_a)
        elif opcode == 8:
            self.equal(mode_c, mode_b, mode_a)
        elif opcode == 9:
            self.adjust_relative_base(mode_c)
        elif opcode == 99:
            self.done = True


def part1(input_):
    execution = Execution(input_, 1)
    while not execution.done:
        execution.process()
    return execution.outputs


def part2(input_):
    execution = Execution(input_, 2)
    while not execution.done:
        execution.process()
    return execution.outputs


def test():
    print(part1(test_input))


if __name__ == '__main__':
    test()
    # import cProfile as profile
    # profile.run('print(part1(task_input))')
    print(part2(task_input))
