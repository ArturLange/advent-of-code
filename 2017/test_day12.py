import unittest

from day12 import PipeTown


class TestDay12(unittest.TestCase):
    def test_initialize_edges(self):
        pid_list = [
            '0 <-> 2',
            '1 <-> 1',
            '2 <-> 0, 3, 4',
            '3 <-> 2, 4',
            '4 <-> 2, 3, 6',
            '5 <-> 6',
            '6 <-> 4, 5'
        ]
        expected = {
            0: {2},
            1: {1},
            2: {0, 3, 4},
            3: {2, 4},
            4: {2, 3, 6},
            5: {6},
            6: {4, 5}
        }
        pipetown = PipeTown(pid_list)
        pipetown.initialize_nodes()
        assert pipetown.programs == expected

    def test_get_programs(self):
        pid_list = [
            '0 <-> 2',
            '1 <-> 1',
            '2 <-> 0, 3, 4',
            '3 <-> 2, 4',
            '4 <-> 2, 3, 6',
            '5 <-> 6',
            '6 <-> 4, 5'
        ]
        pipetown = PipeTown(pid_list)
        pipetown.initialize_nodes()
        print(pipetown.get_programs(0))
        assert pipetown.get_programs(0) == {0, 2, 3, 4, 5, 6}


if __name__ == '__main__':
    unittest.main()
