import itertools
from typing import Any, Dict, List, Set, Tuple

with open('inputs/day5') as input_file:
    input_values= [x.replace('\n', '') for x in input_file.readlines()]
    instructions = [list(line[:]) for line in input_values]


def part1(input_: List[List[str]]):
    return max((get_seat_id(seat_code) for seat_code in input_))

def get_seat_coords(seat_code: List[str]) -> Tuple[int, int]:
    row_numbers = [0, 128]
    col_numbers = [0, 8]
    for letter in seat_code:
        if letter == 'F':
            row_numbers[1] -= (row_numbers[1] - row_numbers[0]) // 2
        if letter == 'B':
            row_numbers[0] += (row_numbers[1] - row_numbers[0]) // 2
        if letter == 'L':
            col_numbers[1] -= (col_numbers[1] - col_numbers[0]) // 2
        if letter == 'R':
            col_numbers[0] += (col_numbers[1] - col_numbers[0]) // 2
    return row_numbers[0], col_numbers[0]

def get_seat_id(seat_code: List[str]) -> int:
    row_number, col_number = get_seat_coords(seat_code)
    return row_number * 8 + col_number

def part2(input_):
    seats_taken: Dict[int, Tuple[int, int]] = {get_seat_id(seat_code): get_seat_coords(seat_code) for seat_code in input_}
    for seat_id, seat_coords in seats_taken.items():
        if seat_id + 1 not in seats_taken:
            seat_row = seat_coords[0] if seat_coords[1] < 7 else seat_coords[0] + 1
            if seat_id + 2 in seats_taken and 0 < seat_row < 128:
                return seat_row, (seat_coords[1] + 1) % 8 
        if seat_id - 1 not in seats_taken:
            seat_row = seat_coords[0] if seat_coords[1] > 0 else seat_coords[0] - 1
            if seat_id - 2 in seats_taken and 0 < seat_row < 128:
                return seat_row, (seat_coords[1] - 1) % 8 


if __name__ == "__main__":
    # print(instructions)
    print(part1(instructions))
    print(part2(instructions))
    row, col = part2(instructions)
    print(row * 8 + col)
