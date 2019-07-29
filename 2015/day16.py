
def aunt_matches(aunt: dict) -> bool:
    return all((
        aunt.get('children') is None or aunt.get('children') == 3,
        aunt.get('cats') is None or aunt.get('cats') == 7,
        aunt.get('samoyeds') is None or aunt.get('samoyeds') == 2,
        aunt.get('pomeranians') is None or aunt.get('pomeranians') == 3,
        aunt.get('akitas') is None or aunt.get('akitas') == 0,
        aunt.get('vizslas') is None or aunt.get('vizslas') == 0,
        aunt.get('goldfish') is None or aunt.get('goldfish') == 5,
        aunt.get('trees') is None or aunt.get('trees') == 3,
        aunt.get('cars') is None or aunt.get('cars') == 2,
        aunt.get('perfumes') is None or aunt.get('perfumes') == 1,
    ))


def aunt_matches_2(aunt: dict) -> bool:
    return all((
        aunt.get('children') is None or aunt.get('children') == 3,
        aunt.get('cats') is None or aunt.get('cats') > 7,
        aunt.get('samoyeds') is None or aunt.get('samoyeds') == 2,
        aunt.get('pomeranians') is None or aunt.get('pomeranians') < 3,
        aunt.get('akitas') is None or aunt.get('akitas') == 0,
        aunt.get('vizslas') is None or aunt.get('vizslas') == 0,
        aunt.get('goldfish') is None or aunt.get('goldfish') < 5,
        aunt.get('trees') is None or aunt.get('trees') > 3,
        aunt.get('cars') is None or aunt.get('cars') == 2,
        aunt.get('perfumes') is None or aunt.get('perfumes') == 1,
    ))


def part1():
    with open('day16input') as input_file:
        aunts = dict()
        for line in input_file.readlines():
            parsed_line = line.split()
            number = int(parsed_line[1].replace(':', ''))
            names = parsed_line[2::2]
            values = parsed_line[3::2]
            aunt = {"number": number}
            for i in range(len(names)):
                aunt[names[i].replace(':', '')] = int(
                    values[i].replace(',', ''))
            aunts[number] = aunt
        aunts = {x: aunts[x] for x in aunts if aunt_matches(aunts[x])}
    return list(aunts.values())[0]


def part2():
    with open('day16input') as input_file:
        aunts = dict()
        for line in input_file.readlines():
            parsed_line = line.split()
            number = int(parsed_line[1].replace(':', ''))
            names = parsed_line[2::2]
            values = parsed_line[3::2]
            aunt = {"number": number}
            for i in range(len(names)):
                aunt[names[i].replace(':', '')] = int(
                    values[i].replace(',', ''))
            aunts[number] = aunt
        aunts = {x: aunts[x] for x in aunts if aunt_matches_2(aunts[x])}
    return list(aunts.values())[0]


if __name__ == "__main__":
    print(part1())
    print(part2())
