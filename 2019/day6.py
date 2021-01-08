from collections import defaultdict, Counter
from typing import Set, List, Dict

with open('inputs/day6') as input_file:
    task_input = [
        line.replace('\n', '').split(')') for line in input_file.readlines()
    ]

test_input = [
    'COM)B',
    'B)C',
    'C)D',
    'D)E',
    'E)F',
    'B)G',
    'G)H',
    'D)I',
    'E)J',
    'J)K',
    'K)L'
]

test_input = [x.split(')') for x in test_input]

# print(task_input)


class Body:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent: Body = parent
        self.children: Set[Body] = set()

    @property
    def value(self):
        return self.parent.value + 1 if self.parent else 0

    def __repr__(self):
        return f'O({self.name})'


def part1(input_):
    results: Dict[str, Body] = {}
    for orbitted, orbitting in input_:
        if not results.get(orbitted):
            orbitted_body = Body(orbitted)
        else:
            orbitted_body = results[orbitted]
        if not results.get(orbitting):
            orbitting_body = Body(orbitting)
        else:
            orbitting_body = results[orbitting]
        orbitting_body.parent = orbitted_body
        orbitted_body.children.add(orbitting_body)
        results[orbitted] = orbitted_body
        results[orbitting] = orbitting_body
    return sum(x.value for x in results.values())


def part2(input_):
    results: Dict[str, Body] = {}
    for orbitted, orbitting in input_:
        if not results.get(orbitted):
            orbitted_body = Body(orbitted)
        else:
            orbitted_body = results[orbitted]
        if not results.get(orbitting):
            orbitting_body = Body(orbitting)
        else:
            orbitting_body = results[orbitting]
        orbitting_body.parent = orbitted_body
        orbitted_body.children.add(orbitting_body)
        results[orbitted] = orbitted_body
        results[orbitting] = orbitting_body
    orbits_san = []
    orbit = results['SAN']
    while orbit.parent:
        orbit = orbit.parent
        orbits_san.append(orbit)
    orbits_you = []
    orbit = results['YOU']
    while orbit.parent:
        orbit = orbit.parent
        orbits_you.append(orbit)

    common_orbits = []
    for orb in orbits_you:
        if orb in orbits_san:
            common_orbits.append(orb)
    print(common_orbits)

    common_orbit = common_orbits[0]

    count = 0
    current_orbit = results['YOU']
    while current_orbit.parent != common_orbit:
        current_orbit = current_orbit.parent
        count += 1
    current_orbit = results['SAN']
    while current_orbit.parent != common_orbit:
        current_orbit = current_orbit.parent
        count += 1
    return count


def test():
    pass


if __name__ == '__main__':
    test()
    # print(part1(task_input))
    print(part2(task_input))
