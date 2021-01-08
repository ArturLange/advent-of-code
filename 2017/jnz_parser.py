from collections import defaultdict
from dataclasses import dataclass, field
from typing import Callable, List, Set

STARTING_REGISTERS = {x: 0 for x in 'abcdefgh'}


@dataclass
class Registers:
    __slots__ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    a: int
    b: int
    c: int
    d: int
    e: int
    f: int
    g: int
    h: int

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)


def is_numeric(value: str):
    try:
        int(value)
        return True
    except ValueError:
        return False


class Operation:
    func: Callable
    mutates: Set[str]
    uses: Set[str]

    def __init__(self, op_string: List[str], func: Callable):
        self.func = func
        self.mutates = self.get_mutates(op_string)
        self.uses = self.get_uses(op_string)
        self.instructions: List[str] = [' '.join(op_string).upper()]

    def get_mutates(self, op_string: List[str]) -> Set[str]:
        raise NotImplementedError()

    def get_uses(self, op_string: List[str]) -> Set[str]:
        raise NotImplementedError()

    def __repr__(self):
        return f'Operation func:{self.instructions}, mutates:{self.mutates}, uses:{self.uses}'

    def __add__(self, other):
        def func():
            self.func()
            other.func()
        result = CombinedOperation('', func)
        result.mutates = self.mutates.union(other.mutates)
        result.uses = self.uses.union(other.uses)
        result.instructions = self.instructions + other.instructions
        return result


class SetOperation(Operation):
    def get_mutates(self, op_string: List[str]) -> Set[str]:
        return {op_string[1]}

    def get_uses(self, op_string: List[str]) -> Set[str]:
        if not is_numeric(op_string[2]):
            return {op_string[2]}
        return set()


class SubOperation(Operation):
    def get_mutates(self, op_string: List[str]) -> Set[str]:
        return {op_string[1]}

    def get_uses(self, op_string: List[str]) -> Set[str]:
        if not is_numeric(op_string[2]):
            return {op_string[2]}
        return set()


class MulOperation(Operation):
    def get_mutates(self, op_string: List[str]) -> Set[str]:
        return {op_string[1]}

    def get_uses(self, op_string: List[str]) -> Set[str]:
        if not is_numeric(op_string[2]):
            return {op_string[2]}
        return set()


class JnzOperation(Operation):
    def get_mutates(self, op_string: List[str]) -> Set[str]:
        return set()

    def get_uses(self, op_string: List[str]) -> Set[str]:
        if not is_numeric(op_string[1]):
            return {op_string[1]}
        return set()


class CombinedOperation(Operation):
    def get_mutates(self, op_string):
        pass

    def get_uses(self, op_string):
        pass


class JNZParser:
    __slots__ = [
        'length', 'operations', 'registers',
        'mul_counter', 'counter', 'index'
    ]

    def __init__(self, filename, registers: dict = None):
        starting_registers = dict(STARTING_REGISTERS)
        if registers:
            starting_registers.update(registers)
        with open(filename, 'r') as input_file:
            operations = input_file.readlines()
            operations = [operation.replace('\n', '')
                          for operation in operations]
        self.length = len(operations)
        self.operations: List[Callable] = self.get_operations_from_strings(
            operations)
        self.registers = Registers(**starting_registers)
        self.mul_counter = 0
        self.counter = 0
        self.index = 0

    def get_operations_from_strings(self, strings: List[str]):
        operations = []
        i = 0
        while i < self.length:
            operation = strings[i].split(' ')
            if operation[0] == 'set':
                sound: str = operation[1]
                value: str = operation[2]
                operations.append(self._set_gen(sound, value))
            elif operation[0] == 'sub':
                sound: str = operation[1]
                value: str = operation[2]
                operations.append(self._sub_gen(sound, value))
            elif operation[0] == 'mul':
                sound: str = operation[1]
                value: str = operation[2]
                operations.append(self._mul_gen(sound, value))
            elif operation[0] == 'jnz':
                sound: str = operation[1]
                value: str = operation[2]
                operations.append(self._jnz_gen(sound, value))
            elif operation[0] == 'nop':
                pass
            else:
                raise ValueError
            i += 1
        return operations

    def get_value(self, value):
        try:
            return int(value)
        except ValueError:
            return self.registers[value]

    def _set(self, index: str, value: str):
        self.registers[index] = self.get_value(value)
        self.counter += 1

    def _sub(self, index: str, value: str):
        self.registers[index] -= self.get_value(value)
        self.counter += 1

    def _mul(self, index: str, value: str):
        self.registers[index] *= self.get_value(value)
        self.counter += 1
        self.mul_counter += 1

    def _jnz(self, index: str, value: str):
        if self.get_value(index) != 0:
            self.index += self.get_value(value) - 1
        self.counter += 1

    def _set_gen(self, index: str, value: str):
        def func():
            self._set(index, value)
        return func

    def _sub_gen(self, index: str, value: str):
        def func():
            self._sub(index, value)
        return func

    def _mul_gen(self, index: str, value: str):
        def func():
            self._mul(index, value)
        return func

    def _jnz_gen(self, index: str, value: str):
        def func():
            self._jnz(index, value)
        return func

    def execute(self):
        while self.index < self.length:
            self.operations[self.index]()
            self.index += 1


class SmartParser(JNZParser):
    def get_operations_from_strings(self, strings: List[str]):
        operations: List[Operation] = []
        i = 0
        while i < self.length:
            operation = strings[i].split(' ')
            if operation[0] == 'set':
                sound: str = operation[1]
                value: str = operation[2]
                operations.append(
                    SetOperation(operation, self._set_gen(sound, value))
                )
            elif operation[0] == 'sub':
                sound: str = operation[1]
                value: str = operation[2]
                operations.append(
                    SubOperation(operation, self._sub_gen(sound, value))
                )
            elif operation[0] == 'mul':
                sound: str = operation[1]
                value: str = operation[2]
                operations.append(
                    MulOperation(operation, self._mul_gen(sound, value))
                )
            elif operation[0] == 'jnz':
                sound: str = operation[1]
                value: str = operation[2]
                operations.append(
                    JnzOperation(operation, self._jnz_gen(sound, value))
                )
            elif operation[0] == 'nop':
                pass
            else:
                raise ValueError
            i += 1
        from pprint import pprint
        pprint(operations)
        pprint(operations[0] + operations[1])
        return operations

    def execute(self):
        while self.index < self.length:
            self.operations[self.index].func()
            self.index += 1


if __name__ == "__main__":
    import cProfile as profile
    parser = SmartParser('inputs/day23')
    profile.run('parser.execute()')
    print(parser.mul_counter)

    # parser = SmartParser('inputs/day23', {'a': 1})
    # profile.run('parser.execute()')

    # print(parser.mul_counter)
