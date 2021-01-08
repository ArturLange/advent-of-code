from datetime import datetime

with open('day4_input') as input_file:
    lines = input_file.readlines()
    times = sorted([
        (
            datetime.strptime(line[1:17], '%Y-%m-%d %H:%M'), 
            line[19:]
        )
        for line in lines
    ],
    key = lambda x: x[0])

    for time in times:
        print(' '.join([str(time[0]), time[1]]))

def part1():
    guards = dict()
    for time in times:
        if time[1].startswith('Guard'):
            guard_id = int(time[1].split()[1][1:])
            if guard_id not in guards:
                guards[guard_id] = [0 for i in range(60)]
    asleep_time = 0
    for time in times:
        if time[1].startswith('Guard'):
            guard_id = int(time[1].split()[1][1:])
        if time[1] == 'falls asleep\n':
            asleep_time = time[0].minute
        if time[1] == 'wakes up\n':
            for minute in range(asleep_time, time[0].minute):
                guards[guard_id][minute] += 1

    # breakpoint()
    worst_guard =guard_id
    worst_minutes = sum(guards[guard_id])
    for id, minutes in guards.items():
        print(guard_id, minutes)
        if sum(minutes) > worst_minutes:
            # breakpoint()
            worst_guard = id
            worst_minutes = sum(minutes)

    print(worst_guard)
    worst_minute = 0, guards[worst_guard][0]
    for minute, number in enumerate(guards[worst_guard]):
        if number > worst_minute[1]:
            worst_minute = minute, number
    print(worst_minute)
        
    print(guards)

    return(worst_guard * worst_minute[0])



def part2():
    guards = dict()
    for time in times:
        if time[1].startswith('Guard'):
            guard_id = int(time[1].split()[1][1:])
            if guard_id not in guards:
                guards[guard_id] = [0 for i in range(60)]
    asleep_time = 0
    for time in times:
        if time[1].startswith('Guard'):
            guard_id = int(time[1].split()[1][1:])
        if time[1] == 'falls asleep\n':
            asleep_time = time[0].minute
        if time[1] == 'wakes up\n':
            for minute in range(asleep_time, time[0].minute):
                guards[guard_id][minute] += 1

    # breakpoint()
    worst_guard =guard_id
    worst_minutes = max(guards[guard_id])
    for id, minutes in guards.items():
        print(guard_id, minutes)
        if max(minutes) > worst_minutes:
            # breakpoint()
            worst_guard = id
            worst_minutes = max(minutes)

    print(worst_guard)
    worst_minute = 0, guards[worst_guard][0]
    for minute, number in enumerate(guards[worst_guard]):
        if number > worst_minute[1]:
            worst_minute = minute, number
    print(worst_minute)
        
    print(guards)

    return(worst_guard * worst_minute[0])

print(part2())
