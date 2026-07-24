# 23: Virtual Environments in Practice

Lesson 13 introduced `venv` at a basic level (create it, activate it, install packages). This lesson focuses on the *practical, day-to-day* workflow: managing dependencies with `requirements.txt`, avoiding common mistakes, and understanding what a virtual environment is actually doing.

---

## 1. Quick Recap: Creating and Activating

```bash
python -m venv .venv          # create a virtual environment in a folder named .venv

# Activate it:
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate           # Windows

deactivate                        # leave the virtual environment, any OS
```

Once activated, your shell prompt usually shows `(.venv)` at the start, and `python`/`pip` now point at the isolated environment's copies instead of your system-wide Python.

---

## 2. Why Isolation Actually Matters (a Concrete Scenario)

Imagine two projects on your machine:
- **Project A** needs `requests==2.25.0` (an older version, for compatibility reasons)
- **Project B** needs `requests==2.31.0` (the latest, for a security fix)

Without virtual environments, installing one version system-wide breaks the other project. Each project gets its **own** `.venv` folder with its **own** installed packages, completely isolated from every other project and from your system Python.

```bash
cd project-a && python -m venv .venv && source .venv/bin/activate && pip install requests==2.25.0
cd ../project-b && python -m venv .venv && source .venv/bin/activate && pip install requests==2.31.0
# both installations coexist peacefully, because they live in separate .venv folders
```

---

## 3. `requirements.txt` — Recording and Restoring Dependencies

Once you've installed the packages your project needs, "freeze" the exact versions into a file:

```bash
pip freeze > requirements.txt
```

This produces a file like:
```
requests==2.31.0
numpy==1.26.4
flask==3.0.2
```

Anyone else (including future you, on a new machine) can recreate the exact same environment with one command:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**This is why `requirements.txt` belongs in version control, but `.venv/` itself should NOT** — the venv folder can be huge, is machine-specific, and is trivially regenerated from `requirements.txt`. Add this to your `.gitignore`:

```
.venv/
__pycache__/
*.pyc
```

---

## 4. Checking What's Installed

```bash
pip list                    # everything installed in the CURRENT (activated) environment
pip show requests            # detailed info about one specific package
which python                  # (macOS/Linux) confirms which Python binary is active
where python                   # (Windows) same idea
```

If `pip list` shows packages you didn't expect, or `import` fails for something you're sure you installed, the most common cause is **forgetting to activate the virtual environment** in that terminal session.

---

## 5. A Common Gotcha: Per-Terminal Activation

Activation only affects the **current terminal session**. If you open a new terminal tab/window, it starts back at your system Python — you have to `source .venv/bin/activate` again in the new session. Many editors (VS Code, PyCharm) can be configured to auto-select and auto-activate a project's virtual environment, which avoids this trip-up.

---

## 6. Alternative Tools (What Else Is Out There)

| Tool | What it adds over plain `venv` |
|---|---|
| `venv` (standard library) | Nothing extra — the baseline, always available |
| `virtualenv` | A faster, more feature-rich third-party predecessor to `venv` |
| `pipenv` | Combines venv management + `requirements.txt`-like locking into one tool (`Pipfile`) |
| `poetry` | Full dependency management + packaging + publishing workflow |
| `conda` | Manages non-Python dependencies too (C libraries, R, etc.) — popular in data science |

For most learning projects, the standard library's `venv` + `requirements.txt` combo (what this lesson focuses on) is entirely sufficient, and it's the one workflow guaranteed to exist on any machine with Python installed.

---

## 📚 Resources

- **W3Schools:** [Python Virtual Environment](https://www.w3schools.com/python/python_virtualenv.asp)
- **Docs:** [`venv` — Creation of virtual environments](https://docs.python.org/3/library/venv.html)
- **YouTube:** [Corey Schafer — Python Tutorial: VENV](https://www.youtube.com/watch?v=Kg1Yvry_Ydk)
- **Real Python:** [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)

---

## 🧠 Try It Yourself

1. Create a new virtual environment, activate it, and install any one package (e.g. `requests`). Run `pip freeze > requirements.txt` and look at the resulting file.
2. Deactivate, delete the `.venv` folder entirely, then recreate the environment from scratch using only `requirements.txt` — confirm everything still works.
3. Create a `.gitignore` file that excludes `.venv/`, `__pycache__/`, and `*.pyc`.
4. Open two separate terminal sessions, activate the venv in only one of them, and run `pip list` in both — observe the difference and explain in a comment why it happens.
