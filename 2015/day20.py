from time import time

from matplotlib import pyplot as plt


def get_divisors(number: int):
    i = 0
    while i < int(number ** 0.5):
        i += 1
        if number % i == 0:
            yield i
            if number // i != i:
                yield number // i 


def get_divisors2(number: int):
    i = 0
    while i < int(number ** 0.5):
        i += 1
        if number % i == 0:
            if number / i <= 50:
                yield i
            if i <= 50 and number // i != i:
                yield number // i 


def get_presents_number(house_num: int):
    return 10 * sum(get_divisors(house_num))

def get_presents_number2(house_num: int):
    return 11 * sum(get_divisors2(house_num))

def part1():
    presents_number = 10
    house_num = 36000000 // 50
    while presents_number < 36000000:
        house_num += 1
        presents_number = get_presents_number(house_num)
        if house_num % 1000 == 0:
            print(house_num, presents_number)

    return house_num

def part2():
    presents_number = 10
    house_num = 36000000 // 50
    while presents_number < 36000000:
        house_num += 1
        presents_number = get_presents_number2(house_num)
        if house_num % 1000 == 0:
            print(house_num, presents_number)

    return house_num


if __name__ == "__main__":
    # print(part1())
    print(part2())
