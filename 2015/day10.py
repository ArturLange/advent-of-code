def to_looksay(input_: str):
    result = ''
    queue = list(reversed(input_))
    current = queue.pop()
    count = 1
    while queue:
        next_ = queue.pop()
        if next_ == current:
            count += 1
        else:
            result += f'{count}{current}'
            current = next_
            count = 1
    result += f'{count}{current}'
    return result


if __name__ == "__main__":
    looksay = '3113322113'
    for i in range(50):
        looksay = to_looksay(looksay)
    print(len(looksay))
