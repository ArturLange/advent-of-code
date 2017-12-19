import unittest

from day19 import get_position_cell


class TestDay19(unittest.TestCase):
    def test_get_position_cell(self):
        map_ = '''|   
        |   
        +--+
           |'''
        assert get_position_cell((0, 0), map_) == '|'


if __name__ == '__main__':
    unittest.main()
