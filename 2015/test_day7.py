import unittest

from matplotlib import pyplot as plt

from day7 import parse_operation


class TestDay7(unittest.TestCase):
    def test_parse_operation(self):
        self.assertEqual(
            parse_operation('ep OR eo -> eq'),
            ('eq', 'OR', ['ep', 'eo']))


if __name__ == "__main__":
    unittest.main()
