# Hash Group Anagrams

Source: hash_group_anagrams

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Write a function that groups a list of strings into anagram groups, using a dictionary keyed by each word's sorted-letters signature (e.g. "eat" and "tea" both map to the key "aet"). Return a list of lists; the order of groups and order within groups should follow the first-seen order of the input.

Expected function
```python
def group_anagrams(words):
    pass
```


Here is a possible program to test your function :
```python
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
```

And its output :
```text
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```
