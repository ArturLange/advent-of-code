from itertools import cycle
from typing import Set, List, Optional
from operator import itemgetter
from arturlib.vectors import Vector
from PIL import Image
import arrow
import time

with open('inputs/day10') as input_file:
    task_input = [line.replace('\n', '') for line in input_file.readlines()]

test_input = [
    '.#..#',
    '.....',
    '#####',
    '....#',
    '...##',
]

test_input_2 = [
    '......#.#.',
    '#..#.#....',
    '..#######.',
    '.#.#.###..',
    '.#..#.....',
    '..#....#.#',
    '#..#....#.',
    '.##.#..###',
    '##...#..#.',
    '.#....####',
]

test_input_3 = [
    '#.#...#.#.',
    '.###....#.',
    '.#....#...',
    '##.#.#.#.#',
    '....#.#.#.',
    '.##..###.#',
    '..#...##..',
    '..##....##',
    '......#...',
    '.####.###.',
]

test_input_4 = [
    '.#..#..###',
    '####.###.#',
    '....###.#.',
    '..###.##.#',
    '##.##.#.#.',
    '....###..#',
    '..#.#..#.#',
    '#..#.#.###',
    '.##...##.#',
    '.....#.#..',
]

test_input_5 = [
    '.#..##.###...#######',
    '##.############..##.',
    '.#.######.########.#',
    '.###.#######.####.#.',
    '#####.##.#.##.###.##',
    '..#####..#.#########',
    '####################',
    '#.####....###.#.#.##',
    '##.#################',
    '#####.##.###..####..',
    '..######..##.#######',
    '####.##.####...##..#',
    '.#####..#.######.###',
    '##...#.##########...',
    '#.##########.#######',
    '.####.#.###.###.#.##',
    '....##.##.###..#####',
    '.#.#.###########.###',
    '#.#.#.#####.####.###',
    '###.##.####.##.#..##',
]


# print(task_input)

class Asteroid:
    def __init__(self, *coords):
        x, y = coords
        resolution = 0.0005
        if abs(x - round(x)) <= resolution:
            x = round(x)
        if abs(y - round(y)) <= resolution:
            y = round(y)
        self.coords = x, y

    def __hash__(self):
        return hash(self.coords)

    def __repr__(self):
        return f'A{self.coords}'

    @property
    def x(self):
        return self.coords[0]

    @property
    def y(self):
        return self.coords[1]

    def __eq__(self, other):
        return self.coords == other.coords

    def __iter__(self):
        return (x for x in self.coords)


