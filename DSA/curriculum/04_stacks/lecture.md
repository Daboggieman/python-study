# DSA 04: Stacks

A **stack** is a linear data structure that follows **LIFO**: Last In, First Out. Think of a stack of plates — you can only add or remove from the top.

---

## 1. The Core Operations

| Operation | Description | Complexity |
|---|---|---|
| `push(x)` | add `x` to the top | O(1) |
| `pop()` | remove and return the top item | O(1) |
| `peek()` / `top()` | look at the top item without removing it | O(1) |
| `is_empty()` | check if the stack has no items | O(1) |

All of these are O(1) — that's the entire point of a stack. It intentionally gives up flexibility (no random access!) in exchange for guaranteed-fast operations at one end.

---

## 2. Implementing a Stack with a Python List

Python lists already support O(1) append/pop *from the end*, so they make a perfectly good stack — just never use `insert(0, ...)` or `pop(0)`.

```python
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)          # add to the "top" (end of list)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._items.pop()          # remove from the "top"

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)
```

## 3. Implementing a Stack with a Linked List

You can also build a stack from nodes — push/pop just add/remove at the `head`:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            raise IndexError("pop from an empty stack")
        data = self.top.data
        self.top = self.top.next
        return data
```

---

## 4. Where Stacks Show Up

- **Function call stack** — every language runtime uses a stack to track function calls and local variables. This is literally why deep recursion causes a "stack overflow."
- **Undo/redo** in editors.
- **Balanced brackets / parentheses matching.**
- **Depth-First Search (DFS)** on trees and graphs.
- **Expression evaluation** (converting infix to postfix, evaluating postfix).
- Browser **back button** history.

---

## 5. Classic Problem: Balanced Brackets

```python
def is_balanced(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0

print(is_balanced("{[()()]}"))  # True
print(is_balanced("{[(])}"))    # False
```

---

## 📚 Resources

- **W3Schools:** [DSA Stacks](https://www.w3schools.com/dsa/dsa_data_stacks.php)
- **YouTube:** [mycodeschool — Stack Data Structure Introduction](https://www.youtube.com/watch?v=F1F2imiOJfk)
- **YouTube:** [Abdul Bari — Stack](https://www.youtube.com/watch?v=I37kGX-nZEE) — excellent for the theory side
- **GeeksforGeeks:** [Stack Data Structure](https://www.geeksforgeeks.org/stack-data-structure/)

---

## 🧠 Try It Yourself

1. Implement `Stack` (list-based) fully, then implement `LinkedStack` and confirm they behave identically for the same sequence of pushes/pops.
2. Implement `is_balanced` and test it against `"([)]"`, `"{[]}"`, and `"((("`.
3. Use a stack to reverse a string without using slicing (`s[::-1]`) or `reversed()`.
4. Use a stack to check if a string is a palindrome (compare against your two-pointer solution from Lesson 01 — which approach uses more memory?).
