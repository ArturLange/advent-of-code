from collections import Counter
from typing import Tuple


def part1():
    with open('day4input') as input_file:
        rooms = [x.replace('\n', '') for x in input_file.readlines()]
    sum_ = 0
    for room in rooms:
        sector_id = is_room_real(room)
        sum_ += sector_id if sector_id else 0
    return sum_


def part2():
    with open('day4input') as input_file:
        rooms = [x.replace('\n', '') for x in input_file.readlines()]
    for room in rooms:
        decrypted = decrypt_room(room)
        if 'north' in decrypted[0] and 'pole' in decrypted[0]:
            print(decrypted)


def decrypt_room(room_string: str):
    code, checksum = room_string.replace(']', '').split('[')
    split_code = code.split('-')
    name = '-'.join(split_code[:-1])
    sector_id = int(split_code[-1])
    code_key = sector_id % 26
    new_str = ''
    for char in name:
        if char == '-':
            new_str += '-'
        else:
            new_str += chr(((ord(char)-97 + code_key) % 26) + 97)

    return new_str, sector_id


def get_key_func(number: int):
    def func(element: Tuple[str, int]):
        return (number - element[1]) * 30 + ord(element[0]) - 97
    return func


def is_room_real(room_string: str):
    code, checksum = room_string.replace(']', '').split('[')
    split_code = code.split('-')
    name = ''.join(split_code[:-1])
    sector_id = int(split_code[-1])
    counts = Counter(name).most_common()
    real_checksum = ''.join((x[0] for x in sorted(
        counts, key=get_key_func(counts[0][1]))))[:5]
    if checksum == real_checksum:
        return sector_id


if __name__ == "__main__":
    print(part1())
    part2()
