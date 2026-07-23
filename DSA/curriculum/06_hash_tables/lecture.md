# DSA 06: Hash Tables

A **hash table** (Python's `dict` and `set`) stores key-value pairs and gives you **average O(1)** insert, lookup, and delete — no matter how large it gets. This is one of the most important data structures in all of computing.

---

## 1. The Core Idea

A hash table uses a **hash function** to convert a key into an integer, then uses that integer (modulo the table size) as an index into an underlying array (called "buckets").

```
key "apple" --> hash("apple") --> 7264891... --> % table_size --> index 4
```

Because computing a hash and jumping to an array index are both O(1), lookup is O(1) on average — you never have to scan through every key.

```python
h = hash("apple")
print(h)             # some large integer (varies by Python session, due to hash randomization)
print(hash("apple") == hash("apple"))  # True — same input, same hash, always
```

---

## 2. Building a (Simplified) Hash Table From Scratch

```python
class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]  # each bucket is a list of (key, value) pairs

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)   # update existing key
                return
        bucket.append((key, value))        # insert new key

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(key)
```

---

## 3. Collisions

Two different keys can hash to the *same* bucket index — this is called a **collision**. The example above handles collisions with **chaining**: each bucket is a small list, so colliding keys just live together in the same bucket. This is why lookup is "average" O(1) rather than "always" O(1) — a worst-case scenario where everything collides into one bucket degrades to O(n).

Other collision strategies:
- **Open addressing** — on collision, probe to the next available slot (linear probing, quadratic probing, double hashing).
- **Chaining** — what we implemented above; typically simpler and what CPython effectively approximates conceptually (CPython's real implementation is open addressing under the hood, but chaining is easier to learn from first).

Good hash tables also **resize** (like dynamic arrays) once they get too full, to keep collisions rare.

---

## 4. Complexity Table

| Operation | Average Case | Worst Case |
|---|---|---|
| Insert | O(1) | O(n) — all keys collide |
| Lookup | O(1) | O(n) |
| Delete | O(1) | O(n) |

In practice, with a good hash function and resizing, worst case is extremely rare — this is why `dict` is the workhorse of Python.

---

## 5. Python's Built-in Hash Table: `dict` and `set`

```python
prices = {"apple": 1.50, "banana": 0.50}
prices["cherry"] = 3.00      # O(1) average insert
print(prices["apple"])        # O(1) average lookup
del prices["banana"]          # O(1) average delete
print("apple" in prices)      # O(1) average membership check

unique_ids = set([1, 2, 2, 3, 3, 3])
print(unique_ids)             # {1, 2, 3} -- O(1) average membership + dedup
```

**Important:** only **hashable** (usually immutable) types can be dict keys or set members — `str`, `int`, `tuple`, `frozenset`. Lists and dicts are unhashable because their contents (and therefore their hash) can change.

---

## 📚 Resources

- **W3Schools:** [Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp) · [DSA Hash Tables](https://www.w3schools.com/dsa/dsa_data_hashtables.php)
- **YouTube:** [mycodeschool — Hashing / Hash Tables](https://www.youtube.com/watch?v=shs0KM3wKv8)
- **YouTube:** [Abdul Bari — Hashing](https://www.youtube.com/watch?v=mFY0J0hf4Zs)
- **Real Python:** [Python Hash Tables: Understanding dictionaries](https://realpython.com/python-hash-table/)

---

## 🧠 Try It Yourself

1. Implement `HashTable` from scratch above, then test `put`, `get`, and `remove` with several keys that intentionally collide (hint: use a tiny `capacity` like 2 to force collisions).
2. Write a function `first_repeated_char(s)` that returns the first character that appears more than once in a string, using a hash table (`dict` or `set`) to do it in O(n) instead of the naive O(n²) nested-loop approach.
3. Write `two_sum(nums, target)` that returns the indices of two numbers that add up to `target`, in O(n) time using a dict (the classic interview question).
4. Explain in a comment why `{[1,2]: "a"}` raises a `TypeError` in Python.
