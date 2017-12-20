from typing import List


class Graph:

    def __init__(self, pid_list: List[str]):
        self.pid_list = pid_list

        self.programs = {}
        self.nodes_and_vertices = []

    def initialize_nodes(self):
        for line in self.pid_list:
            line = line.split('<->')
            key = int(line[0])
            node = [0] * len(self.pid_list)
            for i in (int(x) for x in line[1].split(',')):
                node[i] = 1
            node[key] = 1
            self.nodes_and_vertices.append(node)

    def initialize_graph(self):
        self.initialize_nodes()
        for _ in range(1):
            node = self.nodes_and_vertices[i]
            for j in range(len(node)):
                if node[j] == 1:
                    self.establish_connection(i, j)

    def establish_connection(self, node1_number, node2_number):
        node1 = self.nodes_and_vertices[node1_number]
        node2 = self.nodes_and_vertices[node2_number]
        connected = set([
                            i for i
                            in range(len(node2))
                            if node2[i] == 1]
                        +
                        [
                            i for i
                            in range(len(node1))
                            if node1[i] == 1
                        ])
        for i in connected:
            node1[i] = 1
            node2[i] = 1

    def count_connections(self, pid):
        return self.nodes_and_vertices[pid].count(1)


if __name__ == '__main__':
    with open('inputs/day12', 'r') as input_file:
        pid_list = [line.replace('\n', '') for line in input_file.readlines()]
        graph = Graph(pid_list)
        graph.initialize_graph()
        graph.initialize_nodes()
        print(graph.count_connections(0))
