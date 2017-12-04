def get_captcha_score(number):
    score = 0
    string = list(str(number))
    new_string = list(string.pop())
    new_string.extend(string)
    numbers = zip(str(number), new_string)
    for pair in numbers:
        if pair[0] == pair[1]:
            score += int(pair[0])
    return score


assert get_captcha_score(1111) == 4
assert get_captcha_score(1122) == 3
assert get_captcha_score(1234) == 0
assert get_captcha_score(91212129) == 9

with open('inputs/day1', 'r') as input_file:
    print(get_captcha_score(input_file.readline()))
