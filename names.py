def namesList():
    first = ["Abid", "James", "Ed", "Walter"]
    last = ["Issa", "Johnson", "Jones", "White"]
    full = []

    for i in range(0, len(first)):
        name = first[i] + " " + last[i]
        full.append(name)

    return full

print(namesList())
