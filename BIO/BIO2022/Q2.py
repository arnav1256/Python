redhive = [[1,1]]
bluehive = [[25,6]]
redfacing = [1,1]
bluefacing = [25,6]
[r,b] = [int(x) for x in input().split(' ')]
[s,f] = [int(x) for x in input().split(' ')]
def skirmish(redhive,bluehive,redfacing,bluefacing):
    redfacing[0]+=r
    bluefacing[0]+=b
    if redfacing[0]>25:redfacing[0]-=25
    if bluefacing[0] > 25: bluefacing[0] -= 25
    redfacing[1]+=1
    bluefacing[1]-=1
    if redfacing[1]>6:redfacing[1]-=6
    if bluefacing[1] < 1: bluefacing[1] += 6
    redhive+=[redfacing]
    bluehive+=[bluefacing]
    print(redhive,bluehive,redfacing,bluefacing)
    return redhive,bluehive,redfacing,bluefacing
for i in range(s-1):
    redhive,bluehive,redfacing,bluefacing = skirmish(redhive,bluehive,redfacing,bluefacing)
red,blue = 0,0
for j in range(25):
    for i in redhive:
        for k in bluehive:
            a,b = 0,0
            if i[0] == j: a+=1
            if k[0] == j: b+=1
    if a>b:red+=1
    if a < b: blue += 1
print(red)
print(blue)

