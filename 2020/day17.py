import functools
import itertools
import string
from typing import Any, Dict, List, Set, Tuple


def prod(args):
    return functools.reduce(lambda x, y: x * y, args)


with open('inputs/day17') as input_file:
    input_values = [line.strip() for line in input_file.readlines()]

test_values = ['.#.', '..#', '###']

ACTIVE = '#'
INACTIVE = '.'

Actives = Set[Tuple[int, int, int]]


def get_neighbors(actives: Actives, x: int, y: int, z: int) -> List[bool]:
    result = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                if (i, j, k) in actives:
                    result.append(True)
                else:
                    result.append(False)
    result.remove(((x, y, z) in actives))
    return result


def tick(actives: Actives) -> Set[Tuple[int, int, int]]:
    new_actives = set()
    xs = {x[0] for x in actives}
    ys = {x[1] for x in actives}
    zs = {x[2] for x in actives}
    startx, starty, startz = min(xs) - 1, min(ys) - 1, min(zs) - 1
    stopx, stopy, stopz = max(xs) + 1, max(ys) + 1, max(zs) + 1
    for i in range(startx, stopx + 1):
        for j in range(starty, stopy + 1):
            for k in range(startz, stopz + 1):
                score = get_neighbors(actives, i, j, k).count(True)
                active = (i, j, k) in actives
                if active:
                    if score in (2, 3):
                        new_actives.add((i, j, k))
                else:
                    if score == 3:
                        new_actives.add((i, j, k))
    return new_actives


def part1(input_):
    actives: Set[Tuple[int, int, int]] = set()
    for i, line in enumerate(input_):
        for j, value in enumerate(line):
            if value == ACTIVE:
                actives.add((i, j, 0))
    for _ in range(6):
        actives = tick(actives)
    return len(actives)


Actives2 = Set[Tuple[int, int, int, int]]


def get_neighbors2(actives: Actives2, x: int, y: int, z: int,
                   w: int) -> List[bool]:
    result = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                for l in range(w - 1, w + 2):
                    if (i, j, k, l) in actives:
                        result += 1
    if (x, y, z, w) in actives:
        result -= 1
    return result


def tick2(actives: Actives2) -> Actives2:
    new_actives = set()
    xs = {x[0] for x in actives}
    ys = {x[1] for x in actives}
    zs = {x[2] for x in actives}
    ws = {x[3] for x in actives}
    startx, starty, startz, startw = min(xs) - 1, min(ys) - 1, min(
        zs) - 1, min(ws) - 1
    stopx, stopy, stopz, stopw = max(xs) + 1, max(ys) + 1, max(zs) + 1, max(
        ws) + 1
    for i in range(startx, stopx + 1):
        for j in range(starty, stopy + 1):
            for k in range(startz, stopz + 1):
                for l in range(startw, stopw + 1):
                    score = get_neighbors2(actives, i, j, k, l)
                    active = (i, j, k, l) in actives
                    if active:
                        if score in (2, 3):
                            new_actives.add((i, j, k, l))
                    else:
                        if score == 3:
                            new_actives.add((i, j, k, l))
    return new_actives


def part2(input_):
    actives: Actives2 = set()
    for i, line in enumerate(input_):
        for j, value in enumerate(line):
            if value == ACTIVE:
                actives.add((i, j, 0, 0))
    for _ in range(6):
        actives = tick2(actives)
    return len(actives)


if __name__ == "__main__":
    # print(part1(input_values))
    # print(part2(input_values))

    import cProfile as profile
    profile.run('print(part2(input_values))')
