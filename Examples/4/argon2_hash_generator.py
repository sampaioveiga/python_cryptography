# Argon2 password hash generator
from argon2 import PasswordHasher
import sys

ph = PasswordHasher()

try:
    password = sys.argv[1]
except IndexError:
    print('Usage: python hash_generator.py password')
    sys.exit()

h = ph.hash(password)
print(h)