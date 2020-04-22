'This is a very secret messate'.encode('utf-8')# AES encryption of text

from Crypto.Cipher import AES

key = b'1234567890123456'
data = input('Input your message here: ')

cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))

file_out = open('encrypted.bin', 'wb')
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]

file_out.close()