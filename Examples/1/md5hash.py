# MD5 hash generator

import hmac

# define secret key in bytes
hmac_md5 = hmac.new(b'my-secret-key', digestmod='MD5')

f = open('sample_file.txt', 'rb')
try:
    while True:
        block = f.read(1024)

        if not block:
            break
        hmac_md5.update(block)
finally:
    f.close

digest = hmac_md5.hexdigest()
print(digest)