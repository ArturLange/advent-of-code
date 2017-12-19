from typing import List


class State:

    def __init__(self, instructions: List[str]):

        self.instructions = instructions
        self.values = {}
        self.max_value = 0

    def compare(self, comp_name: str, comp_op: str, comp_value: int) -> bool:
        if comp_op == '>':
            return self.values[comp_name] > comp_value
        if comp_op == '<':
            return self.values[comp_name] < comp_value
        if comp_op == '==':
            return self.values[comp_name] == comp_value
        if comp_op == '!=':
            return self.values[comp_name] != comp_value
        if comp_op == '>=':
            return self.values[comp_name] >= comp_value
        if comp_op == '<=':
            return self.values[comp_name] <= comp_value

    def make_operation(self, name: str, op: str, value: int) -> int:
        if op == 'inc':
            return self.values[name] + value
        if op == 'dec':
            return self.values[name] - value

    def parse_instructions(self):
        for instruction in self.instructions:
            name, op, value, _, comp_name, comp_op, comp_value = instruction.split(' ')
            value = int(value)
            comp_value = int(comp_value)
            if not self.values.get(comp_name):
                self.values[comp_name] = 0
            if not self.values.get(name):
                self.values[name] = 0
            if self.compare(comp_name, comp_op, comp_value):
                self.values[name] = self.make_operation(name, op, value)
            self.max_value = max(list(self.values.values()) + [self.max_value])
        return self.values

    def get_max_value(self):
        return self.max_value


if __name__ == '__main__':
    with open('inputs/day8', 'r') as input_file:
        operations = [line.replace('\n', '') for line in input_file.readlines()]
        state = State(operations)
        print(max(state.parse_instructions().values()))
        print(state.get_max_value())
