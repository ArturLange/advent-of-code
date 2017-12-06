from itertools import permutations


def checksum(spreadsheet):
    sum_ = 0
    for line in spreadsheet:
        sum_ += max(line) - min(line)
    return sum_


def checksum_v2(spreadsheet):
    sum_ = 0
    for line in spreadsheet:
        for a, b in permutations(line, 2):
            if a % b == 0:
                sum_ += int(a / b)
    return sum_


if __name__ == '__main__':
    with open('inputs/day2', 'r') as input_file:
        spreadsheet = [[int(x) for x in line.split()] for line in input_file.readlines()]
        print(checksum(spreadsheet))
        print(checksum_v2(spreadsheet))
