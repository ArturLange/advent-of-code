import unittest

from day16 import spin, exchange, partner


class TestDay16(unittest.TestCase):
    def test_spin(self):
        assert spin(2, [1, 2, 3, 4]) == [3, 4, 1, 2]

    def test_exchange(self):
        assert exchange(1, 4, [0, 1, 2, 3, 4, 5]) == [0, 4, 2, 3, 1, 5]

    def test_partner(self):
        assert partner('a', 't', [
            'e', 't', 'c', 'n', 'k', 'q', 'a'
        ]) == ['e', 'a', 'c', 'n', 'k', 'q', 't']


if __name__ == '__main__':
    unittest.main()
