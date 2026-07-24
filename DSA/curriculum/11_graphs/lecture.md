# DSA 11: Graphs

A **graph** is the most general data structure we've covered: a set of **vertices** (nodes) connected by **edges**. Trees are actually just a special kind of graph (one with no cycles and a single root). Graphs model things like social networks, road maps, the internet, dependency chains, and more.

---

## 1. Key Vocabulary

| Term | Meaning |
|---|---|
| **Vertex / Node** | A single point in the graph |
| **Edge** | A connection between two vertices |
| **Directed** graph | Edges have a direction (A → B doesn't imply B → A) |
| **Undirected** graph | Edges go both ways (A — B implies B — A) |
| **Weighted** graph | Edges carry a cost/distance/value |
| **Cycle** | A path that starts and ends at the same vertex |
| **Degree** | Number of edges touching a vertex |

---

## 2. Representations

### Adjacency List (most common — efficient for sparse graphs)
```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"],
}
```

### Adjacency Matrix (efficient for dense graphs, O(1) edge lookup, O(V²) space)
```python
#      A  B  C  D
# A  [ 0, 1, 1, 0 ]
# B  [ 1, 0, 0, 1 ]
# C  [ 1, 0, 0, 1 ]
# D  [ 0, 1, 1, 0 ]
```

For weighted graphs, an adjacency list stores `(neighbor, weight)` pairs instead of just the neighbor:

```python
weighted_graph = {
    "A": [("B", 4), ("C", 1)],
    "B": [("A", 4), ("D", 1)],
    "C": [("A", 1), ("D", 5)],
    "D": [("B", 1), ("C", 5)],
}
```

---

## 3. Depth-First Search (DFS)

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited
```

---

## 4. Breadth-First Search (BFS)

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
```

**DFS vs BFS:** DFS goes deep first (good for exploring all paths, cycle detection, topological sort). BFS goes wide first (guarantees the **shortest path** in an unweighted graph — this is a critical, testable fact).

---

## 5. Shortest Path in a Weighted Graph: Dijkstra's Algorithm

```python
import heapq

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
```

---

## 6. Complexity Table (V = vertices, E = edges)

| Algorithm | Time Complexity |
|---|---|
| DFS / BFS (adjacency list) | O(V + E) |
| DFS / BFS (adjacency matrix) | O(V²) |
| Dijkstra (with heap) | O((V + E) log V) |

---

## 📚 Resources

- **W3Schools:** [DSA Graphs](https://www.w3schools.com/dsa/dsa_theory_graphs.php)
- **YouTube:** [mycodeschool — Graph Data Structure Introduction](https://www.youtube.com/watch?v=gXgEDyodOJU)
- **YouTube:** [William Fiset — Graph Theory Playlist](https://www.youtube.com/watch?v=09_LlHjoEiY)
- **YouTube:** [Abdul Bari — Dijkstra's Algorithm](https://www.youtube.com/watch?v=XB4MIexjvY0)

---

## 🧠 Try It Yourself

1. Represent the sample undirected graph above as an adjacency list and run both `dfs()` and `bfs()` from `"A"`. Note how the visiting order differs.
2. Write `has_path(graph, start, end)` that returns True/False whether a path exists between two nodes (reuse BFS or DFS).
3. Write `shortest_path_length(graph, start, end)` for an **unweighted** graph using BFS (count the number of edges, not weights).
4. Implement `dijkstra()` on the weighted graph example and confirm the shortest distance from `"A"` to `"D"`.
