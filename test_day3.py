import unittest

from day3 import road_generator, get_coordinates, get_distance, counts_generator


class TestDay3(unittest.TestCase):
    def test_count_generator(self):
        assert list(counts_generator(1)) == []
        assert list(counts_generator(2)) == [1]
        assert list(counts_generator(3)) == [1, 1]
        assert list(counts_generator(6)) == [1, 1, 2, 2, 3]
        assert list(counts_generator(7)) == [1, 1, 2, 2, 3, 3]

    def test_road_generator(self):
        assert list(road_generator(6)) == [(1, 0), (0, 1), (-1, 0), (-1, 0), (0, -1)]
        assert list(road_generator(2)) == [(1, 0)]
        assert list(road_generator(1)) == []

        a = list(road_generator(25000))

    def test_get_coordinates(self):
        assert get_coordinates(1) == (0, 0)
        assert get_coordinates(5) == (-1, 1)

    def test_get_distance(self):
        assert get_distance(1) == 0
        assert get_distance(12) == 3
        assert get_distance(23) == 2
        assert get_distance(1024) == 31

        # assert get_distance(10240) == 63


if __name__ == '__main__':
    unittest.main()
