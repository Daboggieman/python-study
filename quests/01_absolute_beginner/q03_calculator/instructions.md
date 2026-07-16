# Q03: Calculator

## Description
Write a script that asks the user to enter two numbers, and then prints their sum, difference, product, and quotient.

## Example Interaction
```text
Enter first number: 10
Enter second number: 2
Sum: 12.0
Difference: 8.0
Product: 20.0
Quotient: 5.0
```

## Constraints
- Convert user input to floats so that calculations handle decimal inputs.

## Hints
- `input()` returns a string. Convert it using `float(value)`.
- Use formatting or basic math operations (`+`, `-`, `*`, `/`).

---

## Solution
<details>
<summary>View Solution</summary>

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")
```
</details>
