import unittest

from day4 import validate_passphrase, validate_passphrase_v2


class TestDay4(unittest.TestCase):
    def test_validate_passphrase(self):
        assert validate_passphrase('aa bb cc dd ee')
        assert not validate_passphrase('aa bb cc dd aa')
        assert validate_passphrase('aa bb cc dd aaa')

    def test_validate_passphrase_v2(self):
        assert validate_passphrase_v2('abcde fghij')
        assert not validate_passphrase_v2('abcde xyz ecdab')
        assert validate_passphrase_v2('a ab abc abd abf abj')
        assert validate_passphrase_v2('iiii oiii ooii oooi oooo')
        assert not validate_passphrase_v2('oiii ioii iioi iiio')


if __name__ == '__main__':
    unittest.main()
