import unittest

from day23 import Execution


class TestDay23(unittest.TestCase):
    def test_atomic_operations(self):
        operations = ['set f 23']
        execution = Execution(operations)
        execution.execute()
        expected = {x: 0 for x in 'abcdefgh'}
        expected['f'] = 23
        assert execution.sounds == expected

        operations = ['sub d -6']
        execution = Execution(operations)
        execution.execute()
        expected = {x: 0 for x in 'abcdefgh'}
        expected['d'] = 6
        assert execution.sounds == expected

        operations = ['sub d -6', 'mul d -20']
        execution = Execution(operations)
        execution.execute()
        expected = {x: 0 for x in 'abcdefgh'}
        expected['d'] = -120
        assert execution.sounds == expected

        operations = ['jnz a 30', 'set d -20']
        execution = Execution(operations)
        execution.execute()
        expected = {x: 0 for x in 'abcdefgh'}
        expected['d'] = -20
        assert execution.sounds == expected

        operations = ['set a 3', 'jnz a 30', 'set d -20']
        execution = Execution(operations)
        execution.execute()
        expected = {x: 0 for x in 'abcdefgh'}
        expected['a'] = 3
        assert execution.sounds == expected

    def test_execute(self):
        operations = [
            'set b 67',
            'set c b',
            'jnz a 2',
            'jnz 1 5'
        ]
        expected = {x: 0 for x in 'abcdefgh'}
        expected['b'] = 67
        expected['c'] = 67
        execution = Execution(operations)
        execution.execute()
        sounds = execution.sounds
        assert sounds == expected


if __name__ == '__main__':
    unittest.main()
