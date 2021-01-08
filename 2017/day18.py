import asyncio
import re
import string
from collections import deque
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
        self.name = 'exec'

        self.received = deque()
        self.terminated = False
        self.waiting = False
        self.waiting_time = 0
        self.sending = deque()
        self.receiving_to = None
        self.send_counter = 0
        self.i = 0
        self.other_one = None

    def get_value(self, value):
        try:
            return int(value)
        except ValueError:
            return self.sounds[value]

    def wait_for_value(self):
        while not self.other_one.sending and self.waiting_time < 100:
            self.waiting = True
            asyncio.sleep(0.1)
            self.waiting_time += 1
        if self.waiting_time >= 100:
            self.terminated = True
        self.waiting_time = 0
        self.waiting = False

    async def execute(self):
        while self.i < len(self.operations) and not self.terminated:
            operation = self.operations[self.i]
            if self.snd_re.fullmatch(operation):
                sound = self.snd_re.fullmatch(operation)['sound']
                self.sending.append(self.get_value(sound))
                self.send_counter += 1
            elif self.set_re.fullmatch(operation):
                match = self.set_re.fullmatch(
                    operation)
                sound = match['sound']
                value = match['value']
                self.sounds[sound] = self.get_value(value)
            elif self.add_re.fullmatch(operation):
                match = self.add_re.fullmatch(
                    operation)
                sound = match['sound']
                value = match['value']
                self.sounds[sound] += self.get_value(value)
            elif self.mul_re.fullmatch(operation):
                match = self.mul_re.fullmatch(
                    operation)
                sound = match['sound']
                value = match['value']
                self.sounds[sound] *= self.get_value(value)
            elif self.mod_re.fullmatch(operation):
                match = self.mod_re.fullmatch(
                    operation)
                sound = match['sound']
                value = match['value']
                self.sounds[sound] %= self.get_value(value)
            elif self.jgz_re.fullmatch(operation):
                match = self.jgz_re.fullmatch(
                    operation)
                sound = match['sound']
                value = match['value']
                if self.sounds[sound] > 0:
                    self.i += self.get_value(value)
                    self.i -= 1
            elif self.rcv_re.fullmatch(operation):
                match = self.rcv_re.fullmatch((operation))
                sound = match['sound']
                self.wait_for_value()
                if self.other_one.sending:
                    self.sounds[sound] = self.other_one.sending.popleft()
            self.i += 1
            print(self.i, self.name)


class DoubleExecution:
    def __init__(self, operations):
        ex0 = Execution(operations)
        ex1 = Execution(operations)
        ex0.sounds['p'] = 0
        ex1.sounds['p'] = 1
        ex0.other_one = ex1
        ex1.other_one = ex0
        ex1.name = 'ex1'
        ex0.name = 'ex0'

        self.ex0 = ex0
        self.ex1 = ex1

    def execute(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            asyncio.gather(
                self.ex0.execute(),
                self.ex1.execute()
            )
        )
        loop.close()
        return self.ex1.send_counter


if __name__ == '__main__':
    with open('inputs/day18', 'r') as input_file:
        operations = input_file.readlines()
        operations = [operation.replace('\n', '') for operation in operations]
        # execution = IntcodeExecution(operations)
        # print(execution.execute())
        exec2 = DoubleExecution(operations)
        print(exec2.execute())
