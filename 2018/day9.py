from blist import blist

with open('day9_input') as input_file:
    numbers =  input_file.readlines()


def part1(players, last):
    marbles = blist([0,1])
    current = 1
    players_scores = [0] * players
    current_player = 1
    for marble in range(2, last+1):
        if marble % 23 == 0 and marble != 0:
            players_scores[current_player] += marble
            to_remove = (current - 7 + len(marbles) - 1) % (len(marbles)) + 1
            players_scores[current_player] += marbles.pop(to_remove)
            current = to_remove
        else:
            marbles_len = len(marbles)
            current = (current + 2 - 1) % marbles_len + 1
            marbles.insert(current, marble)

        current_player = (current_player + 1) % len(players_scores)
    return max(players_scores)



# print(part1(9, 25))
# print(part1(476, 71431))
import profile
profile.run('print(part1(476, 714310))')
# print(part1(476, 71431 * 100)) # part 2
