# SHA256 hash generator
import hmac
import hashlib

# define secret key in bytes
digest_maker = hmac.new(b'my-secret-key', digestmod = hashlib.sha256)

f = open('sample_file.txt', 'rb')
try:
    while True:
        block = f.read(1024)

        if not block:
            break
        digest_maker.update(block)
finally:
    f.close

digest = digest_maker.hexdigest()
print(digest)