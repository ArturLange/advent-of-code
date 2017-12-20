import unittest

from day13 import count_path_severity, did_get_caught, get_free_path, get_watcher_cycle


class TestDay13(unittest.TestCase):
    def test_count_path_severity(self):
        firewall = {
            0: 3,
            1: 2,
            4: 4,
            6: 4
        }
        assert count_path_severity(firewall) == 24

    def test_get_free_path(self):
        firewall = {
            0: 3,
            1: 2,
            4: 4,
            6: 4
        }
        assert get_free_path({3: 27}) == 0
        assert get_free_path({0: 2}) == 1
        print(f'have to wait: {get_free_path(firewall)}')

    def test_state(self):
        firewall = {
            0: 3,
            1: 2,
            4: 4,
            6: 4
        }
        expected = {
            0: [0, 'down']
        }
        # assert get_state(firewall, 0) ==

    def test_did_get_caught(self):
        firewall = {
            0: 3,
            1: 2,
            4: 4,
            6: 4
        }
        assert did_get_caught(firewall)
        state = {
            0: [2, 'up'],
            1: [0, 'down'],
            4: [2, 'up'],
            6: [2, 'up']
        }
        assert not did_get_caught(firewall, state)

    def test_get_watcher_cycle(self):
        assert list(get_watcher_cycle(2)) == [0, 1]
        assert list(get_watcher_cycle(3)) == [0, 1, 2, 1]
        assert list(get_watcher_cycle(4)) == [0, 1, 2, 3, 2, 1]



if __name__ == '__main__':
    unittest.main()
