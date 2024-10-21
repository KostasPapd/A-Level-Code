import time
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

def f(n):
    first = 0
    second = 1
    third = 1
    for i in range(0, n-1):
        third = first + second
        first = second
        second = third
    return third

def fR(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fR(n-1)+fR(n-2)

runtime = []
runtime1 = []
n =[]
num = int(input("Enter largest term: "))
step = int(input("Enter step: "))
for i in range(0, num, step):
    start1 = time.time()
    f(i)
    end1 = time.time()
    timediff1 = round(end1-start1, 4)
    runtime1.append(timediff1)

    start = time.time()
    fR(i)
    end = time.time()
    timediff = round(end-start, 4)
    runtime.append(timediff)
    n.append(i)

print("Recursive:", runtime)
print("Iterative:", runtime1)
print("n:", n)

plt.plot(n, runtime)
plt.title("Recursion Graph")
plt.ylabel("Recursion Time (s)")
plt.xlabel("Values of n")
plt.show()
