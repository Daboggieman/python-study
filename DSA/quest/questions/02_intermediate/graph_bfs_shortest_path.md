# Graph BFS Shortest Path

Source: graph_bfs_shortest_path

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Given a graph as an adjacency-list dictionary (unweighted, undirected), write a function that returns the length (number of edges) of the shortest path between `start` and `end` using BFS. Return `-1` if no path exists.

Expected function
```python
def shortest_path_length(graph, start, end):
    pass
```


Here is a possible program to test your function :
```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
    "F": [],
}
print(shortest_path_length(graph, "A", "E"))
print(shortest_path_length(graph, "A", "F"))
```

And its output :
```text
3
-1
```
