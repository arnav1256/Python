def getLetter(a, b):
    a, b = ord(a) - 64, ord(b) - 64
    enc = a - b #difference between the letters
    if enc < 1:
        enc += 26
    return chr(enc + 64)
st = list(input())
for i in range(len(st) - 1, 0, -1):
    st[i] = getLetter(st[i], st[i - 1])
print(''.join(st)) #prints all the letters joined into a string
