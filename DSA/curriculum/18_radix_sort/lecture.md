# DSA 18: Radix Sort

**Radix sort** sorts integers **digit by digit**, from the least significant digit (LSD) to the most significant, using a **stable** sort (Counting Sort, from the last lesson!) at each digit position. It's another non-comparison sort, and it can sort in linear time under the right conditions.

---

## 1. The Core Idea

Instead of comparing whole numbers, sort repeatedly by one digit at a time:

```
Input: [170, 45, 75, 90, 802, 24, 2, 66]

Sort by 1's digit:  [170, 90, 802, 2, 24, 45, 75, 66]
Sort by 10's digit: [802, 2, 24, 45, 66, 170, 75, 90]
Sort by 100's digit:[2, 24, 45, 66, 75, 90, 170, 802]  <- fully sorted!
```

The magic ingredient: each digit-pass **must** use a **stable** sort, or the ordering established by previous (less significant) digit passes gets destroyed.

---

## 2. Implementation (using Counting Sort as the stable subroutine)

```python
def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10   # digits are always 0-9

    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):     # iterate in reverse for stability
        digit = (arr[i] // exp) % 10
        count[digit] -= 1
        output[count[digit]] = arr[i]

    return output

def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr
```

`exp` represents which digit place we're currently sorting by: `1` = ones, `10` = tens, `100` = hundreds, etc. `(num // exp) % 10` extracts that digit.

---

## 3. Complexity

| Metric | Value |
|---|---|
| Time | O(d × (n + k)), where d = number of digits, k = base (10 for decimal) |
| Space | O(n + k) |

Since `d` (number of digits) is typically small and fixed (e.g., a 32-bit integer has at most 10 decimal digits), this is effectively **O(n)** for practical purposes — genuinely faster than any comparison sort's O(n log n) floor, for the right kind of data.

---

## 4. Limitations

- Works cleanly on non-negative integers. Negative numbers and floats require extra handling (e.g., separating negatives, sorting them by magnitude, then reversing and re-merging).
- Not a general-purpose sort — like counting sort, it's a specialist for fixed-width data (integers, fixed-length strings).
- Radix sort on strings works the same way, but sorts by *character position* instead of numeric digit (this is how large-scale string sorting, e.g. sorting all words by length-bucketed passes, is sometimes done).

---

## 📚 Resources

- **W3Schools:** [DSA Radix Sort](https://www.w3schools.com/dsa/dsa_algo_radixsort.php)
- **YouTube:** [mycodeschool — Radix Sort](https://www.youtube.com/watch?v=xhr26ia4k38)
- **YouTube:** [Abdul Bari — Radix Sort](https://www.youtube.com/watch?v=nu4gDuFabIM)

---

## 🧠 Try It Yourself

1. Implement `counting_sort_by_digit` and `radix_sort`, then trace `[170, 45, 75, 90, 802, 24, 2, 66]` by hand, one digit pass at a time.
2. Explain in a comment why `counting_sort_by_digit` MUST be stable for radix sort to work (try replacing it with an unstable sort mentally — what breaks?).
3. (Challenge) Extend `radix_sort` to handle negative numbers by splitting the input into negatives and non-negatives, sorting each separately, and merging.
4. Compare radix sort against `sorted()` (Timsort) on a list of 100,000 random integers between 0 and 999. Which is faster, and by how much?
