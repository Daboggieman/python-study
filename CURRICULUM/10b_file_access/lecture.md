# Lecture 10b: File Access, Reading, and Writing

This lesson focuses on working with files in Python: opening them, reading data, writing data, and using the operating system to manage files.

---

## 1. File Paths and Access
A file path tells Python where to find a file. It can be:
- **relative**: `data/sample.txt`
- **absolute**: `/home/user/data/sample.txt`

Use the `open()` function to access a file.

```python
file = open("notes.txt", "r")
```

Common file modes:
- `r` — read (default)
- `w` — write (creates or overwrites)
- `a` — append (add to end)
- `x` — create (fails if file exists)
- `r+` — read and write

---

## 2. Reading from Files
Use `read()`, `readline()`, or `readlines()`.

```python
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
```

Read line by line:

```python
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())
```

---

## 3. Writing to Files
Write text with `write()` or `writelines()`.

```python
with open("output.txt", "w") as file:
    file.write("Hello, file world!\n")
```

Append instead of overwrite:

```python
with open("output.txt", "a") as file:
    file.write("More text\n")
```

---

## 4. File System Helpers
Python’s `os` module helps inspect files and folders.

```python
import os
print(os.path.exists("notes.txt"))
print(os.path.isfile("notes.txt"))
print(os.path.isdir("data"))
```

Create a folder:

```python
os.makedirs("data", exist_ok=True)
```

Delete a file:

```python
os.remove("old.txt")
```

---

## 5. Practical Notes
- Always close files when you are done. `with` handles this automatically.
- Use `'w'` carefully: it erases existing content.
- Convert input strings to the right type before writing if needed.

---

## 🧠 Try It Yourself
1. Create or overwrite a file named `log.txt` and write two lines of text.
2. Read the file back and print each line.
3. Check whether `log.txt` exists using `os.path.exists()`.
