import unittest

from day11 import get_position, get_path, DIRECTIONS, distance, get_farthest_position


class TestDay11(unittest.TestCase):
    def test_get_position(self):
        assert get_position(['n', 'n', 'n']) == (0, 3)
        assert get_position(['s', 's', 's']) == (0, -3)
        assert get_position(['s', 'n', 's']) == (0, -1)

    def test_directions(self):
        x, y = DIRECTIONS['n']
        assert x == 0 and y == 1
        assert distance((0, 0), (x, y)) - 1 < 0.1

        x, y = DIRECTIONS['s']
        assert x == 0 and y == -1
        assert distance((0, 0), (x, y)) - 1 < 0.1

        x, y = DIRECTIONS['ne']
        assert x > 0 and y > 0
        assert distance((0, 0), (x, y)) - 1 < 0.1

        x, y = DIRECTIONS['se']
        assert x > 0 > y
        assert distance((0, 0), (x, y)) - 1 < 0.1

        x, y = DIRECTIONS['nw']
        assert x < 0 < y
        assert distance((0, 0), (x, y)) - 1 < 0.1

        x, y = DIRECTIONS['sw']
        assert x < 0 and y < 0
        assert distance((0, 0), (x, y)) - 1 < 0.1

    def test_get_path(self):
        assert get_path(['n', 'n', 'n']) == 3
        assert get_path(['nw', 'sw']) == 2
        assert get_path(['ne', 'se']) == 2
        assert get_path(['ne', 'ne', 'ne']) == 3
        assert get_path(['ne', 'ne', 'sw', 'sw']) == 0
        assert get_path(['ne', 'ne', 's', 's']) == 2
        assert get_path(['se', 'sw', 'se', 'sw', 'sw']) == 3
