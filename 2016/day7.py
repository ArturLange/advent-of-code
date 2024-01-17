
with open('day7input') as input_file:
    input_lines = [line.replace('\n', '') for line in input_file.readlines()]


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
        for i in range(len(string_) - 2):
            bab = string_[i:i+3]
            if bab == bab[::-1]:
                aba = bab[1:] + bab[1]
                if aba in abas:
                    return True
    return False


test_lines_1 = [
    ('abba[mnop]qrst', True),
    ('abcd[bddb]xyyx', False),
    ('aaaa[qwer]tyui', False),
    ('ioxxoj[asdfgh]zxcvbn', True),
]

test_lines_2 = [
    ('aba[bab]xyz', True),
    ('xyx[xyx]xyx', False),
    ('aaa[kek]eke', True),
    ('zazbz[bzb]cdb', True),
]


def part1() -> int:
    count = 0
    for ip_address in input_lines:
        if ip_supports_tls(ip_address):
            count += 1
    return count


def part2() -> int:
    count = 0
    for ip_address in input_lines:
        if ip_supports_ssl(ip_address):
            count += 1
    return count

def test_1():
    for input_, expected_result in test_lines_1:
        assert ip_supports_tls(input_) == expected_result

def test_2():
    for input_, expected_result in test_lines_2:
        assert ip_supports_ssl(input_) == expected_result


if __name__ == '__main__':
    test_1()
    test_2()
    print(part1())
    print(part2())
