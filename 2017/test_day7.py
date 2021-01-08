import unittest

from day7 import parse_list, get_value_recursive, get_weight, get_weights_dict

list_ = [
    'pbga (66)',
    'xhth (57)',
    'ebii (61)',
    'havc (66)',
    'ktlj (57)',
    'fwft (72) -> ktlj, cntj, xhth',
    'qoyq (66)',
    'padx (45) -> pbga, havc, qoyq',
    'tknk (41) -> ugml, padx, fwft',
    'jptl (61)',
    'ugml (68) -> gyxo, ebii, jptl',
    'gyxo (61)',
    'cntj (57)'
]


class TestDay7(unittest.TestCase):
    def test_get_value_recursive(self):
        assert get_value_recursive({'a': {'b': 34}, 'c': 13}, 'b') == 34
        assert get_value_recursive({'a': {'b': {'d': 25}}, 'c': 13}, 'd') == 25
        assert get_value_recursive({'a': {'b': {'d': 25}}, 'c': 13}, 'b') == {'d': 25}

    def test_parse_list(self):
        assert parse_list(list_)[0] == 'tknk'

    def test_get_weights_dict(self):
        expected = {
            'pbga': 66,
            'xhth': 57,
            'ebii': 61,
            'havc': 66,
            'ktlj': 57,
            'fwft': 72,
            'qoyq': 66,
            'padx': 45,
            'tknk': 41,
            'jptl': 61,
            'ugml': 68,
            'gyxo': 61,
            'cntj': 57
        }
        assert get_weights_dict(list_) == expected

    def test_get_weight(self):
        assert get_weight({'a': {'b': 34}, 'c': 13}, 'c', {'a': 12, 'b': 34, 'c': 13}) == 13
        assert get_weight({'a': {'b': 34}, 'c': 13}, 'b', {'a': 12, 'b': 34, 'c': 13}) == 34
        assert get_weight({'a': {'b': 34}, 'c': 13}, 'a', {'a': 12, 'b': 34, 'c': 13}) == 46
        bigger_tree = {
            'a': {
                'b': 45,
                'g': 23
            },
            'v': {
                'd': {
                    'e': 2,
                    'q': 6
                },
                'p': {
                    'y': 12,
                    't': 7
                }
            }
        }
        weights = {'a': 3, 'b': 45, 'g': 23, 'v': 7, 'd': 4, 'e': 2, 'q': 6, 'p': 0, 'y': 12,
                   't': 7}
        assert get_weight(bigger_tree, 'a', weights) == 3 + 45 + 23
        assert get_weight(bigger_tree, 'b', weights) == 45
        assert get_weight(bigger_tree, 'e', weights) == 2
        assert get_weight(bigger_tree, 'd', weights) == 4 + 2 + 6
        assert get_weight(bigger_tree, 'p', weights) == 0 + 12 + 7
        assert get_weight(bigger_tree, 'v', weights) == 7 + (4 + 2 + 6) + (0 + 12 + 7)


if __name__ == '__main__':
    unittest.main()
