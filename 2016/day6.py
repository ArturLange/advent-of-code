from collections import Counter


def part1() -> str:
    length = 8
    counters = [Counter() for _ in range(length)]
    with open('day6input') as input_file:
        for line in input_file.readlines():
            for i in range(length):
                counters[i][line[i]] += 1
    common = [x.most_common(1)[0][0] for x in counters]
    return ''.join(common)


def part2() -> str:
    length = 8
    counters = [Counter() for _ in range(length)]
    with open('day6input') as input_file:
        for line in input_file.readlines():
            for i in range(length):
                counters[i][line[i]] += 1
    common = [x.most_common()[-1][0] for x in counters]
    return ''.join(common)


if __name__ == '__main__':
    print(part1())
    print(part2())
