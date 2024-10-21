import random
import time

def sort(a):
    if len(a) <= 1:
        return a
    l = a[0:len(a)//2]
    r = a[len(a) // 2:]
    l1 = sort(l)
    l2 = sort(r)

    sorted = combine(l1, l2)
    return sorted

def combine(l1, l2):
    result = []
    x = len(l1)
    y = len(l2)
    p1 = 0
    p2 = 0
    while p1 < x and p2 < y:
        if l1[p1] <= l2[p2]:
            result.append(l1[p1])
            p1 += 1
        elif l2[p2] < l1[p1]:
            result.append(l2[p2])
            p2 += 1
    result = result + l1[p1:] + l2[p2:]
    return result


def makeList():
    list = []
    n = int(input("How many numbers do you want in the array? "))
    for i in range(0, n):
        num = random.randint(0, (n*100))
        list.append(num)
    return list


x = makeList()
print("Unsorted array:")
print(x)
print("Sorted array:")
b = time.time()
s = sort(x)
c = time.time()
print(s)
t = c-b
t = t.__round__(3)
print("Time taken for sort:", t)
