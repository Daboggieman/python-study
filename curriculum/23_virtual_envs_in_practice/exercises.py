# Exercise 23: Virtual Environments in Practice
#
# This lesson is primarily hands-on with your TERMINAL, not this file --
# see lecture.md's "Try It Yourself" section for the actual exercises
# (creating a venv, freezing requirements, recreating from scratch, etc).
#
# Use this file to write a short helper and to record what you observed.

import sys
import os


# TODO: Exercise (helper) - print whether the CURRENT python process is
# running inside a virtual environment. Hint: check for `sys.prefix !=
# sys.base_prefix`, which is True only when a venv is active.
def in_virtual_env():
    pass


if __name__ == "__main__":
    print("Running inside a virtual environment:", in_virtual_env())
    print("Python executable:", sys.executable)

    # TODO: After completing the terminal exercises in lecture.md, write a
    # one-paragraph comment below summarizing what you observed when you
    # ran `pip list` in an activated vs. a non-activated terminal.
