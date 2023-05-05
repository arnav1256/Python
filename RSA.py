from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(1024)

pubKey = keyPair.publickey()
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))


msg = bytes(str(input("Enter plain text: ")), 'utf-8')
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted).decode('UTF-8'))

decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted.decode('utf-8'))
