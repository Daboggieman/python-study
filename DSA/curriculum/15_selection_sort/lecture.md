# DSA 15: Selection Sort

**Selection sort** divides the array into a sorted part (at the front) and an unsorted part (the rest). On each pass, it *selects* the smallest element remaining in the unsorted part and swaps it into place.

---

## 1. The Algorithm

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
```

Walk through `[64, 25, 12, 22, 11]`:
- i=0: smallest in `[64,25,12,22,11]` is 11 (index 4) → swap → `[11,25,12,22,64]`
- i=1: smallest in `[25,12,22,64]` is 12 (index 2) → swap → `[11,12,25,22,64]`
- i=2: smallest in `[25,22,64]` is 22 → swap → `[11,12,22,25,64]`
- i=3: smallest in `[25,64]` is 25 → already in place
- Done: `[11,12,22,25,64]`

---

## 2. Complexity Table

| Case | Time | Space |
|---|---|---|
| Best | O(n²) | O(1) |
| Average | O(n²) | O(1) |
| Worst | O(n²) | O(1) |

Unlike bubble sort or insertion sort, selection sort's time complexity **never improves** for nearly-sorted input — it always does the exact same number of comparisons, because it always scans the whole remaining unsorted part looking for the minimum, regardless of how sorted things already are.

Selection sort is **not stable** by default (a swap can jump an equal element past another equal element) and it **is in-place**.

---

## 3. The One Advantage: Minimal Swaps

Selection sort does at most `n - 1` swaps total — the fewest of any comparison sort. This matters when the "write" operation is expensive (e.g., writing to flash memory), even though the number of *comparisons* is still O(n²).

Compare: bubble sort might do many more swaps than selection sort for the same input, even though both are O(n²) in comparisons.

---

## 📚 Resources

- **W3Schools:** [DSA Selection Sort](https://www.w3schools.com/dsa/dsa_algo_selectionsort.php)
- **YouTube:** [mycodeschool — Selection Sort](https://www.youtube.com/watch?v=92BfuxHn2XE)
- **YouTube:** [Abdul Bari — Selection Sort](https://www.youtube.com/watch?v=g-PGLbMth_g)

---

## 🧠 Try It Yourself

1. Implement `selection_sort` and trace it on `[64, 25, 12, 22, 11]` by hand first.
2. Modify it to count and print the number of swaps performed vs. the number of comparisons, for a list of 10 random integers. Confirm swaps ≤ n-1.
3. Implement a version that finds the **maximum** each pass and builds the sorted array from the back instead of the front.
4. Demonstrate selection sort's instability: sort a list of tuples `[(1,"a"), (1,"b"), (0,"c")]` by the first element only, and check whether `"a"` still comes before `"b"` in the output.
