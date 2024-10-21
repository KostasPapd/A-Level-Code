# Kostas
# 06/12/2023
queue = ["", "", "", "", ""]
tail = 0
head = 0

def IsEmpty():
    global tail, head, queue
    if head == tail:
        return True
    else:
        return False

def IsFull():
    global tail, head, queue
    if head == 0 and tail == len(queue) - 1:
        return True
    else:
        if head == tail + 1:
            return True
        else:
            return False

def pop():
    global head, queue
    if IsEmpty() == True:
        print("Queue is empty")
        print(queue)
        print()
    else:
        e = queue[head]
        queue[head] = ""
        head += 1
        if head == 5:
            head = 0
        print(queue)
        print()
        return e

def push(element):
    global tail, queue
    if IsFull() == True:
        print("Queue is full")
    else:
        queue[tail] = element
        tail += 1
        if tail == 5:
            tail = 0
    print(queue)
    print()

def status():
    if IsFull() == True:
        return "Full"
    elif IsEmpty() == True:
        return "Empty"
    else:
        return "In Use"

def main():
    Continue = True
    while Continue == True:
        choice = input("Do you want to 1. PUSH or 2. POP? ")
        while choice != "1" and choice != "2":
            print("Invalid choice")
            choice = input("Do you want to 1. PUSH or 2. POP? ")
        if choice == "1":
            element = input("Enter the element: ")
            push(element)
        elif choice == "2":
            print("Head pointer: ", pop())
        again = input("Do you want to continue (y, n)? ")
        if again == "y":
            print("Continuing")
        else:
            Continue = False
        print("The current list status is:", status())


if __name__ == "__main__":
    main()
