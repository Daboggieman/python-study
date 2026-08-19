# 🧠 DSA Cheatsheet

An exhaustive quick-reference for Data Structures & Algorithms in Python. Pairs with `DSA/curriculum/` (theory) and `DSA/quest/` (practice problems).

---

## Big-O Complexity, At a Glance

From fastest to slowest (n = input size):

| Notation | Name | Example |
|---|---|---|
| O(1) | Constant | Array index, hash table lookup (average) |
| O(log n) | Logarithmic | Binary search, balanced BST operations |
| O(n) | Linear | Linear search, single loop |
| O(n log n) | Linearithmic | Merge sort, heap sort, `sorted()` |
| O(n²) | Quadratic | Bubble/selection/insertion sort, nested loops |
| O(2ⁿ) | Exponential | Naive recursive Fibonacci, subset generation |
| O(n!) | Factorial | Brute-force traveling salesman, permutations |

**Rules of thumb:**
- Drop constants: O(2n) → O(n).
- Drop lower-order terms: O(n² + n) → O(n²).
- Different variables get different letters: O(V + E) for graphs, not O(n).
- Nested loops over the same input generally multiply: loop inside loop → O(n²).
- A loop that halves its range each time is O(log n).

---

## Master Complexity Table — All Data Structures

| Structure | Access | Search | Insert | Delete | Notes |
|---|---|---|---|---|---|
| Array / Python list | O(1) | O(n) | O(n) worst, O(1) amortized at end | O(n) worst, O(1) at end | Contiguous memory |
| Linked List (singly) | O(n) | O(n) | O(1) at head | O(1) at head | No random access |
| Stack | O(n) | O(n) | O(1) push | O(1) pop | LIFO, top only |
| Queue (deque) | O(n) | O(n) | O(1) enqueue | O(1) dequeue | FIFO, both ends |
| Hash Table (dict/set) | — | O(1) avg, O(n) worst | O(1) avg | O(1) avg | Collisions degrade worst case |
| Binary Search Tree | O(log n) avg, O(n) worst | O(log n) avg, O(n) worst | O(log n) avg, O(n) worst | O(log n) avg, O(n) worst | Degenerates if unbalanced |
| AVL Tree | O(log n) | O(log n) | O(log n) | O(log n) | Always balanced |
| Graph (adj. list) | — | O(V+E) | O(1) edge | O(E) edge | BFS/DFS traversal |

---

## Master Complexity Table — All Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable | In-Place |
|---|---|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Yes |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(n+k) | Yes | No |
| Radix Sort | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | O(n+k) | Yes | No |
| Python `sorted()` (Timsort) | O(n) | O(n log n) | O(n log n) | O(n) | Yes | No (returns new list) |

---

## 1. Lists (Dynamic Arrays)

```python
nums = [1, 2, 3]
nums.append(4)          # O(1) amortized
nums.pop()                # O(1)
nums.pop(0)                # O(n)
nums.insert(0, 0)         # O(n)
x in nums                  # O(n)
nums[1]                    # O(1)
len(nums)                  # O(1)
```
**Rule:** front/middle operations are O(n); end operations are O(1).

## 2. Nodes

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None    # or .left/.right for trees, .children for N-ary
```
Nodes live anywhere in memory; they're connected by references, not physical adjacency.

## 3. Linked Lists

```python
def reverse(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev

def find_middle(head):          # slow/fast pointer
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def has_cycle(head):            # Floyd's algorithm
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

## 4. Stacks (LIFO)

```python
stack = []
stack.append(x)   # push
stack.pop()         # pop
stack[-1]           # peek
len(stack) == 0     # is_empty
```
Uses: function call stack, undo/redo, DFS, balanced brackets, expression evaluation.

## 5. Queues (FIFO)

```python
from collections import deque
q = deque()
q.append(x)         # enqueue
q.popleft()          # dequeue
q[0]                  # peek
```
Uses: BFS, task scheduling, buffering. Never use `list.pop(0)` for a queue — it's O(n).

**Priority Queue:**
```python
import heapq
pq = []
heapq.heappush(pq, (priority, item))
heapq.heappop(pq)     # returns lowest-priority-number item first
```

## 6. Hash Tables

```python
d = {}
d[key] = value        # O(1) avg insert/update
d[key]                 # O(1) avg lookup, KeyError if missing
d.get(key, default)    # O(1) avg, no exception
key in d                # O(1) avg
del d[key]              # O(1) avg
s = set()
s.add(x); x in s; s.remove(x)   # all O(1) avg
```
Only hashable (immutable-ish) types can be keys: `str`, `int`, `float`, `tuple`, `frozenset`.

## 7. Trees (General / N-ary)

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def dfs(node):
    print(node.data)
    for c in node.children:
        dfs(c)

def bfs(root):
    from collections import deque
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.data)
        q.extend(node.children)
