import cProfile as profile
from collections import Counter, deque
from dataclasses import dataclass
from itertools import chain
from typing import Deque, Dict, FrozenSet, List, Optional, Set, Tuple


class Component:
    ports: FrozenSet[int]
    value: int
    is_same: bool

    def __init__(self, *args):
        self.ports = frozenset(args)
        self.value = sum(args)
        self.is_same = len(self.ports) == 1

    def __eq__(self, other):
        return self.ports == other.ports

    def __hash__(self):
        return hash(self.ports)

    def __contains__(self, item):
        return item in self.ports


class OrientedComponent:
    start: int
    end: int
    component: Component
    value: int

    def __init__(self, component: Component, flipped: bool = False):
        self.component = component
        if component.is_same:
            self.start = sorted(component.ports)[0]
            self.end = self.start
        elif flipped:
            self.end, self.start = sorted(component.ports)
        else:
            self.start, self.end = sorted(component.ports)

        self.value = self.component.value

    def __str__(self):
        return f'({self.start}, {self.end})'

    def __repr__(self):
        return str(self)


Bridge = List[OrientedComponent]


def create_component(input_: str) -> Component:
    a, b = input_.split('/')
    return Component(int(a), int(b))


def get_bridge_strength(bridge: Bridge) -> int:
    return sum(x.value for x in bridge)


def get_bridge_strength_and_len_with_sames(bridge: Bridge) -> Tuple[int, int]:
    all_values = set()
    for comp in bridge:
        all_values = all_values.union({comp.start, comp.end})
    same_values = [x * 2 for x in all_values if x in sames]
    strength = get_bridge_strength(bridge) + sum(same_values)
    length = len(bridge) + len(same_values)
    return strength, length


def filter_components_by_pins(pin_number: int, components: Set[Component]):
    return filter(lambda x: pin_number in x, components)


class BridgeTree:
    __slots__ = ['max_value', 'bridge', 'value', 'len']

    def __init__(self, bridge: Bridge, max_value: Dict[str, int]):
        self.max_value = max_value
        self.bridge: Bridge = bridge
        self.value, self.len = get_bridge_strength_and_len_with_sames(
            self.bridge)
        if (self.len > self.max_value['len'] or (
            self.len == self.max_value['len'] and self.value > self.max_value[
            'max'])):
            self.max_value.update({'max': self.value, 'len': self.len})
        # self.children: List[BridgeTree] = self.get_children(
        #     components - set(bridge))
        print(self.bridge, self.max_value)

    def get_children(self, components: Set[Component]):
        last = self.bridge[-1].end
        for component in components:
            if last == min(component.ports):
                yield BridgeTree(
                    self.bridge + [OrientedComponent(component)],
                    self.max_value)
            if last == max(component.ports):
                yield BridgeTree(
                    self.bridge + [OrientedComponent(component, flipped=True)],
                    self.max_value)

    def __repr__(self):
        return f'{self.bridge}'


def get_depth_first_nodes(root):
    stack: Deque = deque([root])
    while stack:
        cur_node = stack.popleft()
        new_comps = components - {x.component for x in cur_node.bridge}
        for child in cur_node.get_children(new_comps):
            stack.appendleft(child)


def improve_components(components: Set[Component]):
    sames: Set[int] = {
        sorted(comp.ports)[0] for comp in components if comp.is_same
    }
    components = set(filter(lambda x: not x.is_same, components))
    return sames, components


if __name__ == '__main__':
    with open('inputs/day24') as input_file:
        lines = input_file.readlines()
        components: Set[Component] = {
            create_component(x) for x in lines}

        sames, components = improve_components(components)

    max_value = {'max': 0, 'len': 0}

    bridge_tree = BridgeTree([OrientedComponent(Component(0, 0))], max_value)

    get_depth_first_nodes(bridge_tree)

    print(max_value)
