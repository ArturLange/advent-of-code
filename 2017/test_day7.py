import unittest

from day7 import parse_list, get_value_recursive

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

from pprint import pprint


class TestDay7(unittest.TestCase):
    def test_get_value_recursive(self):
        assert get_value_recursive({'a': {'b': 34}, 'c': 13}, 'b') == 34
        assert get_value_recursive({'a': {'b': {'d': 25}}, 'c': 13}, 'd') == 25

    def test_parse_list(self):
        pprint(parse_list(list_))
        assert parse_list(list_) == 'tknk'


if __name__ == '__main__':
    unittest.main()