class AsteroidField:
    def __init__(self, asteroids_map: List[str]):
        self.asteroids_map = asteroids_map
        asteroids = set()
        for i in range(len(asteroids_map)):
            for j in range(len(asteroids_map[i])):
                if asteroids_map[i][j] == '#':
                    asteroids.add(Asteroid(i, j))
                elif asteroids_map[i][j] != '.':
                    raise ValueError('wrong data')
        self.asteroids: Set[Asteroid] = asteroids
        self.station: Asteroid = self._get_best_station()

    def _get_best_station(self) -> Asteroid:
        # print(sorted(((x, self.can_see_number(x)) for x in self.asteroids), key=lambda x: x[1]))
        station = max(
            ((x, self.can_see_number(x)) for x in self.asteroids),
            key=itemgetter(1)
        )
        return station[0]

    def get_best_station_value(self):
        return self.can_see_number(self.station)

    def can_see_each_other(self, asteroid1: Asteroid,
                           asteroid2: Asteroid):
        # y = ax + b
        x1, y1 = asteroid1.x, asteroid1.y
        x2, y2 = asteroid2.x, asteroid2.y
        if asteroid1 == asteroid2:
            return False
        if x1 - x2 != 0:
            a = (y1 - y2) / (x1 - x2)
            b = y1 - a * x1
            small = min((x2, x1))
            big = max((x2, x1))
            for i in range(round(small) + 1, round(big)):
                ast = Asteroid(i, a * i + b)
                if ast in self.asteroids:
                    return False
            return True
        else:
            small = min((y2, y1))
            big = max((y2, y1))
            for i in range(round(small) + 1, round(big)):
                if (
                    Asteroid(asteroid1.x, i) in self.asteroids and
                    Asteroid(asteroid1.x, i) != asteroid1 and
                    Asteroid(asteroid1.x, i) != asteroid2
                ):
                    return False
            return True

    def can_see_number(self, asteroid: Asteroid):
        seen_asteroids = list(self.can_see_asteroids(asteroid))
        # print(asteroid, seen_asteroids)
        return len(seen_asteroids)

    def can_see_asteroids(self, asteroid: Asteroid):
        return (
            ast for ast in self.asteroids
            if self.can_see_each_other(asteroid, ast)
        )

    def print_asteroid_sight(self, asteroid):
        new_map = [list(line) for line in self.asteroids_map]
        new_map[asteroid.x][
            asteroid.y] = f'\033[1m{new_map[asteroid.x][asteroid.y]}\033[22m'

        seen = {ast for ast in self.asteroids if
                self.can_see_each_other(asteroid, ast)}
        for ast in self.asteroids - seen:
            new_map[ast.x][
                ast.y] = f'\033[31m{new_map[ast.x][ast.y]}\033[0m'
        for ast in seen:
            new_map[ast.x][
                ast.y] = f'\033[32m{new_map[ast.x][ast.y]}\033[0m'

        for line in new_map:
            print(''.join(line))

    def find_angles(self):
        angles = set()
        for asteroid in self.asteroids:
            angles.add(Vector(asteroid.coords).angle)
            angles.add(-Vector(asteroid.coords).angle)
        return angles

    def shoot_angle(self, angle, right_side) -> Optional[Asteroid]:
        if angle == 'up':
            right_side = True
        if angle == 'down':
            right_side = False

        for i in range(1, 26):
            # breakpoint()
            if angle in ['up', 'down']:
                vec = Vector(self.station) + (
                        Vector((0, 1)) * int(right_side) * i)
            else:
                vec = Vector((i, i * angle)) + Vector(self.station)

            if (ast := Asteroid(*vec)) in self.asteroids:
                self.asteroids.remove(ast)
                return ast

    def shoot_asteroids(self, limit: int):
        shot = 0
        angles: Set[Vector] = self.find_angles()
        angles_list = ['up']
        right_side = True
        angles_list.extend(sorted(angles, reverse=True))
        angles_list.append('down')
        angles_list.extend(sorted(angles, reverse=True))
        all_angles = cycle(angles_list)
        shot_asteroid: Asteroid = None
        while shot < limit:
            current_angle = next(all_angles)
            shot_asteroid = self.shoot_angle(current_angle, right_side)
            if shot_asteroid:
                shot += 1
                self.make_image()
            print(shot, current_angle)
        return shot_asteroid

    def make_image(self):
        image_data = [[0 for _ in range(31)] for _ in range(31)]
        for i in range(31):
            for j in range(31):
                if Asteroid(i, j) in self.asteroids:
                    image_data[i][j] = 50
                if Asteroid(i, j) == self.station:
                    image_data[i][j] = 80
        image = Image.frombytes(
            mode='P',
            size=(31, 31),
            data=b''.join((bytes(i) for i in image_data))
        )

        image.save(f'image{arrow.now().timestamp}.png')
        time.sleep(0.1)


def part1(input_):
    asteroid_field = AsteroidField(input_)
    return asteroid_field.get_best_station_value()


def part2(input_):
    asteroid_field = AsteroidField(input_)
    return asteroid_field.shoot_asteroids(200)


def test():
    for input_, expected in (
        (test_input, 8),
        (test_input_2, 33),
        (test_input_3, 35),
        (test_input_4, 41),
        (test_input_5, 210),
    ):
        asteroid_field = AsteroidField(input_)
        asteroid_field.can_see_each_other(Asteroid(0, 1), Asteroid(4, 3))
        print(expected, asteroid_field.get_best_station_value())


if __name__ == '__main__':
    # test()
    # import cProfile as profile
    # profile.run('print(part1(task_input))')
    # print(part1(task_input))
    print(part2(task_input))
