# DSA Exercise 11: Graphs
# Run this script with: python exercises.py

from collections import deque
import heapq

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"],
}

weighted_graph = {
    "A": [("B", 4), ("C", 1)],
    "B": [("A", 4), ("D", 1)],
    "C": [("A", 1), ("D", 5)],
    "D": [("B", 1), ("C", 5)],
}


# TODO: Exercise 1
def dfs(g, start, visited=None):
    pass


# TODO: Exercise 2
def bfs(g, start):
    pass


# TODO: Exercise 3
def has_path(g, start, end):
    pass


# TODO: Exercise 4 - unweighted shortest path length using BFS
def shortest_path_length(g, start, end):
    pass


# TODO: Exercise 5 - Dijkstra's algorithm for weighted graphs
def dijkstra(g, start):
    pass


if __name__ == "__main__":
    print(dfs(graph, "A"))
    print(bfs(graph, "A"))
    print(has_path(graph, "A", "D"))    # True
    print(shortest_path_length(graph, "A", "D"))  # 2
    print(dijkstra(weighted_graph, "A"))  # {'A': 0, 'B': 4, 'C': 1, 'D': 5}
