import unittest

from day11 import get_position, get_path, DIRECTIONS


class TestDay10(unittest.TestCase):
    def test_get_position(self):
        print(get_position(['ne', 'ne', 'ne']))
        assert get_position(['n', 'n', 'n']) == (0, 3)
        assert get_position(['s', 's', 's']) == (0, -3)
        assert get_position(['s', 'n', 's']) == (0, -1)

    def test_directions(self):
        x, y = DIRECTIONS['n']
        assert x == 0 and y == 1

        x, y = DIRECTIONS['s']
        assert x == 0 and y == -1

        x, y = DIRECTIONS['ne']
        assert x > 0 and y > 0

        x, y = DIRECTIONS['se']
        assert x > 0 and y < 0

        x, y = DIRECTIONS['nw']
        assert x < 0 and y > 0

        x, y = DIRECTIONS['sw']
        assert x < 0 and y < 0

    def test_get_path(self):
        assert get_path(['n', 'n', 'n']) == 3
        assert get_path(['nw', 'sw']) == 2
        assert get_path(['ne', 'se']) == 2
