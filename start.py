#! ./venv/bin/python
import sys
import subprocess
if len(sys.argv) > 1:
    if sys.argv[1] == 'execute':
        subprocess.run("pytest")
    else:
        print('Введите execute для старта тестирования')
        s = input()
        if s == 'execute':
            subprocess.run("pytest")
else:
    print('Введите execute для старта тестирования')
    s = input()
    if s == 'execute':
        subprocess.run("pytest")
