# File Organizer

Write a function named `organize_files(paths)` that groups file paths by their extension.

## Requirements
- Input is a list of strings representing file paths.
- Return a dictionary where each key is an extension and each value is a list of matching file paths.
- If a file has no extension, group it under `"no_extension"`.

## Example
```python
organize_files(["notes.txt", "image.png", "README", "data.txt"])
# -> {"txt": ["notes.txt", "data.txt"], "png": ["image.png"], "no_extension": ["README"]}
```
