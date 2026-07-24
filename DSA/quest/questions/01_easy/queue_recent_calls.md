# Queue Recent Calls

Source: queue_recent_calls

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Design a `RecentCounter` class using a queue (`collections.deque`) that counts recent "pings". `ping(t)` adds a new ping at time `t` (milliseconds) and returns how many pings have occurred in the range `[t - 3000, t]`, inclusive. Assume calls to `ping` are made with strictly increasing values of `t`.

Expected function
```python
class RecentCounter:
    def __init__(self):
        pass

    def ping(self, t):
        pass
```


Here is a possible program to test your function :
```python
counter = RecentCounter()
print(counter.ping(1))
print(counter.ping(100))
print(counter.ping(3001))
print(counter.ping(3002))
```

And its output :
```text
1
2
3
3
```
