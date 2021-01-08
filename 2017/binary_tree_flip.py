from collections import deque


class Node:
    left = None
    right = None

    def __init__(self, value):
        self.value = value


class Tree:
    flipped = set()
    path = deque()

    def get_down(self, node: Node):
        if node.left is not None and node.left.value not in self.flipped:
            return node.left
        if node.right is not None and node.right.value not in self.flipped:
            return node.right
        return False

    def get_way_down(self, node):
        while self.get_down(node):

    @staticmethod
    def flip(node):
        node.right, node.left = node.left, node.right

    def flip_binary_tree(self, root):
        self.path.appendleft(root)
        node = root
        while not
