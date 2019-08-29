from functools import reduce
from itertools import chain, combinations


def part1():
    with open('day24input') as input_file:
        packages = tuple((int(line) for line in input_file.readlines()))

    return get_best_config(packages)


def part2():
    with open('day24input') as input_file:
        packages = tuple((int(line) for line in input_file.readlines()))

    return get_best_config2(packages)


def get_best_config2(packages):
    first_groups = get_smallest_groups2(packages)
    return min((quantum_entanglement(x) for x in first_groups))


def get_best_config(packages):
    first_groups = get_smallest_groups(packages)
    return min((quantum_entanglement(x) for x in first_groups))


def get_smallest_groups2(packages):
    group_weight = sum(packages)//4
    for i in range(len(packages)):
        groups = list(filter(lambda x: sum(x) == group_weight,
                             combinations(packages, i)))
        if groups:
            return groups


def get_smallest_groups(packages):
    group_weight = sum(packages)//3
    for i in range(len(packages)):
        groups = list(filter(lambda x: sum(x) == group_weight,
                             combinations(packages, i)))
        if groups:
            return groups


def quantum_entanglement(group):
    return reduce(lambda x, y: x*y, group)


if __name__ == "__main__":
    print(part1())
    print(part2())
