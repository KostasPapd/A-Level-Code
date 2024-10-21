def fact(n):
    if n == 0 or n == 1:
        factorial = 1
    else:
        factorial = n * fact(n-1)
    return factorial

n = int(input("Enter number: "))
print(fact(n))
