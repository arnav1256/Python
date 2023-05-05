a,b,n=input().split();l=""
f=[a,b]
for i in range(int(n)-2):
    v=ord(f[-2])-64+ord(f[-1])-64
    if v>26: v-=26
    f.append(chr(v+64))
print(f[int(n)-1])