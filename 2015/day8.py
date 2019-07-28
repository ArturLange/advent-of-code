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


if __name__ == "__main__":
    part_1()
