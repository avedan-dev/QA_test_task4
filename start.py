#! ./venv/bin/python
import subprocess
s = input()
if s == 'execute':
    subprocess.run("pytest")
