from typing import Tuple

STARTING_REGISTERS = {
    'a': 0,
    'b': 0
}


class Computer:
    def __init__(self, instructions: Tuple[str], starting_registers: dict = STARTING_REGISTERS):
        self.instructions = instructions
        self.registers = starting_registers
        self.index = 0
        self.length = len(self.instructions)

    def execute(self):
        instruction = self.instructions[self.index].replace(',', '').split()
        if instruction[0] == 'hlf':
            self.registers[instruction[1]] //= 2
            self.index += 1
        elif instruction[0] == 'tpl':
            self.registers[instruction[1]] *= 3
            self.index += 1
        elif instruction[0] == 'inc':
            self.registers[instruction[1]] += 1
            self.index += 1
        elif instruction[0] == 'jmp':
            self.index += int(instruction[1])
        elif instruction[0] == 'jie':
            if self.registers[instruction[1]] % 2 == 0:
                self.index += int(instruction[2])
            else:
                self.index += 1
        elif instruction[0] == 'jio':
            if self.registers[instruction[1]] == 1:
                self.index += int(instruction[2])
            else:
                self.index += 1

    def get_registers(self):
        while self.index < self.length:
            self.execute()
        return self.registers


def part1():
    with open('day23input') as input_file:
        instructions = tuple((line.replace('\n', '')
                              for line in input_file.readlines()))

    computer = Computer(instructions)
    return computer.get_registers()


def part2():
    with open('day23input') as input_file:
        instructions = tuple((line.replace('\n', '')
                              for line in input_file.readlines()))

    computer = Computer(instructions, {'a': 1, 'b': 0})
    return computer.get_registers()


if __name__ == "__main__":
    print(part2())
