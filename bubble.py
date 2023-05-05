import random
list = [random.randint(1, 10) for i in range(10)]
#list = [4,5,7,2,6,8,9,1,3,10]
def bubble(list):
    sorted = True
    while sorted == True:
        sorted = False
        for i in range(len(list)):
            for j in range(len(list)-i-1):
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]

def insertion(list):
    for i in range(1, len(list)):
        for j in range(i):
            if list[i-j-1] > list[i-j]:
                print(list)
                list[i-j-1], list[i-j] = list[i-j], list[i-j-1]
def merge(list):
    if len(list) > 1:
        left, right = list[:len(list)//2], list[len(list)//2:]
        merge(left)
        merge(right)
        i,j,k = 0,0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
def quick(list):
    if len(list) > 1:
        pivot = list[0]
        left, right = [], []
        for i in range(1, len(list)):
            if list[i] < pivot:
                left.append(list[i])
            else:
                right.append(list[i])
        quick(left)
        quick(right)
        list[:] = left + [pivot] + right
def selection(list):
    for i in range(len(list)):
        min = i
        for j in range(i, len(list)):
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]
def heap(list):
    for i in range(len(list)//2-1, len(list)):
        heapify(list, i, len(list))
    for i in range(0, len(list)-1):
        list[i], list[0] = list[0], list[i]
        heapify(list, 0, i)
def heapify(list, i, n):
    left = len(list) - (2*i+1)
    right = len(list)-(2*i+2)
    print(left, right)
    largest = i
    if left < n and list[left] > list[largest]:
        largest = left
    if right < n and list[right] > list[largest]:
        largest = right
    if largest != i:
        list[i], list[largest] = list[largest], list[i]
        heapify(list, largest, n)
print(list)
heap(list)
print(list)












'''
# Python3 program for implementation
# of Heap Sort

# To heapify a subtree rooted with
# node i which is an index in arr[].
# n is size of heap
def heapify(arr, n, i):
    smallest = i # Initialize smalles as root
    l = 2 * i + 1 # left = 2*i + 1
    r = 2 * i + 2
    if l < n and arr[l] < arr[smallest]: smallest = l
# If right child is smaller than # smallest so far
    if r < n and arr[r] < arr[smallest]: smallest = r
    # If smallest is not root
    if smallest != i: (arr[i], arr[smallest]) = (arr[smallest], arr[i])
    # Recursively heapify the affected # sub-tree
    heapify(arr, n, smallest)
    # main function to do heap sort
def heapSort(arr, n): # Build heap (rearrange array)
    for i in range(int(n / 2) - 1, -1, -1): heapify(arr, n, i)
    # One by one extract an element # from heap
    for i in range(n-1, -1, -1): # Move current root to end #
        arr[0], arr[i] = arr[i], arr[0] # call max heapify on the reduced heap
        heapify(arr, i, 0)
# A utility function to print # array of size n
def printArray(arr, n):
    for i in range(n):
        print(arr[i], end = " ")
        print()
# Driver Code
if __name__ == '__main__':
    arr = [4, 6, 3, 2, 9]
    n = len(arr)
    heapSort(arr, n)
    print("Sorted array is ")
    printArray(arr, n)'''