rank = [["", -1],
        ["", -1],
        ["", -1],
        ["", -1],
        ["", -1],
        ["", -1],
        ["", -1],
        ["", -1],
        ["", -1],
        ["", -1]]

head = 0
free = 0

def add(reg, rank):
        global free
        rank[free][0] = reg
        if free != 0:
                rank[free - 1][1] = free
        free += 1
        print(rank)
        print("")

def remove():
        global free, head
        carReg = rank[head][0]
        print("Removing:", carReg)
        rank[head][1] = -1
        rank[head][0] = ""
        head += 1
        print(rank)
        print("")

def main(rank, head):
        print("1. Add taxi\n"
              "2. Remove taxi")
        choice = int(input("Enter your choice: "))
        if choice == 1:
                reg = input("Enter the registration number: ")
                add(reg, rank)
        elif choice == 2:
                print(rank)
                remove()
        main(rank, head)


main(rank, head)