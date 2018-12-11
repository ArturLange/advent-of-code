from collections import deque

with open('day8_input') as input_file:
    numbers =  [int(i) for i in input_file.read().split()]

class Node:
    def __init__(self, numbers):
        numbers = deque(numbers)
        self.child_nodes_count = numbers.popleft()
        self.children = []
        self.metadata_count = numbers.popleft()
        self.metadata = list(reversed([numbers.pop() for _ in range(self.metadata_count)]))
        self.numbers = numbers

    def __str__(self):
        return f'Node with {self.child_nodes_count} child nodes, {self.metadata_count} metadata ({self.metadata}) and content = {list(self.numbers)}'

def part1(numbers):
    numbers = list(numbers)
    tree = {}
    while numbers:
        child_nodes = numbers.pop(0)
        number_of_metadata = numbers.pop(0)
        if not tree:
            tree['children'] = parse_nodes(numbers, child_nodes)
        if not child_nodes:
            metadata_sum += sum([numbers.pop(0) for _ in range(number_of_metadata)])
        else:
            metadata_sum += sum([numbers.pop(-1) for _ in range(number_of_metadata)])
    return metadata_sum

def sum_metadata(numbers: list, nodes=0):
    metadata_sum = 0
    while numbers:
        if len(numbers) == 1:
            breakpoint()
        child_nodes = numbers.pop(0)
        number_of_metadata = numbers.pop(0)
        if not child_nodes:
            metadata_sum += sum([numbers.pop(0) for _ in range(number_of_metadata)])
        else:
            metadata_sum += sum([numbers.pop(-1) for _ in range(number_of_metadata)])
    return metadata_sum



def part2(lines):
    pass


test_numbers = [int(i) for i in '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split()]

# print(part1(test_numbers))
# print(part1(numbers))

node = Node(test_numbers)
print(node)
