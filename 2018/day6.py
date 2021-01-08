from collections import Counter
from pprint import pprint

with open('day6_input') as input_file:
    lines = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in input_file.readlines()]

def distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def part1(coords_list, max_range=400):
    space = [['.' for _ in range(max_range)] for _ in range(max_range)]
    for i in range(len(space)):
        for j in range(len(space[0])):
            distances = []
            for index in range(len(coords_list)):
                distances.append(distance((j, i), coords_list[index]))
            sorted_distances = sorted([(i, distances[i]) for i in range(len(distances))], key=lambda x: x[1])
            if sorted_distances[0][1] != sorted_distances[1][1]:
                space[i][j] = sorted_distances[0][0]
        
    counts = Counter((item for line in space for item in line))
    print(counts)
    for i in range(len(space)):
        counts.pop(space[i][0], None)
        counts.pop(space[i][-1], None)
    for j in range(len(space[0])):
        counts.pop(space[0][j], None)
        counts.pop(space[-1][j], None)
    print(counts)
    pprint(space)
    return max(counts.values())


def part2(coords_list, limit=10000, max_range=400):
    space = [['.' for _ in range(max_range)] for _ in range(max_range)]
    region_size = 0
    for i in range(len(space)):
        for j in range(len(space[0])):
            if sum((distance((j,i), coord) for coord in coords_list)) < limit:
                region_size += 1
    return region_size

coords_list = [
    (1, 1),
    (1, 6),
    (8, 3),
    (3, 4),
    (5, 5),
    (8, 9)
]
# print(part1(coords_list, 10))
print(part2(lines))
