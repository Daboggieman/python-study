# 20: The `math` Module

Python's built-in arithmetic (`+`, `-`, `*`, `/`) covers the basics, but real programs frequently need square roots, trigonometry, logarithms, and more precise constants. That's what the standard library's `math` module provides.

---

## 1. Constants

```python
import math

print(math.pi)     # 3.141592653589793
print(math.e)        # 2.718281828459045
print(math.inf)       # infinity -- useful as a starting "worst case" value
print(math.nan)        # "not a number"
```

```python
best_so_far = math.inf
for value in [5, 2, 8, 1]:
    best_so_far = min(best_so_far, value)
print(best_so_far)   # 1
```

---

## 2. Rounding and Truncation

```python
print(math.floor(4.7))    # 4  -- always rounds DOWN
print(math.ceil(4.2))       # 5  -- always rounds UP
print(math.trunc(4.9))       # 4  -- chops off the decimal, toward zero
print(math.trunc(-4.9))       # -4 -- note: different from floor(-4.9), which is -5!
print(round(4.5))              # 4  -- Python's round() uses "round half to even" (banker's rounding)
```

---

## 3. Powers, Roots, and Logarithms

```python
print(math.sqrt(16))          # 4.0
print(math.pow(2, 10))         # 1024.0  -- always returns a float, unlike 2 ** 10
print(math.log(100, 10))        # 2.0     -- log base 10 of 100
print(math.log2(8))               # 3.0
print(math.log10(1000))            # 3.0
print(math.exp(1))                  # 2.718281828459045 -- e^1
```

---

## 4. Trigonometry

```python
print(math.sin(math.pi / 2))    # 1.0
print(math.cos(0))                 # 1.0
print(math.degrees(math.pi))        # 180.0
print(math.radians(180))              # 3.141592653589793
```

Trig functions expect **radians**, not degrees — `math.degrees()`/`math.radians()` convert between them.

---

## 5. Useful Utility Functions

```python
print(math.gcd(48, 18))         # 6 -- greatest common divisor
print(math.factorial(5))           # 120
print(math.isclose(0.1 + 0.2, 0.3))  # True -- safely compares floats (see below)
print(math.hypot(3, 4))               # 5.0 -- Euclidean distance/hypotenuse
```

**Why `math.isclose()` matters:** floating-point numbers can't represent every decimal value exactly, so `0.1 + 0.2 == 0.3` is actually `False` in Python! `math.isclose()` compares with a small tolerance instead of exact equality, which is almost always what you actually want when comparing floats.

```python
print(0.1 + 0.2 == 0.3)              # False (!)
print(math.isclose(0.1 + 0.2, 0.3))    # True
```

---

## 6. `math` vs the Built-in `statistics` Module

For averages, medians, and standard deviation, reach for the separate `statistics` module instead:

```python
import statistics

data = [2, 4, 4, 4, 5, 5, 7, 9]
print(statistics.mean(data))     # 5.0
print(statistics.median(data))    # 4.5
print(statistics.stdev(data))       # 2.13809...
```

---

## 📚 Resources

- **W3Schools:** [Python Math Module](https://www.w3schools.com/python/module_math.asp)
- **Docs:** [`math` — Mathematical functions](https://docs.python.org/3/library/math.html)
- **YouTube:** [Corey Schafer — Python Tutorial: Math Module](https://www.youtube.com/watch?v=EBWTsSMlpFo)
- **Docs:** [`statistics` module](https://docs.python.org/3/library/statistics.html)

---

## 🧠 Try It Yourself

1. Write a function `hypotenuse(a, b)` using `math.sqrt` (then check your answer against `math.hypot(a, b)`).
2. Demonstrate the floating-point precision problem: print `0.1 + 0.2 == 0.3` and then the correct comparison using `math.isclose()`.
3. Write a function `is_prime(n)` that checks primality efficiently by only testing divisors up to `math.sqrt(n)` (no need to check beyond that point).
4. Compute the mean and standard deviation of a list of 10 numbers using the `statistics` module.
