# 18: Iterators and Generators

Every `for` loop you've ever written relies on a concept called the **iterator protocol**. This lesson pulls back the curtain on how `for x in something:` actually works, then introduces **generators** — a much simpler way to write your own iterators.

---

## 1. Iterable vs Iterator

- An **iterable** is anything you can loop over (`list`, `str`, `dict`, `range`, etc.) — it has an `__iter__` method.
- An **iterator** is the object that actually does the stepping — it has a `__next__` method that returns the next value, and raises `StopIteration` when exhausted.

```python
nums = [1, 2, 3]              # nums is an ITERABLE
it = iter(nums)                  # iter() asks it for an ITERATOR
print(next(it))                   # 1
print(next(it))                   # 2
print(next(it))                   # 3
print(next(it))                   # raises StopIteration
```

A `for` loop is just this process automated:
```python
for x in nums:
    print(x)

# is roughly equivalent to:
it = iter(nums)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    print(x)
```

---

## 2. Building Your Own Iterator (the Verbose Way)

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self          # the iterable IS its own iterator here

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for n in Countdown(3):
    print(n)     # 3, 2, 1
```

This works, but it's a lot of boilerplate for something conceptually simple. That's exactly the problem generators solve.

---

## 3. Generators: The Easy Way

A **generator function** uses `yield` instead of `return`. Each call to `yield` pauses the function, remembering exactly where it left off, and resumes from that point the next time a value is requested.

```python
def countdown(start):
    current = start
    while current > 0:
        yield current
        current -= 1

for n in countdown(3):
    print(n)     # 3, 2, 1
```

Same behavior as the `Countdown` class above, in 5 lines instead of 12. `countdown(3)` doesn't run the function immediately — calling a generator function returns a **generator object**, and the code only actually runs step-by-step as you iterate it.

```python
gen = countdown(3)
print(gen)          # <generator object countdown at 0x...>
print(next(gen))     # 3 -- runs up to the first yield
print(next(gen))     # 2 -- resumes right after the last yield
```

---

## 4. Why Generators Matter: Laziness and Memory

```python
def all_squares_list(n):
    return [i ** 2 for i in range(n)]     # builds the ENTIRE list in memory at once

def all_squares_gen(n):
    for i in range(n):
        yield i ** 2                        # produces ONE value at a time, on demand

# all_squares_list(10_000_000) allocates a huge list immediately.
# all_squares_gen(10_000_000) uses almost no memory until you actually consume it.
for sq in all_squares_gen(10_000_000):
    if sq > 100:
        break     # we only ever computed a handful of squares, not 10 million
```

This "produce values one at a time, only when asked" behavior is called **laziness**, and it's why generators are the standard tool for processing large or infinite sequences.

---

## 5. Generator Expressions

Just like list comprehensions have a generator equivalent:

```python
squares_list = [x**2 for x in range(5)]     # a list, built immediately -- [0, 1, 4, 9, 16]
squares_gen = (x**2 for x in range(5))       # a generator, built lazily
print(sum(squares_gen))                        # 30 -- generators work great with sum(), max(), etc.
```

---

## 6. `itertools` — The Standard Library's Generator Toolbox

```python
import itertools

print(list(itertools.count(1, 2)[:5] if False else []))  # (count() is infinite -- see below)

counter = itertools.count(start=1, step=2)     # infinite: 1, 3, 5, 7, ...
print([next(counter) for _ in range(5)])         # [1, 3, 5, 7, 9]

print(list(itertools.chain([1, 2], [3, 4])))       # [1, 2, 3, 4]
print(list(itertools.permutations([1, 2, 3], 2)))    # all length-2 orderings
```

---

## 📚 Resources

- **W3Schools:** [Python Iterators](https://www.w3schools.com/python/python_iterators.asp)
- **YouTube:** [Corey Schafer — Python Generators Tutorial](https://www.youtube.com/watch?v=bD05uGo_sVI)
- **YouTube:** [mCoding — Iterators and Iterables](https://www.youtube.com/watch?v=jTYiNjvnHZY)
- **Real Python:** [How to Use Generators and yield in Python](https://realpython.com/introduction-to-python-generators/)
- **Docs:** [`itertools` module](https://docs.python.org/3/library/itertools.html)

---

## 🧠 Try It Yourself

1. Build the `Countdown` iterator class exactly as shown, then rewrite it as a `countdown()` generator function — confirm both produce identical output.
2. Write a generator `fibonacci(n)` that yields the first `n` Fibonacci numbers, one at a time.
3. Use a generator expression with `sum()` to compute the sum of squares from 1 to 1,000,000 without ever building a full list.
4. Explore `itertools.count`, `itertools.chain`, and `itertools.permutations` — write one small example program using each.
