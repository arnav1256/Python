def encrypt() :    
    key = int(input('Enter key: '))
    frase = str(input('Enter phrase: '))
    put = []
    putput = ''
    if key >= 26 :
        key -= 26
    for i in range (len(frase)) :
        if frase[i] == ' ' :
            put.append(' ')
        elif ord(frase[i]) + key <= 122 or ord(frase[i]) + key <= 90:
            put.append(chr(ord(frase[i])+key))
        elif ord(frase[i]) + key > 122 or ord(frase[i]) + key > 90:
            put.append(chr(ord(frase[i])+key-26))
    for i in range(len(put)) :
        putput = putput + put[i]
    print(putput)
def decrypt() :
    key = int(input('Enter key: '))
    frase = str(input('Enter phrase: '))
    put = []
    putput = ''
    for i in range (len(frase)) :
        if frase[i] == ' ' :
            put.append(' ')
        elif frase[i] == 'A' or frase[i] == 'a' :
            key -= 256
            put.append(chr(ord(frase[i])-key))
        elif ord(frase[i]) - key >= 122 or ord(frase[i]) - key >= 90:
            put.append(chr(ord(frase[i])-key))
        elif ord(frase[i]) - key < 122 or ord(frase[i]) - key < 90:
            put.append(chr(ord(frase[i])-key+26))
    for i in range(len(put)) :
        putput = putput + put[i]
    print(putput)
a = int(input('Enter 1 for encryption. Enter 2 for decryption. '))
if a == 1 :
    encrypt()
elif a == 2 :
    decrypt()
else:
    print('Invalid Input')