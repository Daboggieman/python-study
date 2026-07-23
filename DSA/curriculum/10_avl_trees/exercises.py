# DSA Exercise 10: AVL Trees
# Run this script with: python exercises.py


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


def get_height(node):
    return node.height if node else 0


def get_balance(node):
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)


# TODO: Exercise 1 - single right rotation (fixes Left-Left case)
def rotate_right(y):
    pass


# TODO: Exercise 2 - single left rotation (fixes Right-Right case)
def rotate_left(x):
    pass


# TODO: Exercise 3 - standard BST insert + rebalance using the 4 cases
def insert(node, value):
    pass


# TODO: Exercise 4 - confirm rotations preserve sorted order
def inorder(node, result=None):
    pass


if __name__ == "__main__":
    root = None
    for value in [1, 2, 3, 4, 5, 6, 7]:  # sorted insert -- the BST killer
        root = insert(root, value)

    print("height after sorted insert:", get_height(root))  # should be small, e.g. 2 or 3
    print(inorder(root))                                       # [1, 2, 3, 4, 5, 6, 7]
