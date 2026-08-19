# DSA 12: Linear Search

**Linear search** is the simplest search algorithm: check every element, one at a time, until you find what you're looking for (or run out of elements). It's the baseline every other search algorithm is compared against.

---

## 1. The Algorithm

```python
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i          # found it, return the index
    return -1                  # not found
```

That's it. No sorting required, works on any iterable, any data type.

---

## 2. Complexity

| Case | Time Complexity | When it happens |
|---|---|---|
| Best case | O(1) | Target is the first element |
| Average case | O(n) | Target is somewhere in the middle, on average |
| Worst case | O(n) | Target is last, or not present at all |

Space complexity: O(1) — no extra memory needed.

---

## 3. When Linear Search Is the *Right* Choice

It's tempting to think "linear search is slow, always use binary search" — but that's not quite right:

- Linear search works on **unsorted** data. Binary search *requires* sorted data.
- If you're only searching **once**, sorting first (O(n log n)) just to binary search (O(log n)) is slower overall than a single linear scan (O(n)).
- Linear search works on any iterable (even ones without random access, like a linked list or a file stream).

**Rule of thumb:** if you search *many times* on the *same* dataset, sort once and binary search repeatedly. If you search *once*, linear search is often simplest and fastest overall.

---

## 4. A Common Variant: Find All Matches

```python
def find_all(arr, target):
    return [i for i, value in enumerate(arr) if value == target]
```

---

## 📚 Resources

- **W3Schools:** [DSA Linear Search](https://www.w3schools.com/dsa/dsa_algo_linearsearch.php)
- **YouTube:** [mycodeschool — Linear Search](https://www.youtube.com/watch?v=246V51AWwZM)
- **YouTube:** [freeCodeCamp — Search Algorithms](https://www.youtube.com/watch?v=p65AHm9MX80)

---

## 🧠 Try It Yourself

1. Implement `linear_search` and `find_all` above.
2. Modify `linear_search` to work on a linked list (from Lesson 03) instead of a Python list — notice it still works, because linear search never needed random access in the first place.
3. Time linear search on a list of 1,000,000 items, searching for a value at the very end, then for a value that doesn't exist. Compare the two times — are they roughly the same? Why?
