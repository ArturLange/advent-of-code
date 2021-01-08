import string

with open('day5_input') as input_file:
    polymer = input_file.read()

def part1(polymer):
    to_be_deleted = list((x + x.swapcase() for x in string.ascii_letters))
    print(to_be_deleted)
    while any((x in polymer for x in to_be_deleted)):
        for letter in to_be_deleted:
            polymer = polymer.replace(letter, '')
    polymer = polymer.replace('\n', '')
    print(any((x in polymer for x in to_be_deleted)))
    print(polymer)
    return len(polymer)

def part2(start_polymer):
    return min((
        part1(polymer.replace(letter.upper(), '').replace(letter.lower(), '')) 
        for letter in string.ascii_lowercase
        ))



print(part1(polymer))
print(part1('dabAcCaCBAcCcaDA'))
print(part2(polymer))
