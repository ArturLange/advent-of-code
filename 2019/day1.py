with open('inputs/day1') as input_file:
    task_input = [int(x) for x in input_file.readlines()]

print(sum(x // 3 - 2 for x in task_input))


def get_fuel(number):
    return max([number // 3 - 2, 0])


def fuel_total(number):
    result = 0
    while get_fuel(number) != 0:
        number = get_fuel(number)
        result += number
    return result


print(fuel_total(100756))
print(sum(fuel_total(x) for x in task_input))
