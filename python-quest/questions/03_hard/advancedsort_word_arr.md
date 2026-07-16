# Advancedsort Word Arr

Source: advancedsort_word_arr

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Write a function that sorts a list of strings using a custom comparison function.

Expected function
```python
def advancedsort_word_arr():
    pass
```


Here is a possible program to test your function :
```python
words = ["banana", "apple", "cherry"]
print(advanced_sort_word_arr(words, lambda a, b: (a > b) - (a < b)))
```

And its output :
```text
['apple', 'banana', 'cherry']
```
