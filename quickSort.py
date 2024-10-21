import random
import time


def makeList():
    list = []
    n = int(input("How many numbers do you want in the array? "))
    for i in range(0, n):
        num = random.randint(0, (n*100))
        list.append(num)
    return list


def part(list, low_mark, high_mark):
    pivot = list[high_mark]
    i = low_mark-1
    for j in range(low_mark, high_mark):
        if list[j] <= pivot:
            i += 1
            (list[i], list[j]) = (list[j], list[i])
    (list[i + 1], list[high_mark]) = (list[high_mark], list[i + 1])
    return i+1


def sort(list, low_mark, high_mark):
    if low_mark < high_mark:
        p = part(list, low_mark, high_mark)
        sort(list, low_mark, (p-1))
        sort(list, (p+1), high_mark)
    return list


list = makeList()
print("Unsorted array:")
print(list)
print("Sorted array:")
s = len(list)
b = time.time()
a = sort(list, 0, (s-1))
c = time.time()
print(a)
t = c-b
t = t.__round__(3)
print("Time for sort:", t, "seconds")