```

## 8. Binary Trees

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(n, r=None):     # Left, Node, Right (sorted order for a BST)
    if r is None: r = []
    if n:
        inorder(n.left, r); r.append(n.data); inorder(n.right, r)
    return r

def preorder(n, r=None):    # Node, Left, Right
    if r is None: r = []
    if n:
        r.append(n.data); preorder(n.left, r); preorder(n.right, r)
    return r

def postorder(n, r=None):   # Left, Right, Node
    if r is None: r = []
    if n:
        postorder(n.left, r); postorder(n.right, r); r.append(n.data)
    return r

def height(n):
    return -1 if n is None else 1 + max(height(n.left), height(n.right))
```

## 9. Binary Search Trees (BST)

```python
def insert(root, v):
    if root is None: return TreeNode(v)
    if v < root.data: root.left = insert(root.left, v)
    elif v > root.data: root.right = insert(root.right, v)
    return root

def search(root, target):
    if root is None: return False
    if root.data == target: return True
    return search(root.left, target) if target < root.data else search(root.right, target)
```
**Rule:** left subtree < node < right subtree, recursively, everywhere. In-order traversal = sorted output.

## 10. AVL Trees

```python
def get_height(n): return n.height if n else 0
def get_balance(n): return 0 if n is None else get_height(n.left) - get_height(n.right)

# balance_factor outside [-1, 0, 1] -> rotate
# LL -> rotate_right | RR -> rotate_left
# LR -> rotate_left(child) then rotate_right | RL -> rotate_right(child) then rotate_left
```
Self-balancing BST: guarantees O(log n) height always, at the cost of bookkeeping on every insert/delete.

## 11. Graphs

```python
graph = {"A": ["B", "C"], "B": ["A"], "C": ["A"]}   # adjacency list

def dfs(g, start, visited=None):
    if visited is None: visited = set()
    visited.add(start)
    for nb in g[start]:
        if nb not in visited: dfs(g, nb, visited)
    return visited

def bfs(g, start):
    from collections import deque
    visited, q, order = {start}, deque([start]), []
    while q:
        node = q.popleft(); order.append(node)
        for nb in g[node]:
            if nb not in visited:
                visited.add(nb); q.append(nb)
    return order
```
**BFS finds shortest path in unweighted graphs. Dijkstra (heap-based) finds shortest path in weighted graphs.**

## 12. Linear Search

```python
def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target: return i
    return -1
```
O(n), works on unsorted data and any iterable. Best when searching only once.

## 13. Binary Search

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: lo = mid + 1
        else: hi = mid - 1
    return -1
```
O(log n), **requires sorted input**. `bisect.bisect_left(arr, x)` gives you this for free.

## 14. Bubble Sort

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped: break
    return arr
```

## 15. Selection Sort

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]: min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```
Fewest swaps of any comparison sort (at most n-1), but always O(n²) comparisons.

## 16. Insertion Sort

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
```
Adaptive: O(n) on already-sorted data. Used inside Python's Timsort for small sub-arrays.

## 17. Counting Sort

```python
def counting_sort(arr):
    if not arr: return arr
    lo, hi = min(arr), max(arr)
    count = [0] * (hi - lo + 1)
    for x in arr: count[x - lo] += 1
    for i in range(1, len(count)): count[i] += count[i-1]
    out = [0] * len(arr)
    for x in reversed(arr):
        count[x - lo] -= 1
        out[count[x - lo]] = x
    return out
```
Not comparison-based. O(n+k). Only good when the value range k is small relative to n.

## 18. Radix Sort

```python
def radix_sort(arr):
    if not arr: return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = counting_sort_by_digit(arr, exp)   # stable counting sort on one digit
        exp *= 10
    return arr
```
Sorts digit-by-digit using a stable counting sort at each digit position. O(d·(n+k)).

## 19. Merge Sort

```python
def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result
```
O(n log n) guaranteed in every case. Stable. Not in-place (needs O(n) extra space).

---

## Common Patterns Cheat Sheet

| Pattern | Used For | Key Idea |
|---|---|---|
| Two pointers | Palindromes, sorted-array pair sums | Move pointers from both ends inward |
| Sliding window | Subarray/substring problems | Grow/shrink a window, track a running stat |
| Fast & slow pointers | Cycle detection, middle of list | Fast moves 2x speed of slow |
| Divide and conquer | Merge sort, binary search | Break problem into smaller identical subproblems |
| Hashing for O(1) lookup | Two Sum, duplicates, grouping | Trade space for time |
| BFS | Shortest path (unweighted), level order | Queue-based, level by level |
| DFS | Path existence, cycle detection, backtracking | Stack-based (or recursion) |
| Greedy | Interval scheduling, coin change (some variants) | Make the locally-best choice at each step |
| Dynamic Programming | Overlapping subproblems (Fibonacci, knapsack) | Cache/memoize repeated subproblem results |

---

## 📚 More Resources

See `DSA/resources/links.md` for the full curated list of W3Schools pages, YouTube playlists, and articles referenced throughout every `DSA/curriculum/` lesson.
