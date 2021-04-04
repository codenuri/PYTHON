st = dir(bool)
print(st)

input()

import glob
st = glob.glob('C:\\windows\\system32\\*.exe')
print(st)

input()

import subprocess
subprocess.run(['notepad.exe', 'a.txt'])