def count_steps(offset_list_):
    offset_list = list(offset_list_)
    index = 0
    steps = 0
    while True:
        try:
            jump_to = index + offset_list[index]
            offset_list[index] += 1
            index = jump_to
            steps += 1
        except IndexError:
            return steps


def count_steps_v2(offset_list_):
    offset_list = list(offset_list_)
    index = 0
    steps = 0
    while True:
        try:
            jump_to = index + offset_list[index]
            if offset_list[index] >= 3:
                offset_list[index] -= 1
            else:
                offset_list[index] += 1
            index = jump_to
            steps += 1
        except IndexError:
            return steps


if __name__ == '__main__':
    with open('inputs/day5', 'r') as input_file:
        offset_list = [int(line) for line in input_file.readlines()]
        print(count_steps(offset_list))
        print(count_steps_v2(offset_list))
