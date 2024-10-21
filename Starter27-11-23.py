n = ["Abid", "Barry", "Saad", "Sally", "Jonathon", "Jon", "Isabel", "Lewis", "Kostas", "Ali", "Stefan"]

print(n[:10])

name = input("Enter the name you want to search: ")
if name in n:
    print("Found")
else:
    print("Not found")

for i in range(0, len(n)):
    name = n[i]
    if name[0] == "S" or name[0] == "s":
        print(name)

num = [[2, 4, 7],
       [5, 9, 3],
       [6, 2, 1]]

largest = num[0][0]
for r in range(0, 3):
    for c in range(0, 3):
        if num[r][c] > largest:
            largest = num[r][c]
print(largest)