# Q04: Even or Odd

## Description
Write a script that prompts the user for an integer, and prints `"Even"` if the number is even, and `"Odd"` if the number is odd.

## Example Interaction
```text
Enter an integer: 7
Odd
```

## Constraints
- Use an integer conversion `int()` for input.

## Hints
- Use the modulo operator `%`. A number is even if `number % 2 == 0`.

---

## Solution
<details>
<summary>View Solution</summary>

```python
num = int(input("Enter an integer: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```
</details>
