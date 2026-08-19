# DSA 03: Linked Lists

A **linked list** is a chain of nodes where each node points to the next. Unlike a Python list, there's no contiguous memory and no index-based jump — you always start at the `head` and walk forward.

---

## 1. Singly Linked List

Each node has `data` and `next` only. The list itself just needs to remember the `head` (and optionally a `tail` for fast appends).

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        print(" -> ".join(values) if values else "EMPTY")
```

---

## 2. Complexity Table

| Operation | Singly Linked List | Python List |
|---|---|---|
| Access by index | O(n) | O(1) |
| Insert at front | O(1) | O(n) |
| Insert at back (no tail pointer) | O(n) | O(1) amortized |
| Insert at back (with tail pointer) | O(1) | O(1) amortized |
| Delete at front | O(1) | O(n) |
| Search by value | O(n) | O(n) |

**Rule of thumb:** if your program does lots of insert/delete at the *front*, use a linked list. If it does lots of random-access reads, use a list.

---

## 3. Doubly Linked List (each node also has `prev`)

```python
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```

Doubly linked lists allow O(1) deletion of a node *you already have a reference to* (no need to find its predecessor), and can be walked in both directions. This is what Python's own `collections.deque` uses internally.

---

## 4. Circular Linked List

The last node's `next` points back to the `head` instead of `None`. Useful for round-robin scheduling, buffering, and things like the Josephus problem.

```python
# tail.next = head   # this one line turns a list circular
```

---

## 5. Reversing a Linked List (a DSA classic)

```python
def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next   # save it before we overwrite
        current.next = prev        # reverse the pointer
        prev = current
        current = next_node
    return prev   # new head
```

---

## 📚 Resources

- **W3Schools:** [Python Classes](https://www.w3schools.com/python/python_classes.asp) · [DSA Linked Lists](https://www.w3schools.com/dsa/dsa_data_linkedlists.php)
- **YouTube:** [mycodeschool — Linked List Insertion](https://www.youtube.com/watch?v=6IZ8p9y1DOc)
- **YouTube:** [William Fiset — Linked Lists](https://www.youtube.com/watch?v=vNAdEo2CB7Y) — algorithm-focused, very thorough
- **Real Python:** [Linked Lists in Python](https://realpython.com/linked-lists-python/)

---

## 🧠 Try It Yourself

1. Implement `push_front`, `push_back`, and `display` from scratch, then add a `pop_front()` method.
2. Implement `reverse(head)` and verify it on a 5-element list by printing before and after.
3. Implement a `find_middle(head)` function using the classic **slow/fast pointer** technique (fast moves 2 steps for every 1 step of slow) — this finds the middle node in a single pass.
4. Convert your singly linked list into a doubly linked list by adding `prev` pointers, then write a `display_backwards()` method.
