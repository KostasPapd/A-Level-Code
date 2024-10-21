names = ["", "", "", "", ""]
stackPointer = 0
maxLength = len(names)

def push(element):
    global stackPointer, maxLength, names
    full = isFull()
    if full == True:
        print("Stack full")
    else:
        names[stackPointer] = element
        stackPointer += 1
    print("Stackpointer:", stackPointer)
    print(names)
    print("")

def pop():
    global stackPointer, maxLength, names
    empty = isEmpty()
    if empty == True:
        print("Stack empty")
    else:
        stackPointer -= 1
    print("Stackpointer:", stackPointer)
    print(names)
    print("")

def isEmpty():
    global stackPointer, maxLength, names
    if stackPointer == 0:
        return True
    else:
        return False

def isFull():
    global stackPointer, maxLength, names
    if stackPointer >= 5:
        return True
    else:
        return False

def main():
    Push = input("Push element? ")
    while Push == "y":
        element = input("Enter an element: ")
        push(element)
        Push = input("Push element? ")
    Pop = input("Pop element? ")
    while Pop == "y":
        pop()
        Pop = input("Pop element? ")
    print("Stackpointer:", stackPointer)
    print(names)
    print("")

main()
