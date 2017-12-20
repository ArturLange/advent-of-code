from itertools import chain


def get_watcher_cycle(watcher_length):
    return chain(
        range(watcher_length),
        (watcher_length - 1 - x for x in range(1, watcher_length - 1))
    )


class State:
    def __init__(self, firewall):
        self.firewall = firewall
        self.watchers_cycles = {watcher: list(get_watcher_cycle(firewall[watcher]))
                                for watcher in firewall}

    def get_watcher_position(self, time, watcher_number):
        cycle_length = len(self.watchers_cycles[watcher_number])
        time %= cycle_length
        return self.watchers_cycles[watcher_number][time]

    def get_safe_pass(self):
        wait_time = 0
        while not all(
                (self.get_watcher_position(wait_time + watcher_number, watcher_number) != 0
                 for watcher_number in self.firewall)
        ):
            wait_time += 1
        return wait_time


if __name__ == '__main__':
    with open('inputs/day13', 'r') as input_file:
        firewall = {}
        for line in input_file.readlines():
            line = line.split(':')
            firewall[int(line[0])] = int(line[1])
        state = State(firewall)
        print(state.get_safe_pass())
