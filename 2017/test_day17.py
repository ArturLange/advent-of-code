import unittest

from day17 import spinlock


class TestDay17(unittest.TestCase):
    def test_spinlock(self):
        values = spinlock
        assert spinlock(3) == 638


if __name__ == '__main__':
    unittest.main()
