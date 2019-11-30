from collections import deque
from typing import List, Sequence, Deque

with open('day8_input') as input_file:
    numbers = [int(i) for i in input_file.read().split()]


class Node:
    def __init__(self, numbers: Deque[int], result: dict):
        self.result = result
        self.numbers = numbers
        self.child_nodes_count = self.numbers.popleft()
        self.metadata_count = self.numbers.popleft()
        self.children: List[Node] = []

        self.init_children()

        self.metadata = list([self.numbers.popleft() for _ in range(self.metadata_count)])
        self.result['metadata_sum'] += sum(self.metadata)


    @property
    def value(self) -> int:
        if not self.children:
            return sum(self.metadata)
        else:
            result = 0
            for index in self.metadata:
                try:
                    result += self.children[index - 1].value
                except IndexError:
                    pass
            return result

    def init_children(self):
        for _ in range(self.child_nodes_count):
            self.children.append(Node(self.numbers, self.result))

    def __str__(self):
        return f'Node with {self.child_nodes_count} child nodes, {self.metadata_count} metadata ({self.metadata}, value={self.value})'


def part1(numbers):
    result = {'metadata_sum': 0}
    numbers = deque(numbers)
    node = Node(numbers, result)
    return result['metadata_sum']


def part2(numbers):
    result = {'metadata_sum': 0}
    numbers = deque(numbers)
    node = Node(numbers, result)
    return node.value


test_numbers = [int(i) for i in '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split()]

print(part1(test_numbers))
print(part1(numbers))
print(part2(numbers))
# result = {'metadata_sum': 0}
# node = Node(test_numbers, result)
# print(node, result)
