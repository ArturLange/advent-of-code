from itertools import chain

from day10 import hash_list_v2

PUZZLE_INPUT = 'xlqgujun'


def hash_grid(strings):
    used = 0
    for x in range(128):
        string = '-'.join([strings, str(x)])
        row = hash_list_v2(string)
        for cell in row:
            byte = bin(int(cell, 16))[2:]
            used += byte.count('1')
    return used


def hex_to_bin(hex_):
    bin_ = bin(int(hex_, 16))[2:]
    bin_ = '0' * (4 - len(bin_)) + bin_
    return bin_


def get_neighbours_region(x, y, grid):
    neighbours = []
    if x > 0:
        neighbours.append(grid[x - 1][y])
    if y > 0:
        neighbours.append(grid[x][y - 1])
    if x < 127:
        neighbours.append(grid[x + 1][y])
    if y < 127:
        neighbours.append(grid[x][y + 1])
    for neighbour in neighbours:
        if type(neighbour) == int:
            return neighbour
    return None


def get_regions(strings):
    grid = []
    for x in range(128):
        string = '-'.join([strings, str(x)])
        row = hash_list_v2(string)
        grid.append(list(''.join([hex_to_bin(cell) for cell in row]).replace('1', 'x')))
    region_number = 1
    while 'x' in chain.from_iterable(grid):
        x, y = get_first_x(grid)
        create_region(x, y, grid, region_number)
        region_number += 1
    return region_number - 1


def get_first_x(grid):
    for x in range(128):
        for y in range(128):
            if grid[x][y] == 'x':
                return x, y


def create_region(x, y, grid, region_number):
    grid[x][y] = region_number
    if x > 0:
        if grid[x - 1][y] == 'x':
            create_region(x - 1, y, grid, region_number)
    if y > 0:
        if grid[x][y - 1] == 'x':
            create_region(x, y - 1, grid, region_number)
    if x < 127:
        if grid[x + 1][y] == 'x':
            create_region(x + 1, y, grid, region_number)
    if y < 127:
        if grid[x][y + 1] == 'x':
            create_region(x, y + 1, grid, region_number)


if __name__ == '__main__':
    print(hash_grid(PUZZLE_INPUT))
    print(get_regions(PUZZLE_INPUT))
