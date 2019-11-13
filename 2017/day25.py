from enum import Enum
from typing import Set


class State(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5


class Tape:
    ones: Set
    position: int
    steps: int
    state: State
    state_functions: dict

    def __init__(self):
        self.ones = set()
        self.position = 0
        self.state = State.A
        self.steps = 0
        self.state_functions = {
            State.A: self.do_state_a,
            State.B: self.do_state_b,
            State.C: self.do_state_c,
            State.D: self.do_state_d,
            State.E: self.do_state_e,
            State.F: self.do_state_f,
        }

    def process_one_turn(self):
        self.state_functions[self.state]()
        self.steps += 1

    def do_state_a(self):
        if self.position in self.ones:
            self.ones.remove(self.position)
            self.position += 1
            self.state = State.F
        else:
            self.ones.add(self.position)
            self.position += 1
            self.state = State.B

    def do_state_b(self):
        if self.position in self.ones:
            self.position -= 1
            self.state = State.C
        else:
            self.position -= 1
            self.state = State.B

    def do_state_c(self):
        if self.position in self.ones:
            self.ones.remove(self.position)
            self.position += 1
            self.state = State.C
        else:
            self.ones.add(self.position)
            self.position -= 1
            self.state = State.D

    def do_state_d(self):
        if self.position in self.ones:
            self.position += 1
            self.state = State.A
        else:
            self.ones.add(self.position)
            self.position -= 1
            self.state = State.E

    def do_state_e(self):
        if self.position in self.ones:
            self.ones.remove(self.position)
            self.position -= 1
            self.state = State.D
        else:
            self.ones.add(self.position)
            self.position -= 1
            self.state = State.F

    def do_state_f(self):
        if self.position in self.ones:
            self.ones.remove(self.position)
            self.position -= 1
            self.state = State.E
        else:
            self.ones.add(self.position)
            self.position += 1
            self.state = State.A


if __name__ == '__main__':
    steps_to_do = 12964419
    tape = Tape()

    for _ in range(steps_to_do):
        tape.process_one_turn()
    print(len(tape.ones))
