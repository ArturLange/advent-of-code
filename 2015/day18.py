from typing import List


def get_on_off(char: str) -> bool:
    return True if char == '#' else False


def get_neighbours(x: int, y: int, lights: List[List[bool]]) -> List[bool]:
    last = len(lights) - 1
    result = []
    if x > 0:
        result.append(lights[x-1][y])
        if y > 0:
            result.append(lights[x-1][y-1])
        if y < last:
            result.append(lights[x-1][y+1])
    if x < last:
        result.append(lights[x+1][y])
        if y > 0:
            result.append(lights[x+1][y-1])
        if y < last:
            result.append(lights[x+1][y+1])
    if y > 0:
        result.append(lights[x][y-1])
    if y < last:
        result.append(lights[x][y+1])
    return result


def part1():
    lights = []
    with open('day18input') as input_file:
        for line in input_file.readlines():
            lights.append([get_on_off(x) for x in line])
    for _ in range(100):
        new_lights = []
        for i in range(len(lights)):
            row = []
            for j in range(len(lights)):
                if lights[i][j]:
                    if get_neighbours(i, j, lights).count(True) in (2, 3):
                        row.append(True)
                    else:
                        row.append(False)
                else:
                    if get_neighbours(i, j, lights).count(True) == 3:
                        row.append(True)
                    else:
                        row.append(False)
            new_lights.append(row)
        lights = new_lights
    return sum((row.count(True) for row in lights))


def part2():
    lights = []
    with open('day18input') as input_file:
        for line in input_file.readlines():
            lights.append([get_on_off(x) for x in line])
    last = len(lights) - 1
    lights[0][0] = True
    lights[0][last] = True
    lights[last][0] = True
    lights[last][last] = True
    for _ in range(100):
        new_lights = []
        for i in range(len(lights)):
            row = []
            for j in range(len(lights)):
                if (i, j) in ((0, 0), (0, last), (last, 0), (last, last)):
                    row.append(True)
                elif lights[i][j]:
                    if get_neighbours(i, j, lights).count(True) in (2, 3):
                        row.append(True)
                    else:
                        row.append(False)
                else:
                    if get_neighbours(i, j, lights).count(True) == 3:
                        row.append(True)
                    else:
                        row.append(False)
            new_lights.append(row)
        lights = new_lights
    return sum((row.count(True) for row in lights))


if __name__ == "__main__":
    print(part2())
