from collections import defaultdict, Counter
from typing import Set, List, Dict

with open('inputs/day5') as input_file:
    task_input = [int(x) for x in input_file.readline().split(',')]

test_input = [
    ['R8', 'U5', 'L5', 'D3'],
    ['U7', 'R6', 'D4', 'L4']
]


# print(task_input)


class Execution:
    def __init__(self, input_: List[int], input_value: int):
        self.input_value = input_value
        self.instructions = input_
        self.index = 0
        self.done = False
        self.printed = []

    def input(self):
        return self.input_value

    def multiply(self, c: int, b: int, a: int):
        result = 1
        self.index += 1
        parameters = self.instructions[self.index:self.index + 3]
        self.index += 3
        if a == 1:
            raise TypeError('a in immediate mode')
        if c == 0:
            result *= self.instructions[parameters[0]]
        elif c == 1:
            result *= parameters[0]
        if b == 0:
            result *= self.instructions[parameters[1]]
        elif b == 1:
            result *= parameters[1]

        self.instructions[parameters[2]] = result

    def jump_if_zero(self, c: int, b: int):
        # breakpoint()
        parameters = self.instructions[self.index + 1:self.index + 3]
        jump_value = 1
        if c == 0:
            jump_value = self.instructions[parameters[0]]
        elif c == 1:
            jump_value = parameters[0]

        if jump_value == 0 and b == 0:
            self.index = self.instructions[parameters[1]]
        elif jump_value == 0 and b == 1:
            self.index = parameters[1]

        if jump_value != 0:
            self.index += 3

    def jump_if_non_zero(self, c: int, b: int):
        parameters = self.instructions[self.index + 1:self.index + 3]
        jump_value = 0
        if c == 0:
            jump_value = self.instructions[parameters[0]]
        elif c == 1:
            jump_value = parameters[0]

        if jump_value != 0 and b == 0:
            self.index = self.instructions[parameters[1]]
        elif jump_value != 0 and b == 1:
            self.index = parameters[1]

        if jump_value == 0:
            self.index += 3

    def less_than(self, c: int, b: int, a: int):
        self.index += 1
        parameters = self.instructions[self.index:self.index + 3]
        self.index += 3
        if a == 1:
            raise TypeError('a in immediate mode')
        if c == 0:
            first_value = self.instructions[parameters[0]]
        else:
            first_value = parameters[0]
        if b == 0:
            second_value = self.instructions[parameters[1]]
        else:
            second_value = parameters[1]

        self.instructions[parameters[2]] = int(first_value < second_value)

    def equal(self, c: int, b: int, a: int):
        self.index += 1
        parameters = self.instructions[self.index:self.index + 3]
        self.index += 3
        if a == 1:
            raise TypeError('a in immediate mode')
        if c == 0:
            first_value = self.instructions[parameters[0]]
        else:
            first_value = parameters[0]
        if b == 0:
            second_value = self.instructions[parameters[1]]
        else:
            second_value = parameters[1]

        self.instructions[parameters[2]] = int(first_value == second_value)

    def add(self, c: int, b: int, a: int):
        # breakpoint()
        result = 0
        self.index += 1
        parameters = self.instructions[self.index:self.index + 3]
        self.index += 3
        if a == 1:
            raise TypeError('a in immediate mode')
        if c == 0:
            result += self.instructions[parameters[0]]
        elif c == 1:
            result += parameters[0]
        if b == 0:
            result += self.instructions[parameters[1]]
        elif b == 1:
            result += parameters[1]

        self.instructions[parameters[2]] = result

    def printout(self, param: int):
        if param == 0:
            self.printed.append(
                str(self.instructions[self.instructions[self.index + 1]])
            )
        elif param == 1:
            self.printed.append(str(self.instructions[self.index + 1]))
        self.index += 2

    def process(self):
        print(self.index, self.instructions)
        if self.instructions[self.index] == 99:
            self.done = True
            return self.printed

        instruction = str(self.instructions[self.index]).rjust(5, '0')
        opcode = int(instruction[-2:])
        c = int(instruction[-3])
        b = int(instruction[-4])
        a = int(instruction[-5])
        if opcode == 1:
            self.add(c, b, a)
        elif opcode == 2:
            self.multiply(c, b, a)
        elif opcode == 3:
            result = self.input()
            self.instructions[self.instructions[self.index + 1]] = result
            self.index += 2
        elif opcode == 4:
            self.printout(c)
        elif opcode == 5:
            self.jump_if_non_zero(c, b)
        elif opcode == 6:
            self.jump_if_zero(c, b)
        elif opcode == 7:
            self.less_than(c, b, a)
        elif opcode == 8:
            self.equal(c, b, a)


def part1(input_):
    exec_ = Execution(input_, 1)
    print(len(exec_.instructions))
    while not exec_.done:
        exec_.process()
    return exec_.printed


def part2(input_):
    exec_ = Execution(input_, 5)
    print(len(exec_.instructions))
    while not exec_.done:
        exec_.process()
    return exec_.printed


def test():
    input_ = [1002, 4, 3, 4, 33]
    exec_ = Execution(input_, 1)
    print(exec_.instructions)
    while not exec_.done:
        exec_.process()
    print(exec_.instructions)


if __name__ == '__main__':
    # test()
    # print(part1(task_input))
    print(part2(task_input))
