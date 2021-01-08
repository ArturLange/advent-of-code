from typing import List

with open('inputs/day1') as input_file:
    values: List[int] = [int(x.replace('\n', '')) for x in input_file.readlines()]

EXPECTED_SUM = 2020

for value in values:
    if EXPECTED_SUM - value in values:
        print(value * (EXPECTED_SUM-value))
        break

import itertools

triples = itertools.combinations(values, 3)
result = next(filter(lambda x: sum(x) == EXPECTED_SUM, triples))

print(result[0]* result[1]*result[2])
