import re

pattern_x = r'x=(\d*), y=(\d*)..(\d*)'
pattern_y = r'y=(\d*), x=(\d*)..(\d*)'
clay_x_rx = re.compile(pattern_x)
clay_y_rx = re.compile(pattern_y)

with open('day17_input') as input_file:
    clays = []
    lines = input_file.readlines()
    for line in lines:
        # breakpoint()
        match = clay_x_rx.match(line)
        if match:
            clays.append((
                (int(match.groups()[0])),
                (int(match.groups()[1]), int(match.groups()[2]))
            ))
        else:
            match = clay_y_rx.match(line)
            clays.append((
                (int(match.groups()[1]), int(match.groups()[2])),
                (int(match.groups()[0]))
            ))


def part1():
    print(clays)

part1()
