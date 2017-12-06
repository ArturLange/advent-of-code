import unittest

from day4 import validate_passphrase


class TestDay4(unittest.TestCase):
    def test_validate_passphrase(self):
        assert validate_passphrase('aa bb cc dd ee')
        assert not validate_passphrase('aa bb cc dd aa')
        assert validate_passphrase('aa bb cc dd aaa')


if __name__ == '__main__':
    unittest.main()
