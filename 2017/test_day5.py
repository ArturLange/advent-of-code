import unittest

from day5 import count_steps, count_steps_v2


class TestDay5(unittest.TestCase):
    def test_count_steps(self):
        assert count_steps([0, 3, 0, 1, -3]) == 5
        assert count_steps([1]) == 1
        assert count_steps([0]) == 2
        assert count_steps([0, -1]) == 4

    def test_count_steps_v2(self):
        assert count_steps_v2([0, 3, 0, 1, -3]) == 10
        assert count_steps_v2([1]) == 1
        assert count_steps_v2([0]) == 2
        assert count_steps_v2([0, -1]) == 4
        assert count_steps_v2([3, -1, 5, -3]) == 4


if __name__ == '__main__':
    unittest.main()
