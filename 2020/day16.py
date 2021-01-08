import functools
import itertools
import string
from typing import Any, Dict, Iterable, List, Set, Tuple


def prod(args):
    return functools.reduce(lambda x, y: x * y, args)


with open('inputs/day16') as input_file:
    input_values = [line.strip() for line in input_file.readlines()]
    valid_values = set()

    index = 0
    field_names: Dict[str, Set[int]] = {}
    line = input_values[index]
    while line != '':
        key, ranges = line.split(': ')
        field_names[key] = set()
        range1, range2 = ranges.split(' or ')
        for r in (range1, range2):
            start, stop = (int(x) for x in r.split('-'))
            field_names[key] |= set(range(start, stop + 1))
            valid_values |= set(range(start, stop + 1))
        index += 1
        line = input_values[index]
    index += 2
    your_ticket = tuple(int(i) for i in input_values[index].split(','))
    index += 3

    tickets = set()
    line = input_values[index]
    while line != '':
        tickets.add(tuple(int(value) for value in line.split(',')))
        index += 1
        if index < len(input_values):
            line = input_values[index]
        else:
            line = ''


def part1(valid_numbers: Set, tickets: Set[tuple]):
    result = 0
    for ticket in tickets:
        for value in ticket:
            if value not in valid_numbers:
                result += value
    return result


def is_ticket_valid(valid_numbers: Set, ticket: Tuple[int]):
    for value in ticket:
        if value not in valid_numbers:
            return False
    return True


def part2(tickets: Iterable[Tuple[int]], my_ticket: Tuple[int],
          field_names: Dict[str, Set[int]]):
    header_row = [set(field_names.keys())] * len(my_ticket)
    for ticket in tickets:
        for index, value in enumerate(ticket):
            header_row[index] = set(
                filter(lambda x: value in field_names[x], header_row[index]))
    for _ in range(len(header_row)):
        for header in header_row:
            if len(header) == 1:
                for value in header_row:
                    if value != header:
                        value -= header
    headers_departure = (index for index, header in enumerate(header_row)
                         if tuple(header)[0].startswith('departure'))
    values = tuple(my_ticket[index] for index in headers_departure)
    return prod(values)


if __name__ == "__main__":
    print(part1(valid_values, tickets))
    tickets = filter(lambda x: is_ticket_valid(valid_values, x), tickets)
    print(part2(tickets, your_ticket, field_names))
