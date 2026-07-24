# DSA 17: Counting Sort

Every sorting algorithm so far has been a **comparison sort** — it decides order by comparing elements (`>`, `<`). There's a proven theoretical limit: no comparison sort can beat O(n log n) in the general case. **Counting sort** breaks past this limit by *not comparing at all* — instead, it counts occurrences of each value directly. This only works under a specific condition: the values must be integers (or map to integers) within a known, reasonably small range.

---

## 1. The Core Idea

1. Count how many times each value appears.
2. Use those counts to figure out the final position of each value.
3. Build the output array directly from the counts.

```python
def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1

    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1

    # transform counts into "how many elements are <= this value" (prefix sum)
    for i in range(1, range_size):
        count[i] += count[i - 1]

    output = [0] * len(arr)
    # iterate in reverse to keep it stable
    for num in reversed(arr):
        count[num - min_val] -= 1
        output[count[num - min_val]] = num

    return output
```

Walk through `[4, 2, 2, 8, 3, 3, 1]`:
- Counts of 1,2,3,4,8 → `[1, 2, 2, 1, 0, 0, 0, 1]` (index 0 = value 1)
- Prefix sums tell you exactly how many elements come before or at each value
- Output built directly: `[1, 2, 2, 3, 3, 4, 8]`

---

## 2. Complexity Table

| Metric | Value |
|---|---|
| Time | O(n + k), where k = range of input values |
| Space | O(n + k) |

**This beats O(n log n)!** But only when `k` (the range of values) is not much bigger than `n`. If you tried to counting-sort a list of 10 numbers where values range from 1 to 10,000,000, you'd allocate a 10-million-element count array for only 10 items — a terrible tradeoff. Counting sort is a specialist tool, not a general one.

---

## 3. When to Use It

- Sorting exam scores (0–100).
- Sorting ages (0–120).
- Sorting single-digit or small fixed-range categories.
- As a **subroutine** inside radix sort (next lesson!) — this is its most important real-world use.

Counting sort is **stable** when implemented as shown above (iterating in reverse during the output-building step preserves the original relative order of equal elements) — and that stability is *exactly* what makes it usable as a building block for radix sort.

---

## 📚 Resources

- **W3Schools:** [DSA Counting Sort](https://www.w3schools.com/dsa/dsa_algo_countingsort.php)
- **YouTube:** [mycodeschool — Counting Sort](https://www.youtube.com/watch?v=7zuGmKfUt7s)
- **YouTube:** [Abdul Bari — Counting Sort](https://www.youtube.com/watch?v=OKd534EWcdk)

---

## 🧠 Try It Yourself

1. Implement `counting_sort` and trace `[4, 2, 2, 8, 3, 3, 1]` by hand, writing out the count array and prefix-sum array before running the code.
2. Modify it to sort a list of tuples `(score, name)` by `score` only, and verify it's stable (equal scores keep their original name order).
3. Explain in a comment why counting sort would be a bad choice for sorting 100 random floating-point numbers between 0 and 1,000,000.
4. Compare runtime of `counting_sort` vs `sorted()` on a list of 100,000 integers between 0 and 100 — counting sort should win here.
