from typing import Tuple, Iterable, List, Set

from itertools import combinations


class Moon:
    name: str
    __slots__ = ['name', 'x', 'y', 'z', 'vx', 'vy', 'vz']

    def __init__(self, name: str, position: Tuple[int, int, int]):
        self.name = name
        self.x, self.y, self.z = position
        self.vx, self.vy, self.vz = (0, 0, 0)

    @property
    def position(self):
        return self.x, self.y, self.z

    @property
    def velocity(self):
        return self.vx, self.vy, self.vz

    def __str__(self):
        x = self.x, self.vx
        y = self.y, self.vy
        z = self.z, self.vz
        return (f'pos=<x={x[0]}, y={y[0]}, z={z[0]}>, '
                f'vel=<x={x[1]}, y={y[1]}, z={z[1]}>')

    def __repr__(self):
        return self.name


def make_step(moons: Iterable[Moon]):
    moon_combinations = list(combinations(moons, r=2))
    for moon1, moon2 in moon_combinations:
        if moon1.x < moon2.x:
            moon1.vx += 1
            moon2.vx -= 1
        elif moon1.x > moon2.x:
            moon1.vx -= 1
            moon2.vx += 1
        if moon1.y < moon2.y:
            moon1.vy += 1
            moon2.vy -= 1
        elif moon1.y > moon2.y:
            moon1.vy -= 1
            moon2.vy += 1
        if moon1.z < moon2.z:
            moon1.vz += 1
            moon2.vz -= 1
        elif moon1.z > moon2.z:
            moon1.vz -= 1
            moon2.vz += 1
    for moon in moons:
        moon.x += moon.vx
        moon.y += moon.vy
        moon.z += moon.vz


def get_energy(moons: Iterable[Moon]):
    return sum(
        sum(abs(x) for x in moon.position) * sum(abs(x) for x in moon.velocity)
        for moon in moons
    )


def part1():
    moons: Set[Moon] = {
        Moon('Io', (16, -8, 13)),
        Moon('Europa', (4, 10, 10)),
        Moon('Ganymede', (17, -5, 6)),
        Moon('Callisto', (13, -3, 0)),
    }
    for _ in range(1000):
        make_step(moons)

    return get_energy(moons)


def test():
    moons: List[Moon] = [
        Moon('Io', (-1, 0, 2)),
        Moon('Europa', (2, -10, -7)),
        Moon('Ganymede', (4, -8, 8)),
        Moon('Callisto', (3, 5, -1)),
    ]
    for moon in moons:
        print(moon)
    print()
    for _ in range(10):
        make_step(moons)
        for moon in moons:
            print(moon)
        print()

    return get_energy(moons)


def part2():
    starting_state = (
        (16, -8, 13),
        (4, 10, 10),
        (17, -5, 6),
        (13, -3, 0)
    )
    steps = 0
    moons: Set[Moon] = {
        Moon('Io', (16, -8, 13)),
        Moon('Europa', (4, 10, 10)),
        Moon('Ganymede', (17, -5, 6)),
        Moon('Callisto', (13, -3, 0)),
    }
    make_step(moons)
    positions = set(moon.position for moon in moons)
    while positions != starting_state or set(
            moon.velocity for moon in moons) != {(0, 0, 0)}:
        steps += 1
        make_step(moons)
        if steps % 100000 == 0:
            print(steps)
        positions = set(moon.position for moon in moons)


def test2():
    starting_state = {
        (-1, 0, 2),
        (2, -10, -7),
        (4, -8, 8),
        (3, 5, -1)
    }
    steps = 1
    moons: Set[Moon] = {
        Moon('Io', (-1, 0, 2)),
        Moon('Europa', (2, -10, -7)),
        Moon('Ganymede', (4, -8, 8)),
        Moon('Callisto', (3, 5, -1)),
    }

    make_step(moons)
    positions = set(tuple(moon.position) for moon in moons)
    while positions != starting_state or set(
        tuple(moon.velocity) for moon in moons) != {(0, 0, 0)}:
        steps += 1
        make_step(moons)
        # print(steps)
        positions = set(tuple(moon.position) for moon in moons)

    return steps


if __name__ == '__main__':
    # print(test2())
    import cProfile as profile

    profile.run('print(part2())')
    # print(part2())
