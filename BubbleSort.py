import random, time

def bubbleSort(arr):
    global s, c
    s = 0
    c = 0
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                s += 1
            c += 1
        if not swapped:
            return

def makeList():
    list = []
    n = int(input("How many numbers do you want in the array? "))
    for i in range(0, n):
        num = random.randint(0, (n*100))
        list.append(num)
    return list

arr = makeList()
print("Unsorted array:")
print(arr)
a = time.time()
bubbleSort(arr)
b = time.time()

print("Sorted array is:")
print(arr)
t = b-a
t = t.__round__(3)
print("Time taken for sort:", t, "seconds")
print("Number of swaps:", s)
print("Number of comparisons:", c)
