l = 0
n = int(input())
if n == 1:
    print(5)
    exit()
global num
def getlen(m):
    global l, num
    i = 0
    while m>0:
        if i == 0:
            m-=9**i
            l += 1
            if m <= 0:
                num = m+9**i
                return l
        else:
            m -= (9 ** i)
            l += 1
            if m <= 0:
                num = m + 9 ** i
                return l
            m -= (9 ** i)
            l += 1
            if m <= 0:
                num = m + 9 ** i
                return l
        i+=1
getlen(n)
def recur(m):
    ns = []
    if m%2==0:
        if m==2:
            [ns.append("".join([str(i), str(10 - i)])) for i in range(1, 10)]
            return ns
        else:
            e = recur(m-2)
            f = []
            for i in range(1,10):
                st = ''.join([str(i),str(10-i)])
                for k in e:
                    o = list(k)
                    o.insert(len(o)//2,st)
                    f.append(o)
            return f
    else:
        if m==3:
            [ns.append("".join([str(i), "5", str(10 - i)])) for i in range(1, 10)]
            return ns
        else:
            e = recur(m-2)
            f = []
            for i in range(1,10):
                st = ''.join([str(i),str(10-i)])
                for k in e:
                    o = list(k)
                    o.insert(len(o)//2,st[0])
                    o.insert(len(o)//2+1,st[1])
                    f.append(o)
            return f
final = recur(l)
for i in range(len(final)):
    final[i] = ''.join(final[i])
    final[i] = int(final[i])
print(sorted(final)[num-1])