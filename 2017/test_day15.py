import unittest

from day15 import get_matches, generator_a, generator_b, to_bin_32, trim, picky_generator_a, picky_generator_b


class TestDay15(unittest.TestCase):
    def test_get_matches(self):
        # assert get_matches(65, 8921, 5) == 1
        # assert get_matches(65, 8921) == 588
        pass

    def test_generator_a(self):
        a = generator_a(65)
        assert next(a) == 1092455
        assert next(a) == 1181022009
        assert next(a) == 245556042
        assert next(a) == 1744312007
        assert next(a) == 1352636452

    def test_picky_generator_a(self):
        a = picky_generator_a(65)
        assert next(a) == 1352636452
        assert next(a) == 1992081072
        assert next(a) == 530830436
        assert next(a) == 1980017072
        assert next(a) == 740335192

    def test_picky_generator_b(self):
        b = picky_generator_b(8921)
        assert next(b) == 1233683848

    def test_generator_b(self):
        b = generator_b(8921)
        assert next(b) == 430625591

    def test_to_bin_32(self):
        assert to_bin_32(1092455) == '00000000000100001010101101100111'
        assert to_bin_32(430625591) == '00011001101010101101001100110111'

    def test_trim(self):
        assert trim('00000000000100001010101101100111', 16) == '1010101101100111'
