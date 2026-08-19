# OOP Temperature Property

Source: oop_temperature_property

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Define a `Temperature` class that stores the value internally in Celsius (`self._celsius`), with a `celsius` property (getter + setter) AND a `fahrenheit` property (getter + setter) that stay in sync -- setting either one updates the underlying Celsius value so BOTH properties reflect the change consistently. Use `fahrenheit = celsius * 9/5 + 32`.

Expected function
```python
class Temperature:
    def __init__(self, celsius=0):
        pass

    @property
    def celsius(self):
        pass

    @celsius.setter
    def celsius(self, value):
        pass

    @property
    def fahrenheit(self):
        pass

    @fahrenheit.setter
    def fahrenheit(self, value):
        pass
```


Here is a possible program to test your function :
```python
t = Temperature(0)
print(t.fahrenheit)
t.fahrenheit = 212
print(round(t.celsius, 2))
```

And its output :
```text
32.0
100.0
```
