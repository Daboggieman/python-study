# Word Counter

Write a function named `count_words(text)` that counts how many times each word appears in a string.

## Requirements
- Ignore punctuation such as `. , ! ? : ;`.
- Treat uppercase and lowercase as the same.
- Return a dictionary where the keys are lowercase words and the values are counts.

## Example
```python
count_words("Python is fun, fun for everyone!")
# -> {"python": 1, "is": 1, "fun": 2, "for": 1, "everyone": 1}
```

## Hint
Split the text into words, clean each word, and update a dictionary.
