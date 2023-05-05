dict = {1: [2, 3],
        2: [1, 5, 8, 6],
        3: [4, 1],
        4: [3, 6, 9],
        5: [2],
        6: [4, 7, 2],
        7: [6, 8],
        8: [2, 9, 7],
        9: [4, 8]}
matrix = [
            [0,1,0,0],
            [1,0,1,1],
            [0,1,0,1],
            [0,1,1,0]
         ]
def DFS(graph, start):
    s = [start]
    v = [start]
    while len(s) >0:
        vx = s[-1]
        s = s[:-1]
        print(vx)
        for i in graph[vx]:
            if i not in v:
                s.append(i)
                v.append(i)
def BFS(graph, start):
    s = [start]
    v = [start]
    while len(s) >0:
        vx = s[0]
        s = s[1:]
        print(vx)
        for i in graph[vx]:
            if i not in v:
                s.append(i)
                v.append(i)
def dictionary(matrix):
    d = {}
    c = 1; r = 1
    for i in range(1, len(matrix)+1):
        d[i] = []
    for i in matrix:
        for j in i:
            if j == 1:
                if r not in d[c]:
                    d[c].append(r)
                    d[r].append(c)
            c +=1
        r+=1
        c=1
    print(d)