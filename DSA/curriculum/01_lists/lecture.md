# DSA 01: Lists (Dynamic Arrays)

Before we build our own data structures, we need to understand the one Python gives us for free: the **list**. In most other languages this concept is called a **dynamic array**, and almost every custom data structure we build later (stacks, queues, hash tables) will be built on top of it.

This lesson looks at Python's `list` through a *data structures* lens: not "how do I use it" (you already know that), but "what is actually happening underneath, and how fast is it?"

---

## 1. What Is an Array, Really?

A plain **array** (the kind you'd find in C or Java) is a fixed-size, contiguous block of memory. Because every element is the same size and sits right next to the next one, the computer can jump straight to index `i` using simple arithmetic: `address = base_address + (i * element_size)`. This is why indexing an array is **O(1)** — constant time, regardless of how big the array is.

A **dynamic array** (Python's `list`, Java's `ArrayList`, C++'s `std::vector`) is an array that can grow. Under the hood, Python's list keeps a contiguous block of memory that's usually a bit *bigger* than it needs, so it has "spare room" to grow into without immediately needing to resize.

```python
nums = [10, 20, 30]
print(nums[0])   # O(1) — jumps straight to the memory slot
```

---

## 2. Why Appending Is (Usually) O(1)

When you call `nums.append(x)`, if there's spare capacity, Python just writes into the next free slot — O(1).

When the list is completely full, Python has to:
1. Allocate a new, larger block of memory (CPython typically grows by roughly 1.125x plus a bit).
2. Copy every existing element into the new block — O(n).
3. Free the old block.

This resize is expensive, but it happens rarely, and when you average the cost over many appends, the *amortized* cost per append is still **O(1)**. This is a classic and important DSA concept: **amortized time complexity**.

```python
nums = []
for i in range(5):
    nums.append(i)   # amortized O(1) each, even though a resize happens occasionally
```

---

## 3. Complexity Cheat Table

| Operation | Example | Time Complexity |
|---|---|---|
| Index access | `nums[i]` | O(1) |
| Index assignment | `nums[i] = x` | O(1) |
| Append | `nums.append(x)` | O(1) amortized |
| Pop from end | `nums.pop()` | O(1) |
| Pop from front | `nums.pop(0)` | O(n) — everything shifts left |
| Insert at front/middle | `nums.insert(0, x)` | O(n) — everything shifts right |
| Search by value | `x in nums` | O(n) |
| Delete by value | `nums.remove(x)` | O(n) |
| Slice | `nums[a:b]` | O(k), k = slice length |
| Length | `len(nums)` | O(1) — Python caches this |

**Key takeaway:** anything that touches the *front* or *middle* of a Python list costs O(n) because every following element has to physically shift over in memory. This is the single biggest reason linked lists exist (next lesson!).

---

## 4. List vs. Array vs. Linked List (preview)

| | Python `list` | Linked List |
|---|---|---|
| Memory layout | Contiguous | Scattered, connected by pointers |
| Random access `[i]` | O(1) | O(n) |
| Insert/delete at front | O(n) | O(1) |
| Insert/delete at end | O(1) amortized | O(1) if you track the tail |
| Cache friendliness | Great | Poor |

Neither is "better" — they trade off differently, and picking the right one for the job is the whole point of studying DSA.

---

## 5. Common List-Based Patterns Used in Algorithms

```python
# Two-pointer technique
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Sliding window
def max_sum_subarray(nums, k):
    window_sum = sum(nums[:k])
    best = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        best = max(best, window_sum)
    return best
```

---

## 📚 Resources

- **W3Schools:** [Python Lists](https://www.w3schools.com/python/python_lists.asp) · [List Methods](https://www.w3schools.com/python/python_lists_methods.asp)
- **YouTube:** [CS Dojo — Data Structures: Arrays](https://www.youtube.com/watch?v=gRAaXBGjR8g) — clear, time-tested explanation of arrays and complexity
- **YouTube:** [mCoding — Dynamic Arrays explained](https://www.youtube.com/watch?v=WTOMcgUsW8k)
- **Docs:** [Python Time Complexity Wiki](https://wiki.python.org/moin/TimeComplexity) — the canonical reference for built-in complexity

---

## 🧠 Try It Yourself

1. Write a function `time_it(func, *args)` that times how long an operation takes, then compare `insert(0, x)` vs `append(x)` on a list of 100,000 items. Confirm which one is slower and explain why.
2. Implement `is_palindrome` and `max_sum_subarray` above from scratch without looking, then trace through them by hand on paper for a small input.
3. Explain in your own words (write it as a comment) why `list.pop(0)` is O(n) but `list.pop()` is O(1).
