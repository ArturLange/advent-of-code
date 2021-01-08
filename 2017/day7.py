import re
from collections import Counter
from pprint import pprint


def initialise_tree(list_: list) -> dict:
    tree = {}
    for line in list_:
        for key in re.compile(r'[a-zA-Z]+').finditer(line):
            tree[key.group(0)] = {}
    return tree


def get_value_recursive(tree, key):
    if type(tree) != dict:
        return False
    elif key in tree:
        return tree[key]
    else:
        for value in (get_value_recursive(tree[new_tree_index], key) for new_tree_index in tree):
            if value:
                return value


def parse_list(list_: list):
    result = initialise_tree(list_)
    while len(result) > 1:
        for line in list_:
            if re.compile(r'[a-zA-Z]+ \([0-9]+\) -> ([a-zA-Z]+,?\s?)+').fullmatch(line):
                line = line.split('->')
                for key in str(line[1]).split(','):
                    key = key[1:]
                    if result.get(key) and result[key] is not {}:
                        get_value_recursive(result, line[0].split()[0])[key] = result.get(key)
                        result.pop(key)
            elif re.compile(r'[a-zA-Z]+ \([0-9]+\)').fullmatch(line):
                data = line.split()
                if result.get(data[0]) is not None:
                    result[data[0]] = int(data[1][1:-1])
    return list(result.keys())[0], result


def get_weights_dict(list_: list) -> dict:
    weights = {}
    for line in list_:
        line = line.split()
        weights[line[0]] = int(line[1][1:-1])
    return weights


def get_weight(tree, key, weights) -> int:
    node = get_value_recursive(tree, key)
    if type(node) == int:
        return node
    else:
        return weights[key] + sum((get_weight(tree, new_key, weights) for new_key in node.keys()))


def get_unbalanced(tree: dict, weights: dict):
    key: str = list(tree.keys())[0]
    branches_weights = {k: get_weight(tree, k, weights) for k in tree[key].keys()}
    counter = Counter(branches_weights.values())
    pprint(tree)
    if len(counter) == 1:
        return None
    unbalanced = counter.most_common()
    unbalanced.reverse()
    unbalanced = unbalanced[0][0]
    unbalanced = [k for k in branches_weights if branches_weights[k] == unbalanced][0]
    print(unbalanced, weights[unbalanced], counter)
    if get_unbalanced(get_value_recursive(tree, unbalanced), weights) == None:
        return key


def balance_tree(list_: list):
    # not to be used
    tree = parse_list(list_)[1]
    weights = get_weights_dict(list_)
    weights_total_and_levels = {key: None for key in weights.keys()}
    while any((weights_total_and_levels.get(key) is not None or
               weights_total_and_levels.get(key)[0] is not None or
               weights_total_and_levels.get(key)[1] is not None for key in weights.keys())):
        for key, value in weights.items():
            key_value = get_value_recursive(tree, key)
            if key_value == value:
                weights_total_and_levels[key] = (key_value)


if __name__ == '__main__':
    with open('inputs/day7', 'r') as input_file:
        list_ = [line.replace('\n', '') for line in input_file.readlines()]
        print(parse_list(list_)[0])
        tree = parse_list(list_)[1]
        weights = get_weights_dict(list_)
        print(get_unbalanced(tree, weights))
