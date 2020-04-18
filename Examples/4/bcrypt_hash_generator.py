import bcrypt

password = input('Insert password: ')
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password.encode(), salt)

print(salt.decode())
print(hashed.decode())