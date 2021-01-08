def is_abba(input_: str) -> bool:
    if len(input_) != 4:
        raise IndexError('ABBA string must have length 4')
    return (
        input_[::-1] == input_ and len(set(input_)) == 2
    )


def contains_abba(input_: str) -> bool:
    for i in range(len(input_) - 3):
        if is_abba(input_[i:i + 4]):
            return True
    return False


def ip_supports_tls(input_: str) -> bool:
    ip_address = input_.replace(']', ',').replace('[', ',').split(',')
    return (
        any((contains_abba(x) for x in ip_address[::2])) and
        all((not contains_abba(x) for x in ip_address[1::2]))
    )


def ip_supports_ssl(input_: str) -> bool:
    ip_address = input_.replace(']', ',').replace('[', ',').split(',')
    abas = set()
    for string_ in ip_address[::2]:
        for i in range(len(string_) - 2):
            aba = string_[i:i+3]
            if aba == aba[::-1] and len(set(aba)) == 2:
                abas.add(aba)
    if not abas:
        return False
    for string_ in ip_address[1::2]:
        for i in range(len(string_) - 3):
            bab = string_[i:i+3]
            if bab == bab[::-1]:
                aba = bab[1:] + bab[1]
                if aba in abas:
                    return True
    return False


test_lines = [
    'ioxxoj[asdfgh]zxcvbn',
    'abcd[bddb]xyyx',
    'aaaa[qwer]tyui',
    'ioxxoj[asdfgh]zxcvbn',
]


def part1() -> int:
    count = 0
    with open('day7input') as input_file:
        for line in input_file.readlines():
            ip_address = line.replace(
                '\n', '')
            if ip_supports_tls(ip_address):
                count += 1
    return count


def part2() -> int:
    count = 0
    with open('day7input') as input_file:
        for line in input_file.readlines():
            ip_address = line.replace(
                '\n', '')
            if ip_supports_ssl(ip_address):
                count += 1
    return count


if __name__ == '__main__':
    print(part1())
    print(part2())
