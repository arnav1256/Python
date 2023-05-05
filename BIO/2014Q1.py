import time
inp = int(input())
time1 = time.time()
oddnums = [2*i+1 for i in range(inp)]
luckynums = []
for j in oddnums:
    luckynums.append(j)
    if j != 1:
        del oddnums[j-1::j]
print(max([i for i in luckynums if inp>i]),min([i for i in luckynums if inp<i]))#1a
print(len(luckynums))#1b when 50 is input
time2 = time.time()
print(time2-time1)
#1c) 999,999,999*2 = 1999999998
#30/30 with google for lines 11 and 12
