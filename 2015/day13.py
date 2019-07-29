from itertools import permutations


def get_score(sitting_config, scores):
    score = 0
    score += sum((
        scores[sitting_config[i]][sitting_config[i+1]]
        for i in range(len(sitting_config)-1)
    ))
    score += scores[sitting_config[-1]][sitting_config[0]]
    score += sum((
        scores[sitting_config[i]][sitting_config[i-1]]
        for i in range(1, len(sitting_config))
    ))
    score += scores[sitting_config[0]][sitting_config[-1]]
    return score


def part1():
    happinesses = dict()
    with open('day13input') as input_file:
        lines = input_file.readlines()
    for line in lines:
        parsed_line = line.split()
        person1 = parsed_line[0]
        happiness = int(parsed_line[3])
        if parsed_line[2] == 'lose':
            happiness = happiness * -1
        person2 = parsed_line[10][:-1]
        if not person1 in happinesses:
            happinesses[person1] = {person2: happiness}
        else:
            happinesses[person1][person2] = happiness
    options = permutations(happinesses.keys())
    return max((get_score(option, happinesses) for option in options))


def part2():
    happinesses = dict()
    with open('day13input') as input_file:
        lines = input_file.readlines()
    for line in lines:
        parsed_line = line.split()
        person1 = parsed_line[0]
        happiness = int(parsed_line[3])
        if parsed_line[2] == 'lose':
            happiness = happiness * -1
        person2 = parsed_line[10][:-1]
        if not person1 in happinesses:
            happinesses[person1] = {person2: happiness}
        else:
            happinesses[person1][person2] = happiness

    for x in happinesses.keys():
        happinesses[x]['Me'] = 0
    happinesses['Me'] = {x: 0 for x in happinesses.keys()}

    options = permutations(happinesses.keys())
    return max((get_score(option, happinesses) for option in options))


if __name__ == "__main__":
    print(part2())
