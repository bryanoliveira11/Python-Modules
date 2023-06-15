# subprocess
import subprocess
import sys

cmd = ['ping', '127.0.0.1']

if sys.platform == 'win32':
    cmd = ['dir']

proc = subprocess.run(
    cmd,
    capture_output=True,
    text=True,
    encoding='cp850')

# print(proc.args)
# print(proc.stderr)
print(proc.stdout)
# print(proc.returncode)
