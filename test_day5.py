import unittest

from day5 import count_steps


class TestDay5(unittest.TestCase):
    def test_count_steps(self):
        assert count_steps([0, 3, 0, 1, -3]) == 5
        assert count_steps([1]) == 1
        assert count_steps([0]) == 2
        assert count_steps([0, -1]) == 4


if __name__ == '__main__':
    unittest.main()
