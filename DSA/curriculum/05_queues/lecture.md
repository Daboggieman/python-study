# DSA 05: Queues

A **queue** is a linear data structure that follows **FIFO**: First In, First Out. Think of a checkout line — whoever joined first gets served first.

---

## 1. The Core Operations

| Operation | Description | Complexity (good implementation) |
|---|---|---|
| `enqueue(x)` | add `x` to the back | O(1) |
| `dequeue()` | remove and return the front item | O(1) |
| `peek()` / `front()` | look at the front item | O(1) |
| `is_empty()` | check if empty | O(1) |

---

## 2. Why NOT a Plain Python List

It's tempting to do:

```python
queue = []
queue.append(4)     # enqueue: O(1), fine
queue.pop(0)         # dequeue: O(n) !! everything shifts left
```

`pop(0)` is O(n) because every remaining element has to shift over one slot. For a queue that's used heavily, this becomes a real performance problem. The fix: `collections.deque`.

---

## 3. `collections.deque` — the Right Tool

`deque` (double-ended queue) is implemented as a doubly linked list of blocks internally, giving O(1) operations at **both** ends.

```python
from collections import deque

queue = deque()
queue.append(1)        # enqueue at back: O(1)
queue.append(2)
queue.append(3)
print(queue.popleft())  # dequeue from front: O(1) -> 1
print(queue)             # deque([2, 3])
```

---

## 4. Implementing a Queue with a Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)
        if self.rear is None:
            self.front = self.rear = node
            return
        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.front is None:
            raise IndexError("dequeue from an empty queue")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data
```

Keeping a `rear` pointer is what makes `enqueue` O(1) instead of O(n).

---

## 5. Variations

- **Circular queue** — uses a fixed-size array and wraps the index around with modulo, avoiding wasted space. Common in producer/consumer buffers.
- **Priority queue** — instead of FIFO, items come out in priority order. Usually implemented with a **heap** (`heapq` in Python).
- **Deque (double-ended queue)** — insertion/removal from both ends, generalizes both stacks and queues.

```python
import heapq

pq = []
heapq.heappush(pq, (2, "do laundry"))
heapq.heappush(pq, (1, "fix critical bug"))
heapq.heappush(pq, (3, "water the plants"))
print(heapq.heappop(pq))  # (1, 'fix critical bug') -- lowest number = highest priority
```

---

## 6. Where Queues Show Up

- **Breadth-First Search (BFS)** on trees and graphs.
- **Task scheduling** (print queues, CPU task queues, message queues like RabbitMQ/Kafka conceptually).
- **Buffering** — streaming data, keyboard/network input buffers.

---

## 📚 Resources

- **W3Schools:** [DSA Queues](https://www.w3schools.com/dsa/dsa_data_queues.php) · [collections.deque docs](https://docs.python.org/3/library/collections.html#collections.deque)
- **YouTube:** [mycodeschool — Queue Data Structure Introduction](https://www.youtube.com/watch?v=XuCbpw6Bj1U)
- **YouTube:** [Abdul Bari — Queue](https://www.youtube.com/watch?v=D6gu-_tmEpQ)

---

## 🧠 Try It Yourself

1. Implement `Queue` using `collections.deque` internally, then implement it again using your own linked-list nodes (no `deque`, no list).
2. Use a queue to simulate a print queue: enqueue 5 "documents", then dequeue and print them one at a time in order.
3. Implement a fixed-size **circular queue** backed by a Python list of size `n`, tracking `front`/`rear` indices and wrapping with `% n`.
4. Use `heapq` to build a simple priority-based to-do list that always pops the most urgent task first.
