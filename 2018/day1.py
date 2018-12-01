from itertools import cycle

def part_1():
    sum_ = 0
    with open('day1_input') as input_file:
        for line in input_file.readlines():
            sum_ += int(line)
    return sum_

def part_2():
    sum_ = 0
    all_numbers = {sum_}
    with open('day1_input') as input_file:
        frequencies = cycle([int(line) for line in input_file.readlines()])
    for number in frequencies:
        sum_ += number
        if sum_ in all_numbers:
            return sum_
        else:
            all_numbers.add(sum_)

print(part_2())

