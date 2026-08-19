# 19: Modules Deep Dive

Lesson 16 introduced `import` at a basic level. This lesson goes deeper: how modules and packages actually work, what `__name__ == "__main__"` really means, and how Python finds the modules you import.

---

## 1. Every `.py` File Is a Module

Any Python file can be imported by another. If you have `mathutils.py`:

```python
# mathutils.py
def square(x):
    return x * x

PI = 3.14159
```

```python
# main.py
import mathutils
print(mathutils.square(5))    # 25
print(mathutils.PI)             # 3.14159
```

Import styles:
```python
import mathutils                       # access via mathutils.square(...)
from mathutils import square           # access via square(...) directly
from mathutils import square as sq     # rename on import
import mathutils as mu                  # rename the whole module
from mathutils import *                  # import everything (generally discouraged -- unclear where names came from)
```

---

## 2. `__name__ == "__main__"` — The Most Important Idiom in This Lesson

Every module has a built-in `__name__` variable. When a file is **run directly**, `__name__` is set to `"__main__"`. When a file is **imported** by another file, `__name__` is set to that module's actual name instead.

```python
# mathutils.py
def square(x):
    return x * x

print(f"mathutils module loaded, __name__ is {__name__}")

if __name__ == "__main__":
    print("Running mathutils.py directly!")
    print(square(4))
```

Run `python mathutils.py` directly → prints both lines (both the load message and the "Running directly" block).
Run `import mathutils` from another file → only prints the load message; the `if` block is skipped.

**Why this matters:** it lets a file be both a reusable module AND a standalone script with its own test/demo code, without that demo code running every single time someone imports it elsewhere.

---

## 3. Packages: Folders of Modules

A **package** is a folder containing an `__init__.py` file (which can be empty) plus one or more modules:

```
mypackage/
    __init__.py
    shapes.py
    colors.py
```

```python
from mypackage import shapes
from mypackage.colors import RED
```

`__init__.py` runs automatically the first time anything from the package is imported — it's a natural place to control what's exposed, e.g.:

```python
# mypackage/__init__.py
from .shapes import Circle, Square    # so `from mypackage import Circle` works directly
```

---

## 4. Where Python Looks for Modules: `sys.path`

```python
import sys
print(sys.path)   # a list of directories Python searches, in order, when you `import`
```

Python checks (roughly, in order): the current script's directory, any directories in the `PYTHONPATH` environment variable, then the standard library and installed site-packages locations. If `import foo` fails with `ModuleNotFoundError`, it usually means `foo` isn't in any of these locations — this is very often a virtual environment issue (see Lesson 23!).

---

## 5. Relative vs Absolute Imports

```python
# Absolute import -- full path from the project root, generally preferred
from mypackage.shapes import Circle

# Relative import -- only valid inside a package, relative to the current module's location
from .shapes import Circle       # same directory
from ..otherpackage import thing  # one directory up
```

---

## 6. `__all__` — Controlling `import *`

```python
# mymodule.py
__all__ = ["public_function"]     # only this name is exported by `from mymodule import *`

def public_function():
    pass

def _private_helper():          # a leading underscore also signals "internal use"
    pass
```

---

## 📚 Resources

- **W3Schools:** [Python Modules](https://www.w3schools.com/python/python_modules.asp) · [Python Packages](https://www.w3schools.com/python/python_packages.asp)
- **YouTube:** [Corey Schafer — Python Modules and Packages](https://www.youtube.com/watch?v=CqvZ3vGoGs0)
- **YouTube:** [mCoding — `if __name__ == "__main__"` explained](https://www.youtube.com/watch?v=g_wlZ9IhbTs)
- **Real Python:** [Python Modules and Packages — An Introduction](https://realpython.com/python-modules-packages/)

---

## 🧠 Try It Yourself

1. Create two files, `mathutils.py` (with a function and a demo `if __name__ == "__main__":` block) and `main.py` that imports and uses it. Run both files directly and confirm the demo block only runs for `mathutils.py`.
2. Print `sys.path` on your machine and identify at least 2 directories in the list.
3. Create a small package folder with `__init__.py` and two modules, then import something from it both via `from package import module` and by re-exporting a name through `__init__.py`.
4. Add an `__all__` list to one of your modules and test what `from mymodule import *` exposes with and without it.
