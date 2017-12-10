def hash_list(lengths, list_length=256):
    current_position = 0
    skip_size = 0
    list_ = list(range(list_length))
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
    return list_


if __name__ == '__main__':
    lengths = [187, 254, 0, 81, 169, 219, 1, 190, 19, 102, 255, 56, 46, 32, 2, 216]
    result = hash_list(lengths)
    print(result[0] * result[1])
