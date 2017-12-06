from collections import Counter
from itertools import combinations


def validate_passphrase(passphrase):
    counter = Counter(passphrase.split())
    return all((count == 1 for count in counter.values()))


def is_anagram(word1, word2):
    w1 = list(word1)
    w2 = list(word2)
    w1.sort()
    w2.sort()
    return w1 == w2


def validate_passphrase_v2(passphrase):
    checks = combinations(passphrase.split(), 2)
    return all((not is_anagram(word1, word2) for word1, word2 in checks))


if __name__ == '__main__':
    with open('inputs/day4', 'r') as input_file:
        valid = 0
        valid_v2 = 0
        for line in input_file.readlines():
            if validate_passphrase(line):
                valid += 1
            if validate_passphrase_v2(line):
                valid_v2 += 1
        print(valid, valid_v2)
