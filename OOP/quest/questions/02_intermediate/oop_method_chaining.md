# OOP Method Chaining

Source: oop_method_chaining

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Define a `StringBuilder` class with an internal list of parts. Add an `add(self, text)` method that appends `text` and returns `self` (enabling method chaining), and a `build(self)` method that returns all parts joined into one string with no separator.

Expected function
```python
class StringBuilder:
    def __init__(self):
        pass

    def add(self, text):
        pass

    def build(self):
        pass
```


Here is a possible program to test your function :
```python
result = StringBuilder().add("Hello").add(", ").add("world!").build()
print(result)
```

And its output :
```text
Hello, world!
```
