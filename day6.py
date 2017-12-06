from copy import deepcopy


def get_max_and_index(iterable):
    max_ = 0
    index = 0
    for i, element in enumerate(iterable):
        if element > max_:
            max_ = element
            index = i
    return index, max_


def cycle_time(memory_bank):
    count = 0
    state = deepcopy(memory_bank)
    previous_values = [memory_bank]
    while True:
        print(state, previous_values)

        index, value = get_max_and_index(state)
        state[index] = 0

        for i in range(index + 1, len(memory_bank)):
            if value > 0:
                value -= 1
                state[i] += 1

        while value > 0:
            for index in range(len(state)):
                if value > 0:
                    value -= 1
                    state[index] += 1
        count += 1
        print(state, previous_values)

        if state in previous_values:
            return count
        else:
            previous_values.append(deepcopy(state))


if __name__ == '__main__':
    with open('inputs/day6', 'r') as input_file:
        memory_bank = [int(x) for x in input_file.readline().split('\t')]
        print(cycle_time(memory_bank))
