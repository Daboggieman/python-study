# Fixthemain Main

Source: fixthemain_main

#### Files to submit:
- solution.py

#### Allowed functions:
- Only built-in functions (no external imports besides sys)

#### Instructions:
Write a function that reads a single string argument from the command line (sys.argv[1]),
removes all digit characters from it, converts the result to title case, and prints it,
followed by a blank line.

Expected function
```python
def fixthemain_main():
    pass
```
Here is a possible program to test your function:
```python
import sys
sys.argv = ["program", "hello123"]
fixthemain_main()
```
And its output:
```text
Hello
```