l = ["a", "b", "c", "d"]

def search(n, l):
    for i in range(0, len(l)):
        if n == l[i]:
            return True
    return False

n = input("Enter element you want to find: ")
print(search(n, l))
