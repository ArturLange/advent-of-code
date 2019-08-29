from itertools import accumulate, count

ROW = 2947
COLUMN = 3029


def generate_first_numbers():
    return (x+1 for x in accumulate(count(0)))


def coords_to_number(row: int, col: int):
    to_add = col - 1
    row_num = row + to_add
    gen = generate_first_numbers()
    for i in range(row_num-1):
        next(gen)
    return next(gen) + to_add


def get_nth_number(n: int):
    number = 20151125
    for _ in range(n-1):
        number = (number * 252533) % 33554393
    return number


if __name__ == "__main__":
    row = ROW
    col = COLUMN
    number = coords_to_number(row, col)
    print(get_nth_number(number))
