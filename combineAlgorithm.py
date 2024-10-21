l1 = [1, 4, 16, 146, 2000, 1214312]
l2 = [3, 9, 57, 201, 12121]

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
    if p1 == x:
        result.append(l2[p2:])
    else:
        result.append(l1[p1:])

    return result


print("Combined list: ", combine(l1, l2))
