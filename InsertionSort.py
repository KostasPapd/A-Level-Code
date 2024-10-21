import random, time

def insert(a):
    n = len(a)
    if n <= 1:
        return
    for i in range(1, n):
        key = a[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

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
insert(arr)
b = time.time()

print("Sorted array is:")
print(arr)
t = b-a
t = t.__round__(3)
print("Time taken for sort:", t, "seconds")
