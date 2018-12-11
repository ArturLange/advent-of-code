from itertools import product

GRID_SERIAL_NUMBER = 7857

def get_power(x, y, serial_number):
        rack_id = x + 10
        power_level = (rack_id * y + serial_number) * rack_id
        return int(str(power_level)[-3]) - 5

def part1(serial_number):
    return max(
        (
            (
                x,
                y,
                sum((get_power(x+i, y+j, serial_number) for i, j in product(list(range(3)), list(range(3)))))
            )
            for x in range(300-2) for y in range(300 -2)
        ),
        key=lambda x: x[2]
    )

def part2(serial_number):
    return max(
        (
            (
                x,
                y,
                sum((get_power(x+i, y+j, serial_number) for i, j in product(list(range(size)), list(range(size))))),
                size
            )
            for size in range(1, 5) for x in range(300-size+1) for y in range(300 -size+1)
        ),
        key=lambda x: x[2]
    )


assert get_power(3, 5, 8) == 4
assert get_power(122, 79, 57) == -5


print(part2(GRID_SERIAL_NUMBER))
