import unittest

from day10 import hash_list, hash_list_v2


class TestDay10(unittest.TestCase):
    def test_hash_list(self):
        list_5 = list(range(5))
        result = hash_list([3, 4, 1, 5], list_5)[0]
        assert result == [3, 4, 2, 1, 0]
        assert result[0] * result[1] == 12

    def test_hash_list_v2(self):
        assert hash_list_v2('') == 'a2582a3a0e66e6e86e3812dcb672a272'
        assert hash_list_v2('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
        assert hash_list_v2('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
        assert hash_list_v2('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'


if __name__ == '__main__':
    unittest.main()
