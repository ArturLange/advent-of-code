import asyncio
import re
import string
from queue import Queue, Empty


class Dispatcher:

    def __init__(self, timeout: int or None=None):

        self.timeout = timeout

    _queue0 = Queue()
    _queue1 = Queue()

    def get_queue(self, number: int) -> Queue:
        if number == 0:
            return self._queue0
        elif number == 1:
            return self._queue1
        else:
            raise IndexError

    def add_to_queue(self, element, queue_number: int):
        queue = self.get_queue(queue_number)
        queue.put(element, timeout=self.timeout)

    def get_from_queue(self, queue_number: int):
        queue = self.get_queue(int(not queue_number))
        return queue.get(timeout=self.timeout)


class Execution:
    def __str__(self):
        return f'Execution {self._number}'

    def __init__(self, number: int, operations: list, dispatcher: Dispatcher):
        self.dispatcher = dispatcher
        self._operations = operations
        self._number = number
        self._initialise_registers()

        self.snd_re = re.compile(r'snd (?P<register>[a-z])')
        self.set_re = re.compile(r'set (?P<register>[a-z]) (?P<value>-?[a-z0-9]+)')
        self.add_re = re.compile(r'add (?P<register>[a-z]) (?P<value>-?[a-z0-9]+)')
        self.mul_re = re.compile(r'mul (?P<register>[a-z]) (?P<value>-?[a-z0-9]+)')
        self.mod_re = re.compile(r'mod (?P<register>[a-z]) (?P<value>-?[a-z0-9]+)')
        self.jgz_re = re.compile(r'jgz (?P<register>[a-z]) (?P<value>-?[a-z0-9]+)')
        self.rcv_re = re.compile(r'rcv (?P<register>[a-z])')

        self.line_number = 0

        self.terminated = False

        self.sent_counter = 0
        print(f'{str(self)} initialised')

    def get_value(self, value):
        try:
            return int(value)
        except ValueError:
            return self._registers[value]

    def _initialise_registers(self):
        self._registers = {x: 0 for x in string.ascii_lowercase}
        self._registers['p'] = self._number

    def snd(self, register):
        print(f'{str(self)} sending')
        self.dispatcher.add_to_queue(self._registers[register], self._number)
        print(f'{str(self)} sent')
        self.sent_counter += 1

    def rcv(self, register):
        print(f'{str(self)} receiving')
        try:
            self._registers[register] = self.dispatcher.get_from_queue(self._number)
            print(f'{str(self)} received')
        except Empty:
            self.terminated = True
            print(f'Process {self._number} waited {self.dispatcher.timeout}s - {int(not self._number)} empty')

    def set(self, register, value):
        self._registers[register] = self.get_value(value)

    def add(self, register, value):
        self._registers[register] += self.get_value(value)

    def mul(self, register, value):
        self._registers[register] *= self.get_value(value)

    def mod(self, register, value):
        self._registers[register] %= self.get_value(value)

    def jgz(self, register, value):
        if self._registers[register] > 0:
            self.line_number += self.get_value(value)
            self.line_number -= 1

    async def execute(self):
        while self.line_number < len(self._operations) and not self.terminated:
            operation = self._operations[self.line_number]
            if self.snd_re.fullmatch(operation):
                register = self.snd_re.fullmatch(operation)['register']
                self.snd(register)
            elif self.set_re.fullmatch(operation):
                match = self.set_re.fullmatch(
                    operation)
                register = match['register']
                value = match['value']
                self.set(register, value)
            elif self.add_re.fullmatch(operation):
                match = self.add_re.fullmatch(
                    operation)
                register = match['register']
                value = match['value']
                self.add(register, value)
            elif self.mul_re.fullmatch(operation):
                match = self.mul_re.fullmatch(
                    operation)
                register = match['register']
                value = match['value']
                self.mul(register, value)
            elif self.mod_re.fullmatch(operation):
                match = self.mod_re.fullmatch(
                    operation)
                register = match['register']
                value = match['value']
                self.mod(register, value)
            elif self.jgz_re.fullmatch(operation):
                match = self.jgz_re.fullmatch(
                    operation)
                register = match['register']
                value = match['value']
                self.jgz(register, value)
            elif self.rcv_re.fullmatch(operation):
                match = self.rcv_re.fullmatch((operation))
                register = match['register']
                self.rcv(register)
            self.line_number += 1


def execute_2_processes(operations):
    dispatcher = Dispatcher()
    execution0 = Execution(0, operations, dispatcher)
    execution1 = Execution(1, operations, dispatcher)

    loop = asyncio.get_event_loop()

    loop.run_until_complete(
        asyncio.gather(
            execution0.execute(),
            execution1.execute()
        )
    )
    loop.close()

    print(execution0._registers)
    print(execution1._registers)
    print(execution0.sent_counter)
    print(execution1.sent_counter)


if __name__ == '__main__':
    with open('inputs/day18', 'r') as input_file:
        operations = input_file.readlines()
        operations = [operation.replace('\n', '') for operation in operations]
    execute_2_processes(operations)
