from collections import Counter

lines = []
with open('day2_input') as input_file:
        for line in input_file.readlines():
            lines.append(line)

def part_1():

    multipliers = [0] * max(len(line) for line in lines)

    for line in lines:
        counter = Counter(line)
        for i in range(2, len(line)+1):
            if i in counter.values():
                multipliers[i] += 1

    print(multipliers)
    product = 1
    for i in multipliers:
        if i != 0:
            product = product * i
    print(product)

# part_1()

def part_2():
    common = ''
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            new_common = ''
            for k in range(len(lines[i])):
                if lines[i][k] == lines[j][k]:
                    new_common += lines[i][k]
            if len(new_common) > len(common):
                common = new_common
    return common

print(part_2())

