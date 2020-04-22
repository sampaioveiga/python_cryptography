# AES encryption of file

from Crypto.Cipher import AES
from Crypto import Random
import os, random, struct

def encrypt_file(key, filename, chunk_size=64*1024):
    output_filename = filename + '.encrypted'

    #iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    rnd = Random.new()
    iv = rnd.read(16)

    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(filename)

    with open(filename, 'rb') as inputfile:
        with open(output_filename, 'wb') as outputfile:
            outputfile.write(struct.pack('<Q', filesize))
            outputfile.write(iv)

            while True:
                chunk = inputfile.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) %16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outputfile.write(encryptor.encrypt(chunk))

encrypt_file('abcdefghi123456', 'sample_file.txt')