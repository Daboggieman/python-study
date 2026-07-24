# DSA 14: Bubble Sort

**Bubble sort** repeatedly steps through the list, compares adjacent elements, and swaps them if they're in the wrong order. Larger elements "bubble up" to the end with each pass. It's the classic first sorting algorithm taught precisely because it's easy to visualize — but it's rarely used in production due to its poor performance.

---

## 1. The Algorithm

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

Walk through `[5, 2, 4, 1]`:
- Pass 1: `[2, 5, 4, 1]` → `[2, 4, 5, 1]` → `[2, 4, 1, 5]` (5 has bubbled to the end)
- Pass 2: `[2, 4, 1, 5]` → `[2, 1, 4, 5]` (4 is now in place)
- Pass 3: `[1, 2, 4, 5]` (fully sorted)

---

## 2. The Optimization: Early Exit

If a full pass makes **zero** swaps, the list is already sorted — no need to keep going.

```python
def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
```

This turns the **best case** (already-sorted input) into O(n) instead of always O(n²).

---

## 3. Complexity Table

| Case | Time | Space |
|---|---|---|
| Best (already sorted, with early-exit) | O(n) | O(1) |
| Average | O(n²) | O(1) |
| Worst (reverse sorted) | O(n²) | O(1) |

Bubble sort is **stable** (equal elements keep their original relative order) and **in-place** (no extra array needed).

---

## 4. Why Learn It If It's "Bad"?

Bubble sort is O(n²), which makes it impractical for large datasets compared to O(n log n) algorithms like merge sort. But it's foundational because:
- It teaches the core idea of "compare and swap" that shows up in many algorithms.
- It's genuinely fine for tiny lists (< ~20 elements) or nearly-sorted data, where the constant-factor simplicity can even beat fancier algorithms.
- It's a great first step toward understanding *why* we need better algorithms — you'll appreciate merge sort a lot more after living with bubble sort's O(n²) pain.

---

## 📚 Resources

- **W3Schools:** [DSA Bubble Sort](https://www.w3schools.com/dsa/dsa_algo_bubblesort.php)
- **YouTube:** [mycodeschool — Bubble Sort](https://www.youtube.com/watch?v=6Gv8vg0kcHc)
- **YouTube:** [Abdul Bari — Bubble Sort](https://www.youtube.com/watch?v=xli_FI7CuzA)

---

## 🧠 Try It Yourself

1. Implement `bubble_sort` and trace it by hand on `[5, 2, 4, 1]` before running the code, comparing each pass to what the code produces.
2. Implement the early-exit optimization and print how many passes it takes for an already-sorted list of 10 items (should be just 1).
3. Modify bubble sort to sort in **descending** order instead of ascending, changing only the comparison.
4. Count and print the total number of swaps performed for a reverse-sorted list of size 10 — this is bubble sort's worst case.
