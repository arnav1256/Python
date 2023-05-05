def d1q1():
    g = [*open("amogus.txt", "r").readlines()]; print(sum(int(g[i]) < int(g[i + 1]) for i in range(len(g) - 1)))
def d1q2():
    g = [*open("amogus.txt", "r").readlines()]; print(sum(int(g[i]) < int(g[i + 3]) for i in range(len(g) - 3)))
def d2q1():
    depth = 0; a = 0; g = list(map(str.split, [*open("amogus.txt", "r").readlines()]))
    for i in range(len(g)):
        if g[i][0] == 'forward': a += int(g[i][1])
        elif g[i][0] == 'down': depth += int(g[i][1])
        else: depth -= int(g[i][1])
    print(depth*a)
def d2q2():
    aim = 0; a = 0; depth = 0; g = list(map(str.split, [*open("amogus.txt", "r").readlines()]))
    for i in range(len(g)):
        if g[i][0] == 'forward': a += int(g[i][1]); depth += aim * int(g[i][1])
        elif g[i][0] == 'down': aim += int(g[i][1])
        else: aim -= int(g[i][1])
    print(depth*a)
def d3q1():
    gamma = ''; epsilon = ''; g = [*open('amogus.txt', 'r').readlines()]
    for i in range (12):
        zero = 0; one = 0
        for j in range(len(g)):
            if g[j][i] == '0': zero += 1
            else: one += 1
        if zero < one:
            gamma += '1'; epsilon += '0'
        else:
            gamma += '0'; epsilon += '1'
    print(int(gamma, 2)*int(epsilon, 2))
def d3q2():
    g = list(map(str.strip, [*open("amogus.txt", "r").readlines()])); f = list(map(str.strip, [*open("amogus.txt", "r").readlines()]))
    for i in range(12):
        zero = 0; one = 0
        for j in range(len(g)):
            if g[j][i] == '0': zero += 1
            else: one += 1
        if (zero < one) or (zero == one):
            for k in range(zero):
                for j in g:
                    if j[i] == '0': g.remove(j)
            if len(g) == 1: break
        elif one < zero:
            for k in range(one):
                for j in g:
                    if j[i] == '1': g.remove(j)
            if len(g) == 1: break
    for i in range(12):
        zero = 0; one = 0
        for j in range(len(f)):
            if f[j][i] == '0': zero += 1
            else: one += 1
        if (zero < one) or (zero == one):
            for k in range(one):
                for j in f:
                    if j[i] == '1': f.remove(j)
            if len(f) == 1: break
        elif one < zero:
            for k in range(zero):
                for j in f:
                    if j[i] == '0': f.remove(j)
            if len(f) == 1: break
    print(int(g[0], 2)*int(f[0], 2))
def d6q1():
    g = [int(x) for x in open("amogus.txt", "r").readline().split(',')]; dict = {0: g.count(0),1: g.count(1),2: g.count(2),3: g.count(3),4: g.count(4),5: g.count(5),6: g.count(6),7: g.count(7),8: g.count(8)}
    for i in range(80): k = dict[0]; dict[6], dict[0], dict[1], dict[2], dict[3], dict[4], dict[5] = dict[0], dict[1], dict[2], dict[3], dict[4], dict[5], dict[6]; dict[6] += dict[7]; dict[7] = dict[8]; dict[8] = k
    print(dict[0] + dict[1] + dict[2] + dict[3] + dict[4] + dict[5] + dict[6] + dict[7] + dict[8])
def d6q2():
    g = [int(x) for x in open("amogus.txt", "r").readline().split(',')]; dict = {0: g.count(0),1: g.count(1),2: g.count(2),3: g.count(3),4: g.count(4),5: g.count(5),6: g.count(6),7: g.count(7),8: g.count(8)}
    for i in range(256): k = dict[0]; dict[6], dict[0], dict[1], dict[2], dict[3], dict[4], dict[5] = dict[0], dict[1], dict[2], dict[3], dict[4], dict[5], dict[6]; dict[6] += dict[7]; dict[7] = dict[8]; dict[8] = k
    print(dict[0] + dict[1] + dict[2] + dict[3] + dict[4] + dict[5] + dict[6] + dict[7] + dict[8])
