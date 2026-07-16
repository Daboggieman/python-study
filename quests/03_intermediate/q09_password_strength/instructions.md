# Password Strength

Write a function named `password_strength(password)` that rates a password based on its complexity.

## Requirements
- Return `"weak"` if the password is shorter than 8 characters.
- Return `"medium"` if it is at least 8 characters long and has either uppercase or digits.
- Return `"strong"` if it has at least 8 characters, an uppercase letter, a lowercase letter, and a digit.

## Example
```python
password_strength("abc123")  # "medium"
password_strength("Abc12345")  # "strong"
password_strength("hello")  # "weak"
```
