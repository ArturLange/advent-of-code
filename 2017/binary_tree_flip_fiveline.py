class Node:
    left = None
    right = None

    def __init__(self, value):
        self.value = value


def flip_binary_tree(root: Node):
    for leaf in [root.left, root.right]:
        if leaf is not None:
            flip_binary_tree(leaf)
    if root.left is not None and root.right is not None:
        root.right, root.left = root.left, root.right


if __name__ == '__main__':
    root = Node(1)
    root.left, root.right = Node(2), Node(3)
    root.right.left, root.right.right = Node(4), Node(5)

    flip_binary_tree(root)
    print(root)
