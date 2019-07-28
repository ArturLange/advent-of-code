def part_1():
    with open('day8input') as input_file:
        strings = [line.replace('\n', '') for line in input_file.readlines()]
    string_code_len = sum((len(line) for line in strings))
    with open('day8helper.py', 'w') as helper_file:
        helper_file.write('sum_=0\n')
        helper_file.writelines((
            f'sum_+=len(str({str_}))\n'
            for str_ in strings
        ))
    from day8helper import sum_
    print(string_code_len - sum_)


def part_2():
    additional = 0
    with open('day8input') as input_file:
        strings = [line.replace('\n', '') for line in input_file.readlines()]
    for str_ in strings:
        additional += 2
        additional += str_.count('"')
        additional += str_.count('\\')
    print(additional)


if __name__ == "__main__":
    part_1()
    part_2()
