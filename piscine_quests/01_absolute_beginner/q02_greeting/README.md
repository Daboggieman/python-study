# Q02: Greeting

## Description
Write a script that prompts the user for their name, and then prints a customized greeting: `"Hello, [name]! Welcome to Python!"`.

## Example Interaction
```text
Enter your name: Alice
Hello, Alice! Welcome to Python!
```

## Constraints
- Do not hardcode the name in the final output. Use user input.

## Hints
- Use `input()` to get input from the user.
- Use an f-string to format the greeting.

---

## Solution
<details>
<summary>View Solution</summary>

```python
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to Python!")
```
</details>
