# Guessing Game Helper

Write a function named `evaluate_guess(secret, guess)` that compares a guessed number to a secret number.

## Requirements
- Return `"too low"` if the guess is smaller than the secret.
- Return `"too high"` if the guess is larger than the secret.
- Return `"correct"` if both values are equal.

## Example
```python
evaluate_guess(42, 20)  # "too low"
evaluate_guess(42, 70)  # "too high"
evaluate_guess(42, 42)  # "correct"
```
