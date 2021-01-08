from matplotlib import pyplot as plt


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


x = list(range(70))
looksay = '1'
y = []
for i in x:
    old_len = len(looksay)
    looksay = to_looksay(looksay)
    y.append(len(looksay)/old_len)
plt.plot(x, y)
plt.show()
