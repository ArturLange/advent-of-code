import unittest

from day2 import checksum, checksum_v2


class TestDay2(unittest.TestCase):
    def test_checksum(self):
        spreadsheet = [[5, 1, 2, 9], [7, 5, 3], [2, 4, 6, 8]]
        assert checksum(spreadsheet) == 18

    def test_checksum_v2(self):
        spreadsheet = [[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]
        assert checksum_v2(spreadsheet) == 9


if __name__ == '__main__':
    unittest.main()
