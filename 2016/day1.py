from collections import Counter, deque
from itertools import cycle
from typing import List


class Grid:
    def __init__(self, instructions: List[str]):
        self.instructions = deque(instructions)
        self.directions = {
            'N': (0, 1),
            'E': (1, 0),
            'W': (-1, 0),
            'S': (0, -1),
        }
        self.current_direction = 'N'
        self.location = (0, 0)

    def turn_right(self):
        turns = {
            'N': 'E',
            'E': 'S',
            'S': 'W',
            'W': 'N'
        }
        self.current_direction = turns[self.current_direction]

    def turn_left(self):
        self.turn_right()
        self.turn_right()
        self.turn_right()

    def follow_instructions(self):
        for instruction in self.instructions:
            if instruction[0] == 'R':
                self.turn_right()
            else:
                self.turn_left()

            number = int(instruction[1:])
            x, y = self.directions[self.current_direction]
            x *= number
            y *= number
            self.location = self.location[0] + x, self.location[1] + y
        return abs(self.location[0]) + abs(self.location[1])

    def find_location(self):
        visited = [(0, 0)]
        for instruction in cycle(self.instructions):
            if instruction[0] == 'R':
                self.turn_right()
            else:
                self.turn_left()

            number = int(instruction[1:])
            x, y = self.directions[self.current_direction]
            for _ in range(number):
                self.location = self.location[0] + x, self.location[1] + y
                if self.location in visited:
                    return abs(self.location[0]) + abs(self.location[1])
                visited.append(self.location)


def part1():
    with open('day1input') as input_file:
        instructions = input_file.readline().replace('\n', '').split(', ')

    grid = Grid(instructions)
    return grid.follow_instructions()


def part2():
    with open('day1input') as input_file:
        instructions = input_file.readline().replace('\n', '').split(', ')
    grid = Grid(instructions)
    return grid.find_location()


if __name__ == "__main__":
    print(part1())
    print(part2())
