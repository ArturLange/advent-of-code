import unittest

from day3 import road_generator, get_coordinates, get_distance


class TestDay3(unittest.TestCase):
    def test_road_generator(self):
        assert list(road_generator(6)) == [(1, 0), (0, 1), (-1, 0), (-1, 0), (0, -1)]
        assert list(road_generator(2)) == [(1, 0)]
        assert list(road_generator(1)) == []

    def test_get_coordinates(self):
        assert get_coordinates(1) == (0, 0)
        assert get_coordinates(5) == (-1, 1)

    def test_get_distance(self):
        assert get_distance(1) == 0
        assert get_distance(12) == 3
        assert get_distance(23) == 2
        assert get_distance(1024) == 31


if __name__ == '__main__':
    unittest.main()
