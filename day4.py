from collections import Counter


def validate_passphrase(passphrase):
    counter = Counter(passphrase.split())
    return all((count == 1 for count in counter.values()))


if __name__ == '__main__':
    with open('inputs/day4', 'r') as input_file:
        valid = 0
        for line in input_file.readlines():
            if validate_passphrase(line):
                valid += 1
        print(valid)
