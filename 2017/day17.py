PUZZLE_INPUT = 345


def spinlock(jump=PUZZLE_INPUT, limit=2017, get_value_after=2017):
    values = [0]
    position = 0
    for i in range(1, limit + 1):
        position = (position + jump) % len(values)
        values.insert(position + 1, i)
        position += 1
    index = values.index(get_value_after)
    print(values[index - 3: index + 4])
    return values[index + 1]


def spinlock_v2(jump=PUZZLE_INPUT, limit=2017):
    values = [0]
    position = 0
    length = len(values)
    for i in range(1, limit + 1):
        position = (position + jump) % length
        if position == 0:
            values.insert(position + 1, i)
        position += 1
        length += 1
    index = values.index(0)
    return values[index + 1]


if __name__ == '__main__':
    print(spinlock())
    print(spinlock_v2(limit=50000000))
