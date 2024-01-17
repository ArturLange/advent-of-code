from typing import Iterable
import functools

EMPTY_CELL = ". "

with open("inputs/day11.txt") as input_file:
    input_lines = [line.replace("\n", "") for line in input_file.readlines()]


def name_to_token(name: str) -> str:
    return "".join(x[0].upper() for x in name.split())


def is_microchip(token: str) -> bool:
    return "M" in token


def is_generator(token: str) -> bool:
    return "G" in token


def is_position_safe(floors: list[set[str]]) -> bool:
    for floor in floors:
        microchips = tuple(x for x in floor if is_microchip(x))
        for microchip in microchips:
            generator = microchip.replace('M', 'G')
            if generator not in floor and len(microchips) > 1:
                return False
    return True


def get_floors(input_: Iterable[str]) -> list[set[str]]:
    floors: list[set[str]] = []
    for line in input_:
        if "contains nothing relevant" in line:
            floors.append(set())
        else:
            tokens = set()
            items = line.split(",")
            for item in items:
                token = name_to_token(item.replace("and", "").split(" a ")[1])
                tokens.add(token)
            floors.append(tokens)
    return floors


def get_diagram(floors: Iterable[set[str]]) -> str:
    all_tokens = functools.reduce(lambda a, b: a | b, floors)
    grid = [
        ["F1", "E "],
        ["F2", ". "],
        ["F3", ". "],
        ["F4", ". "],
    ]
    for token in sorted(all_tokens):
        for line_num, line in enumerate(grid):
            if token in floors[line_num]:
                line.append(token)
            else:
                line.append(EMPTY_CELL)

    return "\n".join(" ".join(line) for line in reversed(grid))


if __name__ == "__main__":
    floors = get_floors(input_lines)
    diagram = get_diagram(floors)
    print(is_position_safe(floors))
    print(diagram)
