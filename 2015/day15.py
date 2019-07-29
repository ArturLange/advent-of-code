from itertools import product
from typing import Tuple

Ingredient = Tuple[int, int, int, int, int]


def get_score(recipe, values) -> int:
    cap = max([sum((recipe[x] * values[x][0] for x in range(len(recipe)))), 0])
    dur = max([sum((recipe[x] * values[x][1] for x in range(len(recipe)))), 0])
    fla = max([sum((recipe[x] * values[x][2] for x in range(len(recipe)))), 0])
    tex = max([sum((recipe[x] * values[x][3] for x in range(len(recipe)))), 0])
    # print(f'{recipe}: {cap} * {dur} * {fla} * {tex} = {cap*dur*fla*tex}')
    return cap * dur * tex * fla


def part1():
    ingredients: List[Ingredient] = []
    with open('day15input') as input_file:
        for line in input_file.readlines():
            parsed_line = line.split()
            cap = int(parsed_line[2].replace(',', ''))
            dur = int(parsed_line[4].replace(',', ''))
            fla = int(parsed_line[6].replace(',', ''))
            tex = int(parsed_line[8].replace(',', ''))
            cal = int(parsed_line[10].replace(',', ''))
            ingredients.append((cap, dur, fla, tex, cal))
    print(ingredients)
    options = product(range(101), repeat=len(ingredients))
    options = filter(lambda x: sum(x) == 100, options)
    return max((get_score(x, ingredients) for x in options))


def part2():
    ingredients: List[Ingredient] = []
    with open('day15input') as input_file:
        for line in input_file.readlines():
            parsed_line = line.split()
            cap = int(parsed_line[2].replace(',', ''))
            dur = int(parsed_line[4].replace(',', ''))
            fla = int(parsed_line[6].replace(',', ''))
            tex = int(parsed_line[8].replace(',', ''))
            cal = int(parsed_line[10].replace(',', ''))
            ingredients.append((cap, dur, fla, tex, cal))
    print(ingredients)
    options = product(range(101), repeat=len(ingredients))
    options = filter(lambda x: sum(x) == 100, options)
    options = filter(
        lambda x: sum((ingredients[i][-1] * x[i]
                       for i in range(len(x)))) == 500,
        options
    )
    return max((get_score(x, ingredients) for x in options))


if __name__ == "__main__":
    # ingredients = [(-1, -2, 6, 3, 8), (2, 3, -2, -1, 3)]
    # recipe = (44, 56)
    # print(get_score(recipe, ingredients))
    print(part2())
