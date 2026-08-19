# DSA 19: Merge Sort

**Merge sort** is the classic example of **divide and conquer**: split the problem into halves, solve each half recursively, then combine ("merge") the solved halves back together. It guarantees O(n log n) time in *every* case — best, average, and worst — which is a huge deal compared to the O(n²) sorts we've studied so far.

---

## 1. The Core Idea

1. **Divide:** split the array into two halves.
2. **Conquer:** recursively sort each half.
3. **Combine:** merge the two sorted halves into one sorted array.

The base case is an array of size 0 or 1 — already sorted by definition.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])    # append any leftovers
    result.extend(right[j:])
    return result
```

Walk through `[5, 2, 4, 1]`:
```
              [5, 2, 4, 1]
             /            \
        [5, 2]            [4, 1]
        /    \             /   \
      [5]    [2]        [4]    [1]
```
Merging back up: `[5]` + `[2]` → `[2,5]`; `[4]` + `[1]` → `[1,4]`; then `[2,5]` + `[1,4]` → `[1,2,4,5]`.

---

## 2. Why the `merge` Step Is O(n)

Because **both halves are already sorted**, merging them only requires comparing the front of each half and taking the smaller one — a single linear pass through both lists combined, with no backtracking. That's what keeps the combine step cheap.

---

## 3. Complexity Table

| Case | Time | Space |
|---|---|---|
| Best | O(n log n) | O(n) |
| Average | O(n log n) | O(n) |
| Worst | O(n log n) | O(n) |

This is the headline feature: merge sort **never** degrades to O(n²), unlike quicksort's worst case or the simple sorts from earlier lessons. The tradeoff is **space** — merge sort needs O(n) auxiliary space for the temporary arrays created during merging (it's not in-place like bubble/selection/insertion sort).

**Why O(n log n)?** The array is halved `log n` times (the "divide" depth), and at each of those `log n` levels, the total work across all merges is O(n) (every element gets touched once per level). `O(n) work × O(log n) levels = O(n log n)`.

---

## 4. Merge Sort Is Stable

Notice the `<=` in `merge()` (not `<`): when elements are equal, we always take from the `left` array first. This preserves the original relative order of equal elements — merge sort is **stable** by construction, which is exactly why it's a favored building block for real-world stable sorts (Python's Timsort is a hybrid of merge sort and insertion sort).

---

## 5. Merge Sort vs Everything Else So Far

| Algorithm | Best | Average | Worst | Stable? | In-place? |
|---|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | Yes | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | No | Yes |
| Insertion Sort | O(n) | O(n²) | O(n²) | Yes | Yes |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | Yes | No |
| Radix Sort | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | Yes | No |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | Yes | No |

---

## 📚 Resources

- **W3Schools:** [DSA Merge Sort](https://www.w3schools.com/dsa/dsa_algo_mergesort.php)
- **YouTube:** [mycodeschool — Merge Sort](https://www.youtube.com/watch?v=TzeBrDU-JaY)
- **YouTube:** [Abdul Bari — Merge Sort](https://www.youtube.com/watch?v=4VqmGXwpLqc)

---

## 🧠 Try It Yourself

1. Implement `merge_sort` and `merge`, then trace `[5, 2, 4, 1]` by hand as a recursion tree before running the code.
2. Add a print statement showing every call's input and output to visualize the recursive splitting and merging in real time.
3. Compare runtime of `merge_sort` vs `bubble_sort` (Lesson 14) on a reverse-sorted list of 5,000 items — the difference should be dramatic.
4. Modify `merge` to count the number of **inversions** (pairs `i < j` where `arr[i] > arr[j]`) as a side effect of merging — this is a classic technique for counting inversions in O(n log n) instead of O(n²).
