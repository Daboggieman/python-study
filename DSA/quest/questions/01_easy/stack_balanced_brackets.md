# Stack Balanced Brackets

Source: stack_balanced_brackets

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Write a function that uses a stack (a plain Python list used as a stack -- only `.append()` and `.pop()`) to check whether the brackets `()`, `[]`, `{}` in a string are balanced and correctly nested.

Expected function
```python
def is_balanced(expression):
    pass
```


Here is a possible program to test your function :
```python
print(is_balanced("{[()()]}"))
print(is_balanced("{[(])}"))
print(is_balanced("((("))
```

And its output :
```text
True
False
False
```
