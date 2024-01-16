import string
import itertools

with open('inputs/day3.txt') as input_file:
    lines = tuple(line.strip() for line in input_file.readlines())

def get_item_priority(letter: str) -> int:
    return string.ascii_letters.index(letter) + 1

def split_rucksack(items: str) -> tuple[set[str], set[str]]:
    return (
        set(items[0:len(items)//2]),
        set(items[len(items)//2:len(items)]),
    )

## Part 1
priorities_sum = 0

for line in lines:
    compartments: tuple[set[str], set[str]] = split_rucksack(line)
    common_item = (compartments[0] & compartments[1]).pop()
    priorities_sum += get_item_priority(common_item)

print(priorities_sum)
## Part 2

badges_sum = 0

for group in itertools.batched(lines, 3):
    group_sets = tuple(set(g) for g in group)
    possible_badges = group_sets[0] & group_sets[1] & group_sets[2]
    badge = possible_badges.pop()
    badges_sum += get_item_priority(badge)

print(badges_sum)