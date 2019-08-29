import string
from collections import deque
from time import sleep
from typing import List


class Program:
    def __init__(self, operations: List[str], id_: int):
        self.operations = operations
        self.id = id_
        self.index = 0

        self.message_queue = deque()
        self.partner: Program = None
        self.waiting = False
        self.terminated = False

        self.send_counter = 0

        self._initialise_registers()

    def _initialise_registers(self):
        self.registers = {x: 0 for x in string.ascii_lowercase}
        self.registers['p'] = self.id

    def get_value(self, key):
        try:
            value = int(key)
            return value
        except ValueError:
            return self.registers[key]

    def send_value(self, value):
        self.send_counter += 1
        self.partner.message_queue.append(value)

    def receive_value(self):
        while not self.message_queue:
            self.waiting = True
            # sleep(1)
            if self.partner.waiting or self.partner.terminated:
                self.partner.terminate()
                self.terminate()
            return
        self.waiting = False
        return self.message_queue.popleft()

    def process_instruction(self, operation: str):
        split_op = operation.split()
        if split_op[0] == 'set':
            self.registers[split_op[1]] = self.get_value(split_op[2])
            self.index += 1
        elif split_op[0] == 'snd':
            self.send_value(self.get_value(split_op[1]))
            self.index += 1
        elif split_op[0] == 'rcv':
            value = self.receive_value()
            if value:
                self.registers[split_op[1]] = value
                self.index += 1
        elif split_op[0] == 'mul':
            self.registers[split_op[1]] *= self.get_value(split_op[2])
            self.index += 1
        elif split_op[0] == 'mod':
            self.registers[split_op[1]] %= self.get_value(split_op[2])
            self.index += 1
        elif split_op[0] == 'add':
            self.registers[split_op[1]] += self.get_value(split_op[2])
            self.index += 1
        elif split_op[0] == 'jgz':
            if self.get_value(split_op[1]) > 0:
                self.index += self.get_value(split_op[2])
            else:
                self.index += 1

    def process_next(self):
        if self.index >= len(self.operations):
            self.terminate()
        else:
            self.process_instruction(self.operations[self.index])

    def terminate(self):
        self.terminated = True


def run_both():
    with open('inputs/day18') as input_file:
        operations = input_file.readlines()
        operations = [operation.replace('\n', '') for operation in operations]

    program0 = Program(operations, 0)
    program1 = Program(operations, 1)
    program0.partner = program1
    program1.partner = program0

    while not program0.terminated or not program1.terminated:
        program0.process_next()
        program1.process_next()

    return program1.send_counter


if __name__ == '__main__':
    print(run_both())
