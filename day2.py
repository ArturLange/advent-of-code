def checksum(spreadsheet):
    sum_ = 0
    for line in spreadsheet.split('\n'):
        numbers = [int(number) for number in line.split()]
        sum_ += max(numbers) - min(numbers)
    return sum_


spreadsheet1 = """5 1 9 5
7 5 3
2 4 6 8"""
assert checksum(spreadsheet1) == 18

with open('inputs/day2', 'r') as input_file:
    input_ = input_file.read()
    print(checksum(input_))
