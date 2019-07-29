import json
import re


def part1():
    with open('day12input') as input_file:
        return sum((int(i) for i in re.findall(r'-?\d+', input_file.read())))


def get_value(obj):
    if type(obj) == int:
        return obj
    elif type(obj) == list:
        return sum((get_value(x) for x in obj))
    elif type(obj) == dict:
        return sum((get_value(x) for x in obj.values())) if "red" not in obj.values() else 0
    else:
        return 0


def part2():
    with open('day12input') as json_file:
        numbers_json = json.load(json_file)
        return get_value(numbers_json)


if __name__ == "__main__":
    print(part2())
    # print(get_value([1, "red", 5]))
