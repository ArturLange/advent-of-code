PUZZLE_INPUT = (618, 814)


def generator_a(start):
    factor = 16807
    modulo = 2147483647
    a = start
    while True:
        b = (a * factor) % modulo
        yield b
        a = b


def generator_b(start):
    factor = 48271
    modulo = 2147483647
    a = start
    while True:
        b = (a * factor) % modulo
        yield b
        a = b


def to_bin_32(number):
    return bin(number)[2:].rjust(32, '0')


def trim(bin_str, bits):
    return bin_str[bits:]


def picky_generator_a(start):
    factor = 16807
    modulo = 2147483647
    a = start
    while True:
        b = (a * factor) % modulo
        while b % 4 != 0:
            b = (b * factor) % modulo
        yield b
        a = b


def picky_generator_b(start):
    factor = 48271
    modulo = 2147483647
    a = start
    while True:
        b = (a * factor) % modulo
        while b % 8 != 0:
            b = (b * factor) % modulo
        yield b
        a = b


def get_matches(a_start, b_start, limit=40000000):
    count = 0
    score = 0
    a = generator_a(a_start)
    b = generator_b(b_start)
    while count < limit:
        a_bin = to_bin_32(next(a))[16:]
        b_bin = to_bin_32(next(b))[16:]
        if a_bin == b_bin:
            score += 1
        count += 1
    return score


def get_matches_picky(a_start, b_start, limit=5000000):
    count = 0
    score = 0
    a = picky_generator_a(a_start)
    b = picky_generator_b(b_start)
    while count < limit:
        a_bin = to_bin_32(next(a))[16:]
        b_bin = to_bin_32(next(b))[16:]
        if a_bin == b_bin:
            score += 1
        count += 1
    return score


if __name__ == '__main__':
    print(get_matches(PUZZLE_INPUT[0], PUZZLE_INPUT[1]))
    print(get_matches_picky(PUZZLE_INPUT[0], PUZZLE_INPUT[1]))
