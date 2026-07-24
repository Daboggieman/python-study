# Radix Sort Strings Fixed Length

Source: radix_sort_strings_fixed_length

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Adapt radix sort to sort a list of strings that are all the SAME fixed length (e.g. product codes like "B12", "A99"), sorting character-position by character-position from the rightmost character to the leftmost, using a stable counting sort keyed on character ordinal value at each position.

Expected function
```python
def radix_sort_strings(words):
    pass
```


Here is a possible program to test your function :
```python
print(radix_sort_strings(["dda", "aac", "bcb", "aad"]))
```

And its output :
```text
['aac', 'aad', 'bcb', 'dda']
```
