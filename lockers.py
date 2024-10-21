# 0 = open, 1 = closed
lockers = [0] * 1000

step = 1
for i in range(0, 1000, 1):
    lockers[i] = 0

while step < 1001:
    for i in range(0, 1000, step):
        if lockers[i] == 1:
            lockers[i] = 0
        else:
            lockers[i] = 1
    step = step + 1

total = 0
for i in range(0, 1000):
    if lockers[i] == 1:
        total = total + lockers[i]

print("Total number of lockers closed: ", str(total))