def d7q1():
    g = sorted([int(x) for x in open("amogus.txt", "r").readline().split(',')]); total = 0
    for i in g:
        total += abs(g[len(g) // 2] - i)
    print(total)
def d7q2():
    g = sorted([int(x) for x in open("amogus.txt", "r").readline().split(',')])
    a = []
    for i in range(1, 2000):
        temp = 0
        for j in g:
            temp += abs(j-i)*(abs(j-i)+1)/2
        a.append(temp)
    print(min(a))
def d9q1():
    g = [[int(k) for k in j] for j in [list(i) for i in list(map(str.strip, [*open("amogus.txt", "r").readlines()]))]]; tot = 0
    for i in range(len(g)):
        for j in range(100):
            if g[i][j] == 9: continue
            elif i == 0 and j == 0:
                if (g[i][j] < g[i][j + 1]) and (g[i][j] < g[i + 1][j]) and (g[i][j] < g[i + 1][j + 1]): tot += 1 + g[i][j]
            elif i == 0 and 0 < j < 99:
                if (g[i][j] < g[i][j - 1]) and (g[i][j] < g[i][j + 1]) and (g[i][j] < g[i + 1][j - 1]) and (g[i][j] < g[i + 1][j]) and (g[i][j] < g[i + 1][j + 1]): tot += 1 + g[i][j]
            elif i == 0 and j == 99:
                if (g[i][j] < g[i][j - 1]) and (g[i][j] < g[i + 1][j - 1]) and (g[i][j] < g[i + 1][j]): tot += 1 + g[i][j]
            elif 0 < i < 99 and j == 0:
                if (g[i][j] < g[i - 1][j]) and (g[i][j] < g[i - 1][j + 1]) and (g[i][j] < g[i][j + 1]) and (g[i][j] < g[i + 1][j]) and (g[i][j] < g[i + 1][j + 1]): tot += 1 + g[i][j]
            elif 0 < i < 99 and 0 < j < 99:
                if (g[i][j] < g[i - 1][j - 1]) and (g[i][j] < g[i - 1][j]) and (g[i][j] < g[i - 1][j + 1]) and (g[i][j] < g[i][j - 1]) and (g[i][j] < g[i][j + 1]) and (g[i][j] < g[i + 1][j - 1]) and (g[i][j] < g[i + 1][j]) and (g[i][j] < g[i + 1][j + 1]): tot += 1 + g[i][j]
            elif 0 < i < 99 and j == 99:
                if (g[i][j] < g[i - 1][j - 1]) and (g[i][j] < g[i - 1][j]) and (g[i][j] < g[i][j - 1]) and (g[i][j] < g[i + 1][j - 1]) and (g[i][j] < g[i + 1][j]): tot += 1 + g[i][j]
            elif i == 99 and j == 0:
                if (g[i][j] < g[i - 1][j]) and (g[i][j] < g[i - 1][j + 1]) and (g[i][j] < g[i][j + 1]): tot += 1 + g[i][j]
            elif i == 99 and 0 < j < 99:
                if (g[i][j] < g[i - 1][j - 1]) and (g[i][j] < g[i - 1][j]) and (g[i][j] < g[i - 1][j + 1]) and (g[i][j] < g[i][j - 1]) and (g[i][j] < g[i][j + 1]): tot += 1 + g[i][j]
            elif i == 99 and j == 99:
                if (g[i][j] < g[i - 1][j - 1]) and (g[i][j] < g[i - 1][j]) and (g[i][j] < g[i][j - 1]): tot += 1 + g[i][j]
    print(tot)