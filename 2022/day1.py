from itertools import islice

with open('inputs/day1.txt') as input_file:
    lines = input_file.readlines()

## Part 1

max_ = 0
current = 0
for line in lines:
    if line == '' or line == '\n':
        max_ = max((max_, current))
        current = 0
    else:
        current += int(line)
print(max_)

## Part 2

elves = []
current = 0
for line in lines:
    if line == '' or line == '\n':
        elves.append(current)
        current = 0
    else:
        current += int(line)

print(sum(islice(reversed(sorted(elves)), 3)))
