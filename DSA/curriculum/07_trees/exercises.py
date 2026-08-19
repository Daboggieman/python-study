# DSA Exercise 07: Trees (General N-ary Trees)
# Run this script with: python exercises.py

from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


# TODO: Exercise 1 - depth-first traversal, print indented by depth
def dfs(node, depth=0):
    pass


# TODO: Exercise 2 - breadth-first (level-order) traversal, print level by level
def bfs(root):
    pass


# TODO: Exercise 3 - return the height of the tree (longest root-to-leaf path, in edges)
def tree_height(node):
    pass


# TODO: Exercise 4 - count how many leaf nodes (no children) exist
def count_leaves(node):
    pass


if __name__ == "__main__":
    root = TreeNode("CEO")
    vp_eng = TreeNode("VP Engineering")
    vp_sales = TreeNode("VP Sales")
    root.add_child(vp_eng)
    root.add_child(vp_sales)
    vp_eng.add_child(TreeNode("Engineer A"))
    vp_eng.add_child(TreeNode("Engineer B"))
    vp_sales.add_child(TreeNode("Sales Rep A"))

    dfs(root)
    print("---")
    bfs(root)
    print("Height:", tree_height(root))       # 2
    print("Leaves:", count_leaves(root))      # 3
