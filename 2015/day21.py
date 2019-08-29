from itertools import chain, combinations, product
from typing import Tuple

PLAYER_HITPOINTS = 100

BOSS_HITPOINTS = 100
BOSS_DMG = 8
BOSS_ARMOR = 2

Stats = Tuple[int, int ,int]

BOSS_STATS: Stats = (BOSS_HITPOINTS, BOSS_DMG, BOSS_ARMOR)

WEAPONS = (
    (8, 4),
    (10, 5),
    (25, 6),
    (40, 7),
    (74, 8),
)

ARMOR = (
    (0, 0),
    (13, 1),
    (31, 2),
    (53, 3),
    (75, 4),
    (102, 5),
)

RINGS = (
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
)

def simulate_fight(player_stats: Stats, boss_stats: Stats, verbose: bool=False) -> bool:
    player_hit = player_stats[1] - boss_stats[2]
    boss_hit = boss_stats[1] - player_stats[2]
    player_hp = player_stats[0]
    boss_hp = boss_stats[0]
    while player_hp > 0 and boss_hp > 0:
        boss_hp -= player_hit
        if verbose:
            print(f'The player deals {player_stats[1]}-{boss_stats[2]} = {player_hit} damage; the boss goes down to {boss_hp} hit points.')
        if boss_hp <= 0:
            return True
        player_hp -= boss_hit
        if verbose:
            print(f'The boss deals {boss_stats[1]}-{player_stats[2]} = {boss_hit} damage; the player goes down to {player_hp} hit points.')
        if player_hp <=0:
            return False



EqInput = Tuple[int, int, tuple]

def get_stats_from_eq(eq_input: EqInput):
    armor = 0
    cost, dmg = WEAPONS[eq_input[0]]

    armor += ARMOR[eq_input[1]][1]
    cost += ARMOR[eq_input[1]][0]

    if eq_input[2]:
        cost += RINGS[eq_input[2][0]][0]
        dmg += RINGS[eq_input[2][0]][1]
        armor += RINGS[eq_input[2][0]][2]
    if len(eq_input[2]) == 2:
        cost += RINGS[eq_input[2][1]][0]
        dmg += RINGS[eq_input[2][1]][1]
        armor += RINGS[eq_input[2][1]][2]

    return cost, dmg, armor


def part1():
    weapon_choices = range(len(WEAPONS))
    armor_choices = range(len(ARMOR))
    ring_choices = chain(combinations(range(len(RINGS)), 2), combinations(range(len(RINGS)), 1), combinations(range(len(RINGS)), 0))

    all_options = product(weapon_choices, armor_choices, ring_choices)
    min_cost = None
    for eq in all_options:
        cost, dmg, armor = get_stats_from_eq(eq)
        stats = (PLAYER_HITPOINTS, dmg, armor)
        if simulate_fight(stats, BOSS_STATS) and (min_cost is None or (min_cost is not None and cost < min_cost)):
            min_cost = cost
    return min_cost

def part2():
    weapon_choices = range(len(WEAPONS))
    armor_choices = range(len(ARMOR))
    ring_choices = chain(combinations(range(len(RINGS)), 2), combinations(range(len(RINGS)), 1), combinations(range(len(RINGS)), 0))

    all_options = product(weapon_choices, armor_choices, ring_choices)
    max_cost = 0
    for eq in all_options:
        cost, dmg, armor = get_stats_from_eq(eq)
        stats = (PLAYER_HITPOINTS, dmg, armor)
        if not simulate_fight(stats, BOSS_STATS) and cost > max_cost:
            max_cost = cost
    return max_cost

if __name__ == "__main__":
    # cost, dmg, armor = get_stats_from_eq((1, 1, (0,)))
    # player_stats = 100, dmg, armor
    # result = simulate_fight(player_stats, BOSS_STATS)
    # print(simulate_fight((8, 5, 5), (12, 7, 2), verbose=True))
    print(part1())
    print(part2())
