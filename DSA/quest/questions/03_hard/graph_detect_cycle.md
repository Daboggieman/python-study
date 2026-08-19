# Graph Detect Cycle

Source: graph_detect_cycle

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Given a **directed** graph as an adjacency-list dictionary, write a function that detects whether it contains a cycle. Use DFS with node coloring (unvisited / in-progress / done) rather than a simple visited set, since a simple visited set alone cannot distinguish "still on the current path" from "already fully explored" in a directed graph.

Expected function
```python
def has_cycle(graph):
    pass
```


Here is a possible program to test your function :
```python
acyclic = {"A": ["B"], "B": ["C"], "C": []}
print(has_cycle(acyclic))

cyclic = {"A": ["B"], "B": ["C"], "C": ["A"]}
print(has_cycle(cyclic))
```

And its output :
```text
False
True
```
