def counter(n):
    return [i+1 for i in range(n)]
def Rcounter(n, li=[]):
    if n == 0: return li[::-1]
    else: return Rcounter(n-1,li+[n])


def x2y(x,y):
    return [i for i in range(x,y+1)]
def Rx2y(x,y,li=[]):
    if x > y: return li
    else: return Rx2y(x+1,y,li+[x])

def squarelist(li):
    if len(li) == 1: return [li[0]**2]
    else: return squarelist(li[:1]) + squarelist(li[1:])

print(squarelist([1,2,3,4,5]))