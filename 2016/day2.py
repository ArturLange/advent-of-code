def part1():
    with open('day2input') as input_file:
        codes = [x.replace('\n', '') for x in input_file.readlines()]
    door_code = ''
    number = 5
    for line in codes:
        for dir_ in line:
            number = move(number, dir_)
        door_code += str(number)
    return door_code


def part2():
    with open('day2input') as input_file:
        codes = [x.replace('\n', '') for x in input_file.readlines()]
    door_code = ''
    char = '5'
    for line in codes:
        for dir_ in line:
            char = move2(char, dir_)
        door_code += char
    return door_code


def move(number: int, direction: str):
    if direction == 'U':
        if number > 3:
            return number - 3
    if direction == 'D':
        if number < 7:
            return number + 3
    if direction == 'R':
        if number % 3 != 0:
            return number + 1
    if direction == 'L':
        if number % 3 != 1:
            return number - 1
    return number


UPS = {
    'A': '6', 'B': '7', 'C': '8', 'D': 'B', '3': '1'
}

DOWNS = {
    '1': '3', '6': 'A', '7': 'B', '8': 'C', 'B': 'D'
}

LEFTS = {
    'C': "B", "B": "A"
}

RIGHTS = {
    "A": "B", "B": "C"
}


def move2(char: str, direction: str):
    if direction == 'U':
        if char in '12459':
            return char
        elif char in '678':
            return str(int(char)-4)
        else:
            return UPS[char]
    if direction == 'D':
        if char in '5ADC9':
            return char
        elif char in '234':
            return str(int(char)+4)
        else:
            return DOWNS[char]
    if direction == 'L':
        if char in '125AD':
            return char
        elif char in '346789':
            return str(int(char)-1)
        else:
            return LEFTS[char]
    if direction == 'R':
        if char in '149CD':
            return char
        elif char in '235678':
            return str(int(char)+1)
        else:
            return RIGHTS[char]
    return char


if __name__ == "__main__":
    print(part1())
    print(part2())
