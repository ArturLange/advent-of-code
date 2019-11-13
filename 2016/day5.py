import hashlib

day5input = 'abbhdwsy'


def generate_password():
    start = day5input
    number = 0
    while True:
        hashed_str: str = hashlib.md5(f'{start}{number}'.encode()).hexdigest()
        if hashed_str.startswith('00000'):
            pos = hashed_str[5]
            if pos in '01234567':
                yield int(pos), hashed_str[6]
        number += 1


def part1() -> str:
    password = ''
    gen = generate_password()
    for _ in range(8):
        password += next(gen)[0]
    return password


def part2() -> str:
    password = ['' for _ in range(8)]
    gen = generate_password()
    while '' in password:
        position, value = next(gen)
        if not password[position]:
            password[position] = value
    return ''.join(password)


if __name__ == '__main__':
    # print(part1())
    print(part2())
