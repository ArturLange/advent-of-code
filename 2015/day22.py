from collections import deque, namedtuple
from itertools import product

BossStats = namedtuple('BossStats', ('hp', 'damage'))
PlayerStats = namedtuple('PlayerStats', ('hp', 'mana'))

BOSS_STATS = BossStats(hp=58, damage=9)

PLAYER_HP = 50
PLAYER_MANA = 500

PLAYER_STATS = PlayerStats(PLAYER_HP, PLAYER_MANA)

SPELLS = ('Magic Missile', 'Drain', 'Shield', 'Poison', 'Recharge')
SPELLS_MANA = (53, 73, 113, 173, 229)


class SpellException(Exception):
    pass


class NoManaException(SpellException):
    pass


class EffectAlreadyPresentException(SpellException):
    pass


class NotEnoughSpellsException(Exception):
    pass


class EndOfFightException(Exception):
    pass


class FightSimulation:
    def __init__(self, boss_stats: BossStats, player_stats: PlayerStats, spells: tuple, verbose: bool = False):
        self.boss_stats = boss_stats
        self.player_stats = player_stats
        self.verbose = verbose
        self.spells = deque(spells)

        self.player_mana = player_stats.mana
        self.player_hp = player_stats.hp
        self.boss_hp = boss_stats.hp
        self.fight_ended = False
        self.fight_result = None

        self.shield = 0
        self.poison = 0
        self.recharge = 0

        self.mana_spent = 0

    @property
    def player_armor(self):
        if self.shield:
            return 7
        else:
            return 0

    def hit_boss(self, damage: int):
        self.boss_hp -= damage
        if self.boss_hp <= 0:
            self.fight_ended = True
            self.fight_result = 'Player won'
            raise EndOfFightException

    def hit_player(self, damage: int):
        self.player_hp -= damage
        if self.player_hp <= 0:
            self.fight_ended = True
            self.fight_result = 'Boss won'
            raise EndOfFightException

    def apply_poison(self):
        if self.poison:
            if self.verbose:
                print(
                    f'Poison deals 3 damage; its timer is now {self.poison}.')
            self.hit_boss(3)
            self.poison -= 1

    def apply_recharge(self):
        if self.recharge:
            self.player_mana += 101
            self.recharge -= 1
            if self.verbose:
                print(
                    f'Recharge provides 101 mana; its timer is now {self.recharge}.')
                if not self.recharge:
                    print('Recharge wears off.')

    def apply_shield(self):
        if self.shield:
            self.shield -= 1
            if self.verbose:
                print(f"Shield's timer is now {self.shield}.")
                if not self.shield:
                    print('Shield wears off, decreasing armor by 7.')

    def cast(self, spell: str):
        if spell == 'Magic Missile':
            self.cast_magic_missile()
        if spell == 'Poison':
            self.cast_poison()
        if spell == 'Recharge':
            self.cast_recharge()
        if spell == 'Drain':
            self.cast_drain()
        if spell == 'Shield':
            self.cast_shield()

    def cast_magic_missile(self):
        cost = 53
        if self.player_mana < cost:
            raise NoManaException

        self.player_mana -= cost
        self.mana_spent += cost
        self.hit_boss(4)
        if self.verbose:
            print('Player casts Magic Missile, dealing 4 damage.')

    def cast_poison(self):
        cost = 173
        if self.player_mana < cost:
            raise NoManaException
        if self.poison:
            raise EffectAlreadyPresentException

        self.player_mana -= cost
        self.mana_spent += cost
        self.poison = 6
        if self.verbose:
            print('Player casts Poison.')

    def cast_recharge(self):
        cost = 229
        if self.player_mana < cost:
            raise NoManaException
        if self.recharge:
            raise EffectAlreadyPresentException

        self.player_mana -= cost
        self.mana_spent += cost
        self.recharge = 5
        if self.verbose:
            print('Player casts Recharge.')

    def cast_shield(self):
        cost = 113
        if self.player_mana < cost:
            raise NoManaException
        if self.shield:
            raise EffectAlreadyPresentException

        self.player_mana -= cost
        self.mana_spent += cost
        self.shield = 6
        if self.verbose:
            print('Player casts Shield, increasing armor by 7.')

    def cast_drain(self):
        cost = 73
        if self.player_mana < cost:
            raise NoManaException

        self.player_mana -= cost
        self.mana_spent += cost
        self.hit_boss(2)
        self.player_hp += 2
        if self.verbose:
            print('Player casts Drain, dealing 2 damage, and healing 2 hit points.')

    def get_next_spell(self):
        try:
            spell_num = self.spells.popleft()
        except IndexError as e:
            raise NotEnoughSpellsException(e)
        return SPELLS[spell_num]

    def player_turn(self):
        spell = self.get_next_spell()

        if self.verbose:
            print('-- Player turn --')
            print(
                f'- Player has {self.player_hp} hit points, {self.player_armor} armor, {self.player_mana} mana')
            print(f'- Boss has {self.boss_hp} hit points')

        self.apply_shield()
        self.apply_poison()
        self.apply_recharge()

        self.cast(spell)

        if self.verbose:
            print()

    def boss_turn(self):
        if self.verbose:
            print('-- Boss turn --')
            print(
                f'- Player has {self.player_hp} hit points, {self.player_armor} armor, {self.player_mana} mana')
            print(f'- Boss has {self.boss_hp} hit points')

        self.apply_shield()
        self.apply_poison()
        self.apply_recharge()

        if not self.player_armor:
            self.hit_player(self.boss_stats.damage)
            if self.verbose:
                print(f'Boss attacks for {self.boss_stats.damage} damage!')
        else:
            dmg: int = max((self.boss_stats.damage - self.player_armor, 1))
            self.hit_player(dmg)
            if self.verbose:
                print(
                    f'Boss attacks for {self.boss_stats.damage} - {self.player_armor} = {dmg} damage!')

        if self.verbose:
            print()

    def simulate(self):
        try:
            while not self.fight_ended:
                self.player_turn()
                self.boss_turn()
            if self.fight_ended:
                print(self.mana_spent)
                return self.fight_result
        except EndOfFightException:
            print(self.mana_spent)
            return self.fight_result
        except Exception as e:
            return None

    def simulate_for_minimal_mana(self):
        try:
            while not self.fight_ended:
                self.player_turn()
                self.boss_turn()
            if self.fight_ended:
                if self.fight_result == 'Player won':
                    return self.mana_spent
        except EndOfFightException:
            if self.fight_result == 'Player won':
                return self.mana_spent
        except Exception as e:
            return None


if __name__ == "__main__":
    # boss_stats = BossStats(hp=13, damage=8)
    # player_stats = PlayerStats(hp=10, mana=250)

    # simulation = FightSimulation(
    #     boss_stats, player_stats, (3, 0, 0, 0), verbose=True)
    # print(simulation.simulate())

    # boss_stats = BossStats(hp=14, damage=8)

    # simulation = FightSimulation(
    #     boss_stats, player_stats, (4, 2, 1, 3, 0), verbose=True)
    # print(simulation.simulate())

    prepare_spells_for_turns = 1
    min_mana = float('inf')
    while True:
        spell_options = product(
            range(len(SPELLS)), repeat=prepare_spells_for_turns)
        for option in spell_options:
            simulation = FightSimulation(
                BOSS_STATS, PLAYER_STATS, option, verbose=False)
            total_mana = simulation.simulate_for_minimal_mana()
            if total_mana:
                print(total_mana)
            if total_mana and total_mana < min_mana:
                print(f'#########################################{total_mana}')
                min_mana = total_mana
        prepare_spells_for_turns += 1
        print(f'Starting to plan for {prepare_spells_for_turns} turns ')
