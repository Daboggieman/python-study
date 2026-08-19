# DSA Exercise 08: Binary Trees
# Run this script with: python exercises.py

from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# TODO: Exercise 1 - Left, Node, Right
def inorder(node, result=None):
    pass


# TODO: Exercise 2 - Node, Left, Right
def preorder(node, result=None):
    pass


# TODO: Exercise 3 - Left, Right, Node
def postorder(node, result=None):
    pass


# TODO: Exercise 4 - breadth-first, level by level
def level_order(root):
    pass


# TODO: Exercise 5 - height of the tree (empty = -1, single node = 0)
def height(node):
    pass


# TODO: Exercise 6 - swap left/right at every node (mirror the tree)
def mirror(node):
    pass


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(inorder(root))     # [4, 2, 5, 1, 3]
    print(preorder(root))    # [1, 2, 4, 5, 3]
    print(postorder(root))   # [4, 5, 2, 3, 1]
    print(level_order(root)) # [1, 2, 3, 4, 5]
    print(height(root))      # 2

    mirror(root)
    print(inorder(root))     # [3, 1, 5, 2, 4]
