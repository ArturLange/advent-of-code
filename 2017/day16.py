import re
from typing import List


def get_functions(operations) -> list:
    functions = []
    for operation in operations:
        spin_operation = re.compile(r's[0-9]*').fullmatch(operation)
        if spin_operation:
            functions.append(lambda x: spin(int(operation[1:]), x))
        else:
            exchange_operation = re.compile(r'x(?P<a>[0-9]*)/(?P<b>[0-9]*)').fullmatch(operation)
            if exchange_operation:
                a, b = int(exchange_operation.group('a')), int(exchange_operation.group('b'))
                functions.append(lambda x: exchange(a, b, x))
            else:
                partner_operation = re.compile(r'p(?P<a>[a-z])/(?P<b>[a-z])').fullmatch(operation)
                a, b = partner_operation.group('a'), partner_operation.group('b')
                partner_a_b = lambda x: partner(a, b, x)
                functions.append(lambda x: partner(a, b, x))
    return functions


def spin(number: int, list_: list):
    new_list: list = list_[-number:]
    new_list.extend(list_[:-number])
    return new_list


def exchange(a: int, b: int, list_: list):
    list_[a], list_[b] = list_[b], list_[a]
    return list_


def partner(a_name: str, b_name: str, list_: list):
    index_a = list_.index(a_name)
    index_b = list_.index(b_name)
    list_[index_a], list_[index_b] = list_[index_b], list_[index_a]
    return list_


def parse_operations(operations: List[str], list_):
    # for operation in operations:
    #     spin_operation = re.compile(r's[0-9]*').fullmatch(operation)
    #     if spin_operation:
    #         list_ = spin(int(operation[1:]), list_)
    #     else:
    #         exchange_operation = re.compile(r'x(?P<a>[0-9]*)/(?P<b>[0-9]*)').fullmatch(operation)
    #         if exchange_operation:
    #             a, b = int(exchange_operation.group('a')), int(exchange_operation.group('b'))
    #             list_ = exchange(a, b, list_)
    #         else:
    #             partner_operation = re.compile(r'p(?P<a>[a-z])/(?P<b>[a-z])').fullmatch(operation)
    #             a, b = partner_operation.group('a'), partner_operation.group('b')
    #             list_ = partner(a, b, list_)
    for function_ in get_functions(operations):
        list_ = function_(list_)
    return list_


def get_list_permutation(list_):
    base_list = list('abcdefghijklmnop')
    permutation_list = [base_list.index(letter) for letter in list_]
    return permutation_list


def permute(list_: list, permutation: list) -> list:
    new_list = [list_[index] for index in permutation]
    return new_list


def get_permutation_order(permutation: List[int]) -> int:
    base_list = list('abcdefghijklmnop')
    list_ = permute(base_list, permutation)
    order = 1
    while list_ != base_list:
        list_ = permute(list_, permutation)
        order += 1
    return order


def look_for_cycle(operations):
    start_list = list('abcdefghijklmnop')
    list_ = parse_operations(operations, start_list)
    count = 1
    while list_ != start_list:
        list_ = parse_operations(operations, list_)
        count += 1
    return count


class Permutation:
    def __init__(self, operations):
        self.operations = operations
        self.base_list = list('abcdefghijklmnop')
        self.list = list('abcdefghijklmnop')

    def make_operation(self, operation):
        spin_operation = re.compile(r's[0-9]*').fullmatch(operation)
        if spin_operation:
            self.spin(int(operation[1:]))
        else:
            exchange_operation = re.compile(r'x(?P<a>[0-9]*)/(?P<b>[0-9]*)').fullmatch(operation)
            if exchange_operation:
                a, b = int(exchange_operation.group('a')), int(exchange_operation.group('b'))
                self.exchange(a, b)
            else:
                partner_operation = re.compile(r'p(?P<a>[a-z])/(?P<b>[a-z])').fullmatch(operation)
                a, b = partner_operation.group('a'), partner_operation.group('b')
                self.partner(a, b)

    def execute_all(self):
        for operation in self.operations:
            self.make_operation(operation)

    def spin(self, number: int):
        new_list: list = self.list[-number:]
        new_list.extend(self.list[:-number])
        self.list = new_list

    def exchange(self, a: int, b: int):
        self.list[a], self.list[b] = self.list[b], self.list[a]

    def partner(self, a_name: str, b_name: str):
        index_a = self.list.index(a_name)
        index_b = self.list.index(b_name)
        self.list[index_a], self.list[index_b] = self.list[index_b], self.list[index_a]

    def look_for_cycle(self):
        cycle = 0
        while True:
            self.execute_all()
            cycle += 1
            if self.list == self.base_list:
                return cycle

    def execute_x_times(self, times):
        cycle_time = self.look_for_cycle()
        for _ in range(times % cycle_time):
            self.execute_all()


if __name__ == '__main__':
    with open('inputs/day16', 'r') as input_file:
        operations = input_file.readline().split(',')
        permutation = Permutation(operations)
        permutation.execute_x_times(1)
        print(''.join(permutation.list))
        permutation = Permutation(operations)
        permutation.execute_x_times(1000000000)
        print(''.join(permutation.list))
