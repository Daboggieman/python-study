# Q05: String Length

## Description
Write a script that prompts the user for a string, and then calculates and prints the number of characters in that string **without** using Python's built-in `len()` function.

## Example Interaction
```text
Enter a string: Python
Length: 6
```

## Constraints
- **Do not** use the built-in `len()` function.

## Hints
- Use a `for` loop to iterate over characters in the string, maintaining a counter variable that starts at `0`.

---

## Solution
<details>
<summary>View Solution</summary>

```python
text = input("Enter a string: ")
count = 0
for char in text:
    count += 1
print(f"Length: {count}")
```
</details>
