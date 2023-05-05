import math
from cryptography.fernet import Fernet

#key generation
key = Fernet.generate_key()
f = Fernet(key)

#encryption
data = input('Enter message to be encrypted: ').encode()
encryption = f.encrypt(data).decode('utf-8').replace('gAAAAAB', '')
print('Ciphertext:', encryption)
print('Key:', key.decode('utf-8'))

#decryption
data = 'gAAAAAB' + encryption
data = data.encode('utf-8')
print('Plaintext after decoding:', f.decrypt(data).decode('utf-8'))