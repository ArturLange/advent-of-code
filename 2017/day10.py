from functools import reduce


def hash_list(lengths, list_, current_position=0, skip_size=0):
    list_length = len(list_)
    for length in lengths:
        if length == 0:
            indexes = []
        elif (current_position + length) % list_length <= current_position:
            indexes = list(range(current_position, list_length))
            indexes.extend(list(range(length - len(indexes))))
        else:
            indexes = list(range(current_position, current_position + length))
        if indexes:
            sublist = [list_[index] for index in indexes]
            for index in indexes:
                list_[index] = sublist.pop()
        current_position = (current_position + length + skip_size) % list_length
        skip_size += 1
    return list_, current_position, skip_size


def to_hex(int_):
    hexed = hex(int_)[2:]
    return hexed if len(hexed) == 2 else '0' + hexed


def hash_list_v2(strings, list_length=256, rounds=64):
    lengths = [ord(char) for char in strings]
    lengths.extend([17, 31, 73, 47, 23])
    list_ = list(range(list_length))
    current_position = 0
    skip_size = 0
    for _ in range(rounds):
        list_, current_position, skip_size = hash_list(lengths, list_, current_position, skip_size)
    result_string = ''
    for part in range(16):
        indexes = range(part * 16, part * 16 + 16)
        hashed = reduce(lambda x, y: x ^ y, (list_[index] for index in indexes))
        result_string += to_hex(hashed)
    return result_string


if __name__ == '__main__':
    lengths = [187, 254, 0, 81, 169, 219, 1, 190, 19, 102, 255, 56, 46, 32, 2, 216]
    strings = '187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216'
    list_256 = list(range(256))
    result = hash_list(lengths, list_256)[0]
    print(result[0] * result[1])
    print(hash_list_v2(strings))
