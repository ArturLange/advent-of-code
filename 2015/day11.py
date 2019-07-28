import math


def letter_to_int(letter: str) -> int:
    return ord(letter) - 96


def int_to_letter(int_: int) -> str:
    return chr(int_ + 96)


def str_to_int(string_: str) -> int:
    result = 0
    rev = string_[::-1]
    for i in range(len(string_)):
        result += (letter_to_int(rev[i]) * (27 ** i))
    return result


def int_to_str(int_: int) -> str:
    value = int_
    result = ''
    length = int(math.log(value, 27)) + 1
    for i in range(length):
        x = length - i - 1
        if 27 ** x <= value:
            y = value // (27 ** x)
            result += int_to_letter(y)
            value -= y * (27 ** x)
    return result


class Password:
    def __init__(self, str_):
        self.str = str_
        self.value = str_to_int(self.str)

    def __add__(self, other):
        length = len(self.str)
        self.value += other
        self.str = int_to_str(self.value)
        while len(self.str) != length:
            self.value += other
            self.str = int_to_str(self.value)
        return self

    def __str__(self):
        return self.str

    def _contains_one_straight(self) -> bool:
        results = [
            letter_to_int(self.str[a:a+3][0]) == letter_to_int(
                self.str[a:a+3][1])-1 == letter_to_int(self.str[a:a+3][2])-2
            for a in range(len(self.str) - 2)
        ]
        return results.count(True) >= 1

    def _not_contains_invalid(self) -> bool:
        return all((
            a not in self.str for a in 'iol'
        ))

    def _contains_two_pairs(self) -> bool:
        pairs = [
            self.str[a:a+2][0] == self.str[a:a+2][1]
            for a in range(len(self.str) - 1)
        ]
        triples = [
            self.str[a:a+3][0] == self.str[a:a+3][1] == self.str[a:a+3][2]
            for a in range(len(self.str) - 2)
        ]
        return pairs.count(True) == 2 and not any(triples)

    def is_valid(self) -> bool:
        return self._not_contains_invalid() and self._contains_two_pairs() and self._contains_one_straight()


if __name__ == "__main__":
    passw = Password('hxbxxyzz')
    passw += 1
    while not passw.is_valid():
        passw += 1
    print(passw)
