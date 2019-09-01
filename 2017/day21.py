from itertools import product
from typing import List

STARTING_PATTERN = '''.#.
..#
###'''


def rotate3(pattern: str):
    return f'{pattern[6]}{pattern[3]}{pattern[0]}{pattern[7]}{pattern[4]}{pattern[1]}{pattern[8]}{pattern[5]}{pattern[2]}'


def rotate2(pattern: str):
    return f'{pattern[2]}{pattern[0]}{pattern[3]}{pattern[1]}'


def rotate3_ntimes(pattern: str, times: int):
    new_pattern = pattern
    for _ in range(times % 4):
        new_pattern = rotate3(new_pattern)
    return new_pattern


def flip3_vert(pattern: str):
    return f'{pattern[2]}{pattern[1]}{pattern[0]}{pattern[5]}{pattern[4]}{pattern[3]}{pattern[8]}{pattern[7]}{pattern[6]}'


def rotates_and_flips3(pattern: str):
    return set((
        pattern,
        rotate3_ntimes(pattern, 1),
        rotate3_ntimes(pattern, 2),
        rotate3_ntimes(pattern, 3),
        flip3_vert(pattern),
        flip3_vert(rotate3_ntimes(pattern, 1)),
        flip3_vert(rotate3_ntimes(pattern, 2)),
        flip3_vert(rotate3_ntimes(pattern, 3)),
    ))


def rotates2(pattern: str):
    return set((
        pattern,
        rotate2(pattern),
        rotate2(rotate2(pattern)),
        rotate2(rotate2(rotate2(pattern))),
    ))


class Pattern2:
    def __init__(self, pattern: str):
        self.pattern = pattern.replace('/', '').replace('\n', '')
        self.size = 2

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return min((
            hash(z) for z in rotates2(self.pattern)
        ))

    def __repr__(self):
        return self.pattern

    def __getitem__(self, index):
        return self.pattern[index]


class Pattern3:
    def __init__(self, pattern: str):
        self.pattern = pattern.replace('/', '').replace('\n', '')
        self.size = 3

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return min((
            hash(z) for z in rotates_and_flips3(self.pattern)
        ))

    def __repr__(self):
        return self.pattern

    def __getitem__(self, index):
        return self.pattern[index]


def get_pixels(iterations: int):
    translate_dict = dict()
    with open('inputs/day21', 'r') as input_file:
        lines = input_file.readlines()
        for line in lines:
            key, value = line.replace('\n', '').split(' => ')
            if len(key) == 5:
                translate_dict[Pattern2(key)] = value
            else:
                translate_dict[Pattern3(key)] = value

    image = [
        STARTING_PATTERN.replace('\n', '')[0:3],
        STARTING_PATTERN.replace('\n', '')[3:6],
        STARTING_PATTERN.replace('\n', '')[6:9],
    ]
    for _ in range(iterations):
        size = len(image)
        if size % 2 == 0:
            dim = size // 2
            parts: List[List[List[str]]] = [
                ['.........'for _ in range(dim)] for _ in range(dim)]
            for i, j in product(range(dim), range(dim)):
                pattern = Pattern2(''.join([
                    image[i*2][j*2],
                    image[i*2][j*2+1],
                    image[i*2+1][j*2],
                    image[i*2+1][j*2+1]
                ]))
                parts[i][j] = translate_dict[pattern].replace('/', '')
            image = []
            for i in range(len(parts)):
                image.append(''.join((x[0:3] for x in parts[i])))
                image.append(''.join((x[3:6] for x in parts[i])))
                image.append(''.join((x[6:9] for x in parts[i])))
        elif size % 3 == 0:
            dim = size // 3
            parts: List[List[List[str]]] = [
                ['................'for _ in range(dim)] for _ in range(dim)]
            for i, j in product(range(dim), range(dim)):
                pattern = Pattern3(''.join([
                    image[i*3][j*3],
                    image[i*3][j*3+1],
                    image[i*3][j*3+2],
                    image[i*3+1][j*3],
                    image[i*3+1][j*3+1],
                    image[i*3+1][j*3+2],
                    image[i*3+2][j*3],
                    image[i*3+2][j*3+1],
                    image[i*3+2][j*3+2],
                ]))
                parts[i][j] = translate_dict[pattern].replace('/', '')
            image = []
            for i in range(len(parts)):
                image.append(''.join((x[0:4] for x in parts[i])))
                image.append(''.join((x[4:8] for x in parts[i])))
                image.append(''.join((x[8:12] for x in parts[i])))
                image.append(''.join((x[12:16] for x in parts[i])))
    return sum((line.count('#') for line in image))


if __name__ == '__main__':
    print(f'Part 1: {get_pixels(5)}')
    print(f'Part 2: {get_pixels(18)}')
