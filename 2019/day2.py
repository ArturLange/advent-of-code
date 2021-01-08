from itertools import product

with open('inputs/day2') as input_file:
    input_ = [int(x) for x in input_file.readline().split(',')]

test_input = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]

print(input_)


def part1(input_, noun=12, verb=2):
    task_input = list(input_)
    index = 0
    length = len(task_input)

    task_input[1] = noun
    task_input[2] = verb
    # print(task_input)

    while task_input[index] != 99:

        if task_input[index] == 1:
            try:
                task_input[task_input[index + 3]] = (
                    task_input[task_input[index + 1]] +
                    task_input[task_input[index + 2]])
            except IndexError:
                return None
        if task_input[index] == 2:
            try:
                task_input[task_input[index + 3]] = (
                        task_input[task_input[index + 1]] *
                        task_input[task_input[index + 2]])
            except IndexError:
                return None
        # print(task_input)
        index += 4
    return task_input[0]


def part2(task_input):
    length = len(task_input)
    for noun, verb in product(range(1500), range(length)):
        result = part1(task_input, noun, verb)
        # if result:
        print(noun, verb, result)
        if result == 19690720:
            return 100 * noun + verb


# print(part1(input_))
print(part2(input_))
