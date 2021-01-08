from typing import Set, List

with open('day13_input') as input_file:
    railmap: List[List[str]] = []
    for row in [line.replace('\n', '') for line in input_file.readlines()]:
        railmap.append(list(row))

TEST_INPUT = '''
/->-\\        
|   |  /----\\
| /-+--+-\\  |
| | |  | v  |
\\-+-/  \\-+--/
  \\------/   
'''

test_railmap = []
print(TEST_INPUT.split('\n')[1:-1])



class Vector:
    value: tuple

    def __init__(self, *values):
        self.value = tuple(values)
        self.length = len(self.value)

    def __len__(self) -> int:
        return self.length

    def __add__(self, other):
        if len(self) != len(other):
            raise TypeError('Vectors have incompatible lengths')
        return Vector(*(self.value[i] + other.value[i] for i in range(len(self))))

    def __str__(self):
        return f'Vector({self.value})'

    def __repr__(self):
        return str(self)

    def __getitem__(self, item):
        return self.value[item]


class Cart:
    directions: List[Vector] = [
        Vector(1, 0),
        Vector(0, 1),
        Vector(-1, 0),
        Vector(0, -1)
    ]

    def __repr__(self):
        return f'Cart({self.location=}, {self.direction=})'

    def __init__(self, location: Vector, direction: Vector):
        self.location = location
        self.direction = direction
        self.turns = 0

    def make_a_turn(self):
        self.turns %= 3
        if self.turns == 0:
            self.turn_left()
        elif self.turns == 1:
            pass
        elif self.turns == 2:
            self.turn_right()
        self.turns += 1

    def turn_right(self):
        index = self.directions.index(self.direction)
        index = (index + 1) % 4
        self.direction = self.directions[index]

    def turn_left(self):
        index = self.directions.index(self.direction)
        index = (index + 3) % 4
        self.direction = self.directions[index]

    def turn_back(self):
        index = self.directions.index(self.direction)
        index = (index + 2) % 4
        self.direction = self.directions[index]

    def move_forward(self):
        self.location += self.direction


def cart_sort(cart: Cart):
    return 1000 * cart.location[0] + cart.location[1]


UP = Vector(-1, 0)
DOWN = Vector(1, 0)
RIGHT = Vector(0, 1)
LEFT = Vector(0, -1)


def part1():
    carts: Set[Cart] = set()
    size = len(railmap)
    print(f'Sizes: {len(railmap)}, {len(railmap[0])}')
    for i in range(size):
        for j in range(size):
            if railmap[i][j] == 'v':
                carts.add(Cart(Vector(i, j), DOWN))
                railmap[i][j] = '|'
            elif railmap[i][j] == '^':
                carts.add(Cart(Vector(i, j), UP))
                railmap[i][j] = '|'
            elif railmap[i][j] == '>':
                carts.add(Cart(Vector(i, j), RIGHT))
                railmap[i][j] = '-'
            elif railmap[i][j] == '<':
                carts.add(Cart(Vector(i, j), LEFT))
                railmap[i][j] = '-'
    sorted_carts = sorted(carts, key=cart_sort)
    crashed = False
    while not crashed:
        for cart in sorted_carts:
            location = cart.location.value
            if type(location[0]) != int:
                breakpoint()
            if railmap[location[0]][location[1]] == '/':
                if cart.direction == UP:
                    cart.direction = RIGHT
                elif cart.direction == RIGHT:
                    cart.direction = UP

            cart.move_forward()


if __name__ == '__main__':
    # print(railmap)
    part1()
