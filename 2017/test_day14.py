import unittest

from day14 import hex_to_bin


class TestDay14(unittest.TestCase):
    def test_hex_to_bin(self):
        assert hex_to_bin('0') == '0000'
        assert hex_to_bin('1') == '0001'
        assert hex_to_bin('4') == '0100'
        assert hex_to_bin('8') == '1000'
        assert hex_to_bin('a') == '1010'
