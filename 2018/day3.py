with open('day3_input') as input_file:
    lines = input_file.readlines()


def part1():
    fabric = [list([0]* 1000) for _ in range(1000)]
    for line in lines:
        data = line.split()
        start = data[2].split(',')
        start = int(start[0]), int(start[1][:-1])
        size = [int(x) for x in data[3].split('x')]
        for i in range(size[1]):
            for j in range(size[0]):
                fabric[start[1] + i][start[0]+ j] += 1

    return sum(
        len([x for x in line if x >= 2]) 
        for line in fabric
    )



def part2():
    fabric = [list([0]* 1000) for _ in range(1000)]
    for line in lines:
        data = line.split()
        number = int(data[0][1:])
        start = data[2].split(',')
        start = int(start[0]), int(start[1][:-1])
        size = [int(x) for x in data[3].split('x')]
        for i in range(size[1]):
            for j in range(size[0]):
                field = fabric[start[1] + i][start[0]+ j]
                if field == 0:
                    fabric[start[1] + i][start[0]+ j] = number
                else:
                    fabric[start[1] + i][start[0]+ j] = 'x'
    for line in lines:
        data = line.split()
        number = int(data[0][1:])
        size = [int(x) for x in data[3].split('x')]
        count = sum(
            len([x for x in line if x == number]) 
            for line in fabric
        )
        if count == size[0] * size[1]:
            return number


print(part2())
