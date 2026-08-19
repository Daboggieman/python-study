# Lecture 13b: Terminal, Shells, and Git Basics

This lesson teaches the command line, shell types, and the basic Git workflow.

---

## 1. What Is a Terminal?
A terminal is a text window where you type commands. It lets you work directly with the operating system.

Common terminals:
- Bash or Zsh on Linux/macOS
- Command Prompt (`cmd`) on Windows
- PowerShell (`psh`) on Windows

---

## 2. Basic Commands
Navigate folders and inspect files:

- `pwd` — print current folder
- `ls` / `dir` — list files
- `cd <folder>` — change directory
- `mkdir <folder>` — create a folder
- `rm <file>` / `del <file>` — delete a file
- `cp` / `copy` — copy files
- `mv` / `move` — move or rename files

Examples:
```bash
cd python-study
ls
mkdir projects
```

---

## 3. PowerShell and Batch Basics
PowerShell runs commands like `Get-ChildItem` and `Set-Location`.

```powershell
Get-ChildItem
Set-Location .\python-study
```

Windows batch files use commands like `echo` and `dir`.

```bat
echo Hello from batch
dir
echo Done
```

---

## 4. Git Basics
Git tracks changes to files and lets you share work.

Common commands:
- `git init` — create a repository
- `git status` — see changes
- `git add .` — stage changes
- `git commit -m "message"` — save a snapshot
- `git branch` — list branches
- `git checkout <branch>` — switch branch
- `git push` — send changes to remote
- `git pull` — fetch remote changes

Example workflow:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <url>
git push -u origin main
```

---

## 5. Why This Matters
Using the terminal and Git is essential for productive work in Python projects. It makes tasks faster and helps you keep a history of your code.

---

## 🧠 Try It Yourself
1. Open a terminal and run `pwd` or `cd` to a project folder.
2. Use `git status` in a repository.
3. Create a simple batch file or PowerShell script that prints a message.
