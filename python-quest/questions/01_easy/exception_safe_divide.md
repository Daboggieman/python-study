# Exception Safe Divide

Source: exception_safe_divide

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Write a function that divides `a` by `b` using a full `try`/`except`/`else`/`finally` structure: catch `ZeroDivisionError` and return `None` in that case (after printing "Cannot divide by zero!"); on success, print "Division succeeded" from the `else` block; always print "Done" from the `finally` block; return the result on success.

Expected function
```python
def divide(a, b):
    pass
```


Here is a possible program to test your function :
```python
print(divide(10, 2))
print(divide(10, 0))
```

And its output :
```text
Division succeeded
Done
5.0
Cannot divide by zero!
Done
None
```
