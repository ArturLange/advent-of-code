def part1():
    with open('day3input') as input_file:
        triangles = [[int(i) for i in x.split()]
                     for x in input_file.readlines()]
    triangles = list(filter(is_valid_triangle, triangles))
    return len(triangles)


def part2():
    with open('day3input') as input_file:
        triangles = [[int(i) for i in x.split()]
                     for x in input_file.readlines()]
    new_triangles = []

    current = [[], [], []]
    for triangle in triangles:
        current[0].append(triangle[0])
        current[1].append(triangle[1])
        current[2].append(triangle[2])
        if len(current[0]) == 3:
            new_triangles.extend(current)
            current = [[], [], []]

    triangles = list(filter(is_valid_triangle, new_triangles))
    return len(triangles)


def is_valid_triangle(numbers):
    return all([
        numbers[0] + numbers[1] > numbers[2],
        numbers[1] + numbers[2] > numbers[0],
        numbers[2] + numbers[0] > numbers[1]
    ])


if __name__ == "__main__":
    print(part1())
    print(part2())
