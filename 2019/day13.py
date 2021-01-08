from dataclasses import dataclass
from typing import List


@dataclass
class Instruction:
    x: int
    y: int
    tile_id: int

with open('inputs/day13') as input_file:
    task_input = [int(x) for x in input_file.readline().split(',')]
    breakpoint()
    instructions = tuple(Instruction(task_input[0+i], task_input[1+i], task_input[2+i]) for i in range(0, len(task_input)-1, 3))


if __name__ == "__main__":
    print(instructions)
