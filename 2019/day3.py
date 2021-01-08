from collections import defaultdict, Counter
from typing import Set, List, Dict

with open('inputs/day3') as input_file:
    task_input = [y.replace('\n', '').split(',') for y in
                  [line for line in input_file.readlines()]]

test_input = [
    ['R8', 'U5', 'L5', 'D3'],
    ['U7', 'R6', 'D4', 'L4']
]

# print(task_input)

dirs = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}


def distance(location):
    return abs(location[0]) + abs(location[1])


def part1(input_):
    visited = set()
    intersections = set()
    for wire in input_:
        new_visited = set()
        location = (0, 0)
        for coords in wire:
            dir = dirs[coords[0]]
            length = int(coords[1:])
            for _ in range(length):
                location = location[0] + dir[0], location[1] + dir[1]
                if location in visited:
                    # breakpoint()
                    intersections.add(location)
                new_visited.add(location)
        visited = visited.union(new_visited)
    print(intersections)
    return min((distance(x) for x in intersections))


def part2(input_):
    visited: List[Dict] = []
    for wire in input_:
        steps = 0
        new_visited = dict()
        location = (0, 0)
        for coords in wire:
            dir_ = dirs[coords[0]]
            length = int(coords[1:])
            for _ in range(length):
                steps += 1
                location = location[0] + dir_[0], location[1] + dir_[1]
                if location in new_visited:
                    new_visited[location] = min((steps, new_visited[location]))
                else:
                    new_visited[location] = steps
        visited.append(new_visited)
    intersections = set()
    counts = Counter()
    for i in range(len(visited)):
        counts += Counter(visited[i].keys())
    counts = {x: y for x, y in dict(counts).items() if y > 1}
    for i in range(len(visited)):
        visited[i] = {x: visited[i][x] for x in visited[i] if x in counts}
    for i in range(len(visited)):
        others = list(filter(lambda x: x is not visited[i], visited))
        for location, value in visited[i].items():
            intersections.add(value + min(other[location] for other in others))
    print(intersections)

    return min(intersections)


if __name__ == '__main__':
    # print(part1(task_input))
    print(part2(task_input))
