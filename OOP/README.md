# 🧱 OOP — Object-Oriented Programming

A dedicated module covering Python's object-oriented programming fundamentals, built in the same two-part style as the rest of this repo:

- **`curriculum/`** — 6 lessons (`lecture.md` + `exercises.py`), same format as the root `curriculum/` folder.
- **`quest/`** — 12 practice problems in the same style as the root `python-quest/` folder, spread across three difficulty tiers (`01_easy`, `02_intermediate`, `03_hard`), each with a question spec (`quest/questions/<tier>/`) and a starter answer stub (`quest/answers/`).
- **`resources/`** — `cheatsheet.md` (one-page reference for everything in this module) and `links.md` (every W3Schools/YouTube/article link used throughout, consolidated).

## Curriculum Order

| # | Topic |
|---|---|
| 01 | Classes and Objects |
| 02 | The `__init__` Method |
| 03 | The `self` Parameter |
| 04 | Class Properties (Attributes + `@property`) |
| 05 | Class Methods and Static Methods |
| 06 | Polymorphism (incl. inheritance basics + `super()`) |

## Suggested Study Flow

1. Read `curriculum/NN_topic/lecture.md`.
2. Complete `curriculum/NN_topic/exercises.py`.
3. Solve the matching `quest/` problems for that topic (filenames are prefixed `oop_`).
4. Keep `resources/cheatsheet.md` open as a running reference while you work.

This module assumes you're comfortable with the fundamentals in the root `curriculum/` folder (functions, loops, data types) — start there first if you haven't already. It pairs naturally with the `DSA/` module, since most custom data structures (linked lists, trees, etc.) are themselves built using classes.
