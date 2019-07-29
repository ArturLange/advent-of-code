from collections import Counter
from itertools import chain, combinations


def part1():
    with open('day17input') as input_file:
        containers = list((int(x.replace('\n', ''))
                           for x in input_file.readlines()))
    options = chain(*(
        combinations(containers, x) for x in range(1, len(containers)+1)
    ))
    options = list(filter(lambda x: sum(x) == 150, options))
    return len(options)


def part2():
    with open('day17input') as input_file:
        containers = list((int(x.replace('\n', ''))
                           for x in input_file.readlines()))
    options = chain(*(
        combinations(containers, x) for x in range(1, len(containers)+1)
    ))
    options = filter(lambda x: sum(x) == 150, options)
    lengths = [len(x) for x in options]
    return lengths.count(min(lengths))


if __name__ == "__main__":
    print(part2())
