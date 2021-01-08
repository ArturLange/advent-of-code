from collections import defaultdict, Counter, deque
from typing import Set, List, Dict
from itertools import permutations

with open('inputs/day8') as input_file:
    task_input = [x for x in
                  list(input_file.readline().replace('\n', ''))]

test_input = list('0222112222120000')


# print(task_input)


def part1(input_, size):
    de_input = deque(input_)
    layers = []
    while de_input:
        result = ''
        for i in range(size):
            result += de_input.popleft()
        layers.append(result)
    counts = [Counter(x) for x in layers]
    result_count = Counter(layers[0])
    for count in counts:
        if count['0'] < result_count['0']:
            result_count = count
    print(counts, result_count)
    return result_count['1'] * result_count['2']


def part2(input_, sizes):
    de_input = deque(input_)
    layers = []
    while de_input:
        result = ''
        for i in range(sizes[0] * sizes[1]):
            result += de_input.popleft()
        layers.append(result)
    final_image = [list('2' * sizes[0]) for _ in range(sizes[1])]
    for i in range(sizes[1]):
        for j in range(sizes[0]):
            index = sizes[0] * i + j
            for layer in layers:
                if final_image[i][j] == '2':
                    final_image[i][j] = layer[index]
    print('\n'.join([''.join(line) for line in final_image]))
    return final_image


def test():
    print(part2(test_input, (2, 2)))


if __name__ == '__main__':
    # test()
    # print(part1(task_input, 150))
    print(part2(task_input, (25, 6)))
