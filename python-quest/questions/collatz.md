### DONE

# Collatz Countdown

Source: collatz

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Write a function that returns the number of steps needed to reach 1 using the Collatz sequence.

Expected function
```python
def collatz_countdown(start):
    pass
```


Here is a possible program to test your function :
```python
print(collatz_countdown(12))
```

And its output :
```text
9
```

if number is even divide by 2, if number is odd multiply number by 3 and add 1 and repeat the sequence again till the final answer is 1
