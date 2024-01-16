import string
import itertools

with open('inputs/day4.txt') as input_file:
    lines = tuple(line.strip() for line in input_file.readlines())
    pairs_assignments = tuple(line.split(',')for line in lines)

def range_to_set(range_: str) -> set[int]:
    start, end = (int(x) for x in range_.split('-'))
    return set(range(start, end + 1))

pairs_sets = tuple((range_to_set(pair[0]), range_to_set(pair[1])) for pair in pairs_assignments)

## Part 1

containing_pairs = tuple(pair for pair in pairs_sets if pair[0] <= pair[1] or pair[0] >= pair[1])
print(len(containing_pairs))

## Part 2

overlapping_pairs = tuple(pair for pair in pairs_sets if not pair[0].isdisjoint(pair[1]))
print(len(overlapping_pairs))