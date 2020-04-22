from Crypto.Cipher import AES

key = b'1234567890123456'
file_in = open('encrypted.bin', 'rb')
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)

print(data.decode())