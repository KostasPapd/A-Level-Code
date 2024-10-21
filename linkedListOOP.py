class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def main():
    global head

    node1 = Node("Apple")
    head = node1
    node2 = Node("Orange")
    node3 = Node("Pear")

    node1.next = node2
    node2.next = node3

def printList():
    node = head
    print()
    while node != None:
        print(node.data)
        node = node.next

def insert(data, location):
    node = head
    while node != None:
        if node.data == location:
            newnode = Node(data)
            newnode.next = node.next
            node.next = newnode
        node = node.next

def deleteData(head, data):
    current = head
    prev = None
    found = False
    while not found:
        if current.data == data:
            found = True
        else:
            prev = current
            current = current.next
    if prev == None:
        head = current.next
    else:
        prev.next = current.next

    return head

main()
insert("Potato", "Apple")
insert("Raspberry", "Orange")
printList()
