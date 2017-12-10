import unittest

from day10 import hash_list


class TestDay10(unittest.TestCase):
    def test_hash_list(self):
        print(hash_list([187, 254, 0, 81, 169, 219, 1, 190, 19, 102, 255, 56, 46, 32, 2, 216]))
        result = hash_list([3, 4, 1, 5], 5)
        assert result == [3, 4, 2, 1, 0]
        assert result[0] * result[1] == 12

        assert hash_list([5, 2, 3, 1], 5) == [1, 4, 2, 3, 0]


if __name__ == '__main__':
    unittest.main()
