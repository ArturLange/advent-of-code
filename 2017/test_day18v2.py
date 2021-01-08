import unittest

from day18v2 import execute_2_processes
OPERATIONS = '''snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d'''


class TestDay18(unittest.TestCase):
    def test_execute_2_processes(self):
        operations = OPERATIONS.split('\n')
        execute_2_processes(operations)


if __name__ == '__main__':
    unittest.main()
