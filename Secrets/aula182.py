# secrets
import os
import secrets
import string as Str
from secrets import SystemRandom as SysRand

os.system('cls')

senha = SysRand().choices(
    Str.ascii_letters + Str.digits + Str.punctuation, k=12
)

print(''.join(senha))

random = secrets.SystemRandom()
