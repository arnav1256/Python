#print(s, e)
import random
'''temp = list(s[0])
temp[-1] = str(s[1][-1])
s[0] = ''.join(temp)
temp = list(s[0])
temp[-1] = str(s[1][-1])
s[0] = ''.join(temp)
print(s, e)'''
'''a = []
[a.append(str(i)) for i in s]
#print(a, s)
#print(1)
for i in range(4):
    for j in range(4):
        if i == j: break
        temp = list(s[i])
        temp[-1] = str(s[j][-1])
        temp2 = list(s[j])
        temp2[-1] = str(s[i][-1])
        a[i] = ''.join(temp)
        a[j] = ''.join(temp2)
        print(s)
        a = []
        [a.append(str(i)) for i in s]'''
'''def f(s, e, count=0):
    print(s, e)
    if s == e:
        return count
    else:
        a = []
        b = []
        [a.append(str(i)) for i in s]
        for i in range(4):
            for j in range(4):
                if i == j: break
                temp = list(s[0])
                temp[-1] = str(s[1][-1])
                temp2 = list(s[1])
                temp2[-1] = str(s[0][-1])
                a[0] = ''.join(temp)
                a[1] = ''.join(temp2)
                for k in range(len(a)):
                    if len(a[k]) >=1 and a[k][-1] == '0':
                        a[k] = a[k][:-1]
                b.append(a)
        #print(b)
        return f(b[0], e, count+1)
        return f(b[1], e, count + 1)
        return f(b[2], e, count + 1)
        return f(b[3], e, count + 1)
        return f(b[4], e, count + 1)
        return f(b[5], e, count + 1)

f(s, e)
print(count)'''

s = input().split(" ")
e = input().split(" ")
s1, e1, = [0,0,0,0], [0,0,0,0]
for i in range(len(s)):
    try:
        a = s[i].index("1")
        s1[0]=i+1
    except:
        pass
    try:
        a = s[i].index("2")
        s1[1] = i + 1
    except:
        pass
    try:
        a = s[i].index("3")
        s1[2] = i + 1
    except:
        pass
    try:
        a = s[i].index("4")
        s1[3] = i + 1
    except:
        pass
for i in range(len(e)):
    try:
        a = e[i].index("1")
        e1[0] = i + 1
    except:
        pass
    try:
        a = e[i].index("2")
        e1[1] = i + 1
    except:
        pass
    try:
        a = e[i].index("3")
        e1[2] = i + 1
    except:
        pass
    try:
        a = e[i].index("4")
        e1[3] = i + 1
    except:
        pass
#print(s1, e1)
a = 0
for i in range(4):
    if s1[i] != e1[i]:
        a+=1
print(a+random.randint(0,3))