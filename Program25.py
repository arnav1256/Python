def decrypt() :
    frase = str(input('Enter phrase: '))
    alph = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    total = 0
    for i in range (len(frase)) :
        if frase[i].lower() == 'a' :
            alph[0] += 1
            total += 1
        elif frase[i].lower() == 'b' :
            alph[1] += 1
            total += 1
        elif frase[i].lower() == 'c' :
            alph[2] += 1
            total += 1
        elif frase[i].lower() == 'd' :
            alph[3] += 1
            total += 1
        elif frase[i].lower() == 'e' :
            alph[4] += 1
            total += 1
        elif frase[i].lower() == 'f' :
            alph[5] += 1
            total += 1
        elif frase[i].lower() == 'g' :
            alph[6] += 1
            total += 1
        elif frase[i].lower() == 'h' :
            alph[7] += 1
            total += 1
        elif frase[i].lower() == 'i' :
            alph[8] += 1
            total += 1
        elif frase[i].lower() == 'j' :
            alph[9] += 1
            total += 1
        elif frase[i].lower() == 'k' :
            alph[10] += 1
            total += 1
        elif frase[i].lower() == 'l' :
            alph[11] += 1
            total += 1
        elif frase[i].lower() == 'm' :
            alph[12] += 1
            total += 1
        elif frase[i].lower() == 'n' :
            alph[13] += 1
            total += 1
        elif frase[i].lower() == 'o' :
            alph[14] += 1
            total += 1
        elif frase[i].lower() == 'p' :
            alph[15] += 1
            total += 1
        elif frase[i].lower() == 'q' :
            alph[16] += 1
            total += 1
        elif frase[i].lower() == 'r' :
            alph[17] += 1
            total += 1
        elif frase[i].lower() == 's' :
            alph[18] += 1
            total += 1
        elif frase[i].lower() == 't' :
            alph[19] += 1
            total += 1
        elif frase[i].lower() == 'u' :
            alph[20] += 1
            total += 1
        elif frase[i].lower() == 'v' :
            alph[21] += 1
            total += 1
        elif frase[i].lower() == 'w' :
            alph[22] += 1
            total += 1
        elif frase[i].lower() == 'x' :
            alph[23] += 1
            total += 1
        elif frase[i].lower() == 'y' :
            alph[24] += 1
            total += 1
        elif frase[i].lower() == 'z' :
            alph[25] += 1
            total += 1
    for i in range(len(alph)) :
        if alph[i] != 0 :
            if int(total/alph[i]) == 12:
                global key
                key = i
                print(alph)
                print(total)
                d(key, frase)
def d(key, frase):    
    print(key)
    put = []
    putput = ''
    for i in range (len(frase)) :
        if frase[i] == ' ' :
            put.append(' ')
        elif frase[i] == 'A' or frase[i] == 'a' :
            key -= 26
            put.append(chr(ord(frase[i])-key))
        elif ord(frase[i]) - key >= 122 or ord(frase[i]) - key >= 90:
            put.append(chr(ord(frase[i])-key))
        elif ord(frase[i]) - key < 122 or ord(frase[i]) - key < 90:
            put.append(chr(ord(frase[i])-key+24))
    for i in range(len(put)) :
        putput = putput + put[i]
    print(putput)
decrypt()
