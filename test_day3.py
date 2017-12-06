import unittest

from day3 import road_generator, get_coordinates, get_distance_from_zero, counts_generator, \
    is_neighbour, get_larger_than


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

    def test_get_coordinates(self):
        assert get_coordinates(1) == (0, 0)
        assert get_coordinates(5) == (-1, 1)

    def test_get_distance_from_zero(self):
        assert get_distance_from_zero(1) == 0
        assert get_distance_from_zero(12) == 3
        assert get_distance_from_zero(23) == 2
        assert get_distance_from_zero(1024) == 31

    def test_is_neighbour(self):
        assert is_neighbour((0, 0), (0, 1))
        assert is_neighbour((45, 2), (44, 2))
        assert is_neighbour((45, 2), (44, 3))
        assert not is_neighbour((12, 2), (12, 0))

    def test_get_larger_than(self):
        assert get_larger_than(1) == 2
        assert get_larger_than(2) == 4
        assert get_larger_than(3) == 4
        assert get_larger_than(4) == 5
        assert get_larger_than(5) == 10
        assert get_larger_than(6) == 10
        assert get_larger_than(7) == 10
        assert get_larger_than(8) == 10
        assert get_larger_than(9) == 10
        assert get_larger_than(10) == 11
        assert get_larger_than(11) == 23


if __name__ == '__main__':
    unittest.main()
