from copy import deepcopy


def get_captcha_score(number, places):
    score = 0
    string = list(str(number))
    new_string = move_list(string, places)
    numbers = zip(string, new_string)
    for pair in numbers:
        if pair[0] == pair[1]:
            score += int(pair[0])
    return score


def move_list(list_, number):
    old_list = deepcopy(list_)
    new_list = []
    for _ in range(number):
        new_list.append(old_list.pop())
    new_list.reverse()
    new_list.extend(old_list)
    return new_list


assert get_captcha_score(1111, 1) == 4
assert get_captcha_score(1122, 1) == 3
assert get_captcha_score(1234, 1) == 0
assert get_captcha_score(91212129, 1) == 9

assert get_captcha_score(1212, 2) == 6
assert get_captcha_score(1221, 2) == 0
assert get_captcha_score(123425, 3) == 4
assert get_captcha_score(123123, 3) == 12
assert get_captcha_score(12131415, 4) == 4

with open('inputs/day1', 'r') as input_file:
    input_string = input_file.readline()
    print(get_captcha_score(input_string, 1))
    print(get_captcha_score(input_string, int(len(input_string) / 2)))
