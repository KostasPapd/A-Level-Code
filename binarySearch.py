a = [4, 7, 12, 45, 65, 78, 93, 100]

def search(n, a):
    global m
    found = False
    l = 0
    h = len(a)
    m = (l + h)//2
    while found == False and h >= 0 and l<=(len(a)):
        if n >= a[m]:
            if n == a[m]:
                found = True
            else:
                l = m+1
                m = (l + h)//2
        elif n <= a[m]:
            if n == a[m]:
                found = True
            else:
                h = m - 1
                m = (l + h) // 2

    if found == True:
        c = 0
        for i in range(0, (len(a)-1)):
            if a[i] == n:
                return c
            else:
                c += 1
    else:
        return -1

n = int(input("Enter the element you want to search for: "))
f = search(n, a)

if f == -1:
    print("Not found")
else:
    print("Found at index", f)
