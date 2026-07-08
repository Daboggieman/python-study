# Lecture 13: Pip & Virtual Envs

When building Python applications, you will often need to use third-party packages that are not part of the standard library. To manage these libraries, we use **Pip** and **Virtual Environments**.

---

## 1. Third-Party Packages and PyPI
The **Python Package Index (PyPI)** is a repository of software for the Python programming language. Developers publish libraries here, and you can download them using **pip** (Python's package installer).

---

## 2. Why Virtual Environments?
A **virtual environment** is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.

### The Problem:
If you install all packages globally, different projects might require different versions of the same package (e.g., Project A needs Django 3.2, Project B needs Django 4.0). This leads to dependency conflicts.

### The Solution:
Use a virtual environment for each project to isolate its dependencies.

---

## 3. Managing Virtual Environments

### Creating a Virtual Environment
Run this command in your project directory:
```bash
python -m venv .venv
```
This creates a folder named `.venv` containing a local copy of Python and pip.

### Activating the Environment
Before installing packages, you must activate the virtual environment:

- **Windows (Command Prompt)**:
  ```cmd
  .venv\Scripts\activate.bat
  ```
- **Windows (PowerShell)**:
  ```powershell
  .venv\Scripts\activate.ps1
  ```
- **macOS / Linux**:
  ```bash
  source .venv/bin/activate
  ```

Once activated, your terminal prompt will be prefixed with `(.venv)`.

### Deactivating
When you're done working, deactivate it:
```bash
deactivate
```

---

## 4. Using Pip to Manage Packages

With your virtual environment activated, you can install packages:

```bash
# Install a package
pip install requests

# Install a specific version
pip install requests==2.31.0

# Upgrade a package
pip install --upgrade requests

# Uninstall a package
pip install -y requests
```

---

## 5. Requirements Files
To share projects, you should document the dependencies. We do this by creating a `requirements.txt` file.

```bash
# Generate requirements.txt
pip freeze > requirements.txt

# Install dependencies from requirements.txt
pip install -r requirements.txt
```

---

## 🧠 Try It Yourself
1. Create a virtual environment named `.venv_test` in a temporary folder.
2. Activate it, install the `requests` library, and check its version using `pip show requests`.
3. Deactivate the environment and delete the folder.
