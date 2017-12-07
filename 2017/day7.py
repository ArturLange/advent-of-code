import re


def initialise_tree(list_):
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


def parse_list(list_):
    result = initialise_tree(list_)
    while len(result) > 1:
        for line in list_:
            # import pdb;pdb.set_trace()
            if re.compile(r'[a-zA-Z]+ \([0-9]+\) -> ([a-zA-Z]+,?\s?)+').fullmatch(line):
                line = line.split('->')
                for key in str(line[1]).split(','):
                    key = key[1:]
                    if result.get(key) and result[key] is not {}:
                        get_value_recursive(result, line[0].split()[0])[key] = result.get(key)
                        # result[line[0].split()[0]][key] = result.get(key)
                        result.pop(key)
            elif re.compile(r'[a-zA-Z]+ \([0-9]+\)').fullmatch(line):
                data = line.split()
                if result.get(data[0]) is not None:
                    result[data[0]] = int(data[1][1:-1])
    return list(result.keys())[0]


if __name__ == '__main__':
    with open('inputs/day7', 'r') as input_file:
        list_ = [line.replace('\n', '') for line in input_file.readlines()]
        print(parse_list(list_))
