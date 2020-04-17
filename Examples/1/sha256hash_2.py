# hash generator
import hmac
import hashlib
import sys

try:
    hash_name = sys.argv[1]
except IndexError:
    print('Specify hash name as first argument')
else:
    try:
        data = sys.argv[2]
    except IndexError:
        print('Specify data to hash as second argument')

h = hashlib.new(str(hash_name))
h.update(data.encode())

digest = h.hexdigest()
print(digest)