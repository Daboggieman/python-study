# 🐍 Python Study

A structured, self-paced Python curriculum with **100 piscine-style practice questions** — from absolute beginner to API design.

Built by combining lessons from the **[Net Ninja Python Playlist](https://www.youtube.com/playlist?list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK)** and concepts from **[Python Crash Course (3rd Edition)](https://nostarch.com/python-crash-course-3rd-edition)** by Eric Matthes.

---

## 📖 How to Use This Repo

### 1. Follow the Curriculum
Work through the `curriculum/` modules in order (01 → 15). Each module has:
- **`lecture.md`** — concise notes with code examples
- **`exercises.py`** — small practice exercises with `TODO` comments

### 2. Tackle the Piscine Quests
The `piscine_quests/` folder contains **100 coding challenges** across 7 difficulty tiers:

| Tier | Questions | Level | What You'll Practice |
|------|-----------|-------|---------------------|
| 🟢 Absolute Beginner | Q01–Q15 | First-time coder | print, input, variables, basic math |
| 🟡 Beginner | Q16–Q32 | Getting comfortable | lists, dicts, string methods, simple algorithms |
| 🟠 Elementary | Q33–Q50 | Building confidence | file I/O, recursion, parsing, mini-programs |
| 🔵 Intermediate | Q51–Q68 | Levelling up | OOP, decorators, generators, testing, CLI |
| 🟣 Advanced | Q69–Q80 | Going deep | concurrency, metaprogramming, design patterns |
| 🔴 API Design | Q81–Q92 | Real-world skills | REST, auth, pagination, WebSockets |
| ⚫ Capstone | Q93–Q100 | Putting it all together | Full projects with DB, auth, deployment |

Each question has a `README.md` with the problem statement and a `solution.py` you can check after attempting it.

### 3. Track Your Progress
Use `PROGRESS.md` to check off exercises as you complete them. Mark items:
- `[ ]` = not started
- `[~]` = in progress
- `[x]` = confident (can solve from memory)

### 4. Use the Resources
The `resources/` folder contains:
- 📚 Official PCC source code from the author's GitHub
- 📝 Chapter-by-chapter book notes
- 📋 Python cheatsheet
- 🔗 Useful links and references

---

## 📂 Repo Structure

```
python-study/
├── README.md              ← You are here
├── ROADMAP.md             ← Curriculum overview with status tracking
├── PROGRESS.md            ← Personal progress checklist
│
├── curriculum/            ← 15 structured learning modules
│   ├── 01_hello_python/
│   ├── 02_variables_types/
│   ├── ...
│   └── 15_final_project/
│
├── piscine_quests/        ← 100 practice questions
│   ├── 01_absolute_beginner/
│   ├── 02_beginner/
│   ├── 03_elementary/
│   ├── 04_intermediate/
│   ├── 05_advanced/
│   ├── 06_api_design/
│   └── 07_capstone_projects/
│
└── resources/             ← Books, notes, cheatsheets, links
    ├── pcc_3e_source/     ← Official Python Crash Course source code
    ├── book_notes/        ← Chapter summaries
    └── ...
```

---

## 🎯 Sources & Credits

| Source | What It Covers |
|--------|---------------|
| [Net Ninja Python Playlist](https://www.youtube.com/playlist?list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK) | Basics, data types, control flow, functions, file I/O, modules |
| [Python Crash Course 3e](https://nostarch.com/python-crash-course-3rd-edition) by Eric Matthes | Variables, lists, dicts, classes, testing, files, projects |
| [Official PCC Source Code](https://github.com/ehmatthes/pcc_3e) | Free companion code for every chapter |

---

## 🛠 Requirements

- **Python 3.12+** (any 3.10+ should work for most exercises)
- A code editor (VS Code recommended)
- `pip` for installing packages (API exercises only)

---

## 🤝 Contributing

This repo is primarily a personal study resource, but pull requests with:
- Bug fixes in solutions
- Additional practice questions
- Improved explanations

are welcome!

---

## 📜 License

Study materials and original code in this repo are open for educational use.
Python Crash Course source code is included under the author's original license — see `resources/pcc_3e_source/README.md`.
