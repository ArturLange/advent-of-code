import itertools
import math
import string
from typing import Any, Dict, List, Set, Tuple

with open('inputs/day13') as input_file:
    departure_time = int(input_file.readline().strip())
    buses = input_file.readline().strip().split(',')


test_buses = '1789,37,47,1889'.split(',')
test_buses = '1789,x,47,1889,x,465,12'.split(',')

def part1(departure_time: int, buses: List[str]):
    buses_set: Set[int] = {int(x) for x in buses if x != 'x'}
    times = {}
    for bus in buses_set:
        i = 1
        while bus * i < departure_time:
            i += 1
        times[bus] = i * bus

    earliest_bus =  sorted(times.items(), key=lambda x: x[1])[0]
    return earliest_bus[0] * (earliest_bus[1]-departure_time)


def check_timestamp(timestamp: int, buses):
    for bus_id, time_ in buses:
        if (timestamp + time_) % bus_id != 0:
            return False
    return True




def part2(buses: List[str]):
    buses_set: Set[Tuple[int, int]] = {(int(bus_id), index) for index, bus_id in enumerate(buses) if bus_id != 'x'}
    buses_slowest: List[Tuple[int, int]] = sorted(buses_set, key=lambda x: x[0])
    slowest_bus = buses_slowest.pop()
    diff = slowest_bus[0]
    timestamp = slowest_bus[0] - slowest_bus[1]
    remainders = tuple((timestamp+bus[1]) % bus[0] for bus in buses_set)
    remainders_zeros = remainders.count(0)
    while remainders.count(0) != len(remainders):
        while remainders.count(0) == remainders_zeros:
            timestamp += diff
            remainders = tuple((timestamp+bus[1]) % bus[0] for bus in buses_set)
        for bus in buses_set:
            if (timestamp+bus[1]) % bus[0] == 0:
                diff = math.lcm(diff, bus[0])
        remainders_zeros = remainders.count(0)
        
    return timestamp



if __name__ == "__main__":
    print(part1(departure_time, buses))
    # print(part2(buses))

    import cProfile as profile

    profile.run('print(part2(buses))')
