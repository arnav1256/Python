import random, time
l_list = [random.randint(0,1000) for i in range(995)]
b_list = sorted(l_list)
def linear(n, l):
    for i in range(len(l)):
        if l[i] == n:
            return i
    return -1
def linear_recursive(n, l, count = 0):
    if len(l) == 0:
        return -1
    elif l[0] == n:
        return count
    else:
        return linear_recursive(n, l[1:], count + 1)
def binary(n, l):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == n:
            return mid
        elif l[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    return -1
def binary_recursive(n, l, low, high):
    if high >= low:
        mid = (low + high) // 2
        if l[mid] == n:
            return mid
        elif l[mid] < n:
            return binary_recursive(n, l, mid+1, high)
        else:
            return binary_recursive(n, l, low, mid-1)
    else:
        return -1
def test():
    #binary search times
    #print(b_list)
    t1 = time.perf_counter_ns()
    binary_recursive(50, b_list, 0, len(b_list))
    t2 = time.perf_counter_ns()
    a = t2 - t1
    #print("binary recursive:", a)
    t1 = time.perf_counter_ns()
    binary(50, b_list)
    t2 = time.perf_counter_ns()
    b = t2 - t1
    #print("binary iterative:", b)

    #linear search times
    #print(l_list)
    t1 = time.perf_counter_ns()
    linear(50, l_list)
    t2 = time.perf_counter_ns()
    c = t2 - t1
    #print("linear iterative:",c)
    t1 = time.perf_counter_ns()
    linear_recursive(50, l_list)
    t2 = time.perf_counter_ns()
    d = t2 - t1
    #print("linear recursive:",d)
    return a,b,c,d

coords = [test() for j in range(2000)]
from matplotlib import pyplot as plt
plt.ylim(0,2*10**6)
plt.plot([i for i in range(len(coords))], [i[0] for i in coords], label="Binary Recursive", linewidth=0.5)
plt.plot([i for i in range(len(coords))], [i[1] for i in coords], label="Binary Iterative", linewidth=0.5)
plt.plot([i for i in range(len(coords))], [i[2] for i in coords], label="Linear Recursive", linewidth=0.5)
plt.plot([i for i in range(len(coords))], [i[3] for i in coords], label="Linear Iterative", linewidth=0.5)
plt.legend(loc='best')
plt.ylabel('Time (ns)')
plt.xlabel('Trial')
plt.show()