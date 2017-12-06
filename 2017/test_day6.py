import unittest

from day6 import cycle_time


class TestDay6(unittest.TestCase):
    def test_cycle_time(self):
        assert cycle_time([0, 2, 7, 0]) == (5, 4)


if __name__ == '__main__':
    unittest.main()
