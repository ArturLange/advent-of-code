from collections import defaultdict, Counter, deque
from typing import Set, List, Dict
from itertools import permutations

with open('inputs/day7') as input_file:
    task_input = [int(x) for x in input_file.readline().split(',')]

test_input = [
    3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55,
    26, 1001, 54,
    -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2,
    53, 55, 53, 4,
    53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10
]


# print(task_input)


class Execution:
    def __init__(self, name: str, input_: List[int],
                 phase_setting: int, input_amp=None, input_value: int = None):
        self.name = name
        self.input_amp: Execution = input_amp
        self.instructions = list(input_)
        self.index = 0
        self.done = False
        self.printed = []
        self.outputs = deque()
        self.inputs = deque()
        self.inputs.append(phase_setting)
        if input_value is not None:
            self.inputs.append(input_value)

    def input(self, index: int):
        # breakpoint()
        # print(f'{self.name} getting input')
        if self.input_amp:
            while self.input_amp.outputs:
                self.inputs.append(self.input_amp.outputs.popleft())
        if self.inputs:
            value = self.inputs.popleft()
            # print(f'{self.name} got input {value}')
            self.instructions[index] = value
            self.index += 2

    def output(self, index: int):
        # print(f'{self.name} outputting {self.instructions[index]}')
        self.outputs.append(self.instructions[index])
        self.index += 2

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
        # breakpoint()
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
        # print(self.name, self.index, self.instructions, self.inputs,
        #       self.outputs)
        if self.done:
            return
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
            if any([c, b, a]):
                raise Exception('Input got parameters')
            self.input(self.instructions[self.index + 1])
        elif opcode == 4:
            if any([c, b, a]):
                raise Exception('output got parameters')
            index = self.instructions[self.index + 1]
            self.output(index)
        elif opcode == 5:
            self.jump_if_non_zero(c, b)
        elif opcode == 6:
            self.jump_if_zero(c, b)
        elif opcode == 7:
            self.less_than(c, b, a)
        elif opcode == 8:
            self.equal(c, b, a)
        elif opcode == 99:
            self.done = True


def try_phase_setting(input_, number: int):
    setting = list(str(number).rjust(5, '0'))
    a = Execution('A', input_=input_, phase_setting=int(setting[0]))
    while not a.done:
        a.process()

    b = Execution('B', input_=input_, phase_setting=int(setting[1]))
    while not b.done:
        b.process()

    c = Execution('C', input_=input_, phase_setting=int(setting[2]))
    while not c.done:
        c.process()

    d = Execution('D', input_=input_, phase_setting=int(setting[3]))
    while not d.done:
        d.process()

    e = Execution('E', input_=input_, phase_setting=int(setting[4]))
    while not e.done:
        e.process()

    return int(e.printed[0])


def try_phase_setting_2(input_, number: int):
    setting = list(str(number).rjust(5, '0'))
    input_signal = 0

    a = Execution(name='A', input_=input_, phase_setting=int(setting[0]),
                  input_value=input_signal)

    b = Execution(name='B', input_=input_, phase_setting=int(setting[1]),
                  input_amp=a)
    c = Execution(name='C', input_=input_, phase_setting=int(setting[2]),
                  input_amp=b)
    d = Execution(name='D', input_=input_, phase_setting=int(setting[3]),
                  input_amp=c)
    e = Execution(name='E', input_=input_, phase_setting=int(setting[4]),
                  input_amp=d)
    a.input_amp = e

    while not all(x.done for x in [a, b, c, d, e]):
        a.process()
        b.process()
        c.process()
        d.process()
        e.process()

    return e.outputs.popleft()


def part1(input_):
    max_signal = 0
    for i in permutations('01234', 5):
        phase = int(''.join(i))
        new = try_phase_setting(input_, phase)
        if new > max_signal:
            max_signal = new
            print(new, i)
    return max_signal


def part2(input_):
    max_signal = 0
    for i in permutations('56789', 5):
        phase = int(''.join(i))
        new = try_phase_setting_2(input_, phase)
        if new > max_signal:
            max_signal = new
            print(new, i)
    return max_signal


def test():
    return part2(test_input)


if __name__ == '__main__':
    # test()
    # print(part1(task_input))
    print(part2(task_input))
