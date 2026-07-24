# DSA Exercise 09: Binary Search Trees
# Run this script with: python exercises.py


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# TODO: Exercise 1
def insert(root, value):
    pass


# TODO: Exercise 2
def search(root, target):
    pass


def find_min(node):
    while node.left:
        node = node.left
    return node


# TODO: Exercise 3
def delete(root, value):
    pass


# TODO: Exercise 4
def inorder(node, result=None):
    pass


# TODO: Exercise 5
# Return the height of a BST (empty = -1, single node = 0). Reuse your
# solution from the Binary Trees lesson if you like.
def height(node):
    pass


if __name__ == "__main__":
    root = None
    for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        root = insert(root, value)

    print(inorder(root))          # sorted list of all values
    print(search(root, 6))         # True
    print(search(root, 99))        # False

    root = delete(root, 3)          # delete a node with two children
    print(inorder(root))

    # Compare balanced vs unbalanced height for the same 5 values
    balanced = None
    for value in [3, 1, 4, 5, 2]:
        balanced = insert(balanced, value)
    print("balanced-ish height:", height(balanced))

    unbalanced = None
    for value in [1, 2, 3, 4, 5]:
        unbalanced = insert(unbalanced, value)
    print("sorted-insert height:", height(unbalanced))
