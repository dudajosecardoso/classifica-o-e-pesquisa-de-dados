class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def insertionSort(self):
        current = self.head
        while current:
            next_node = current.next
            while next_node:
                if current.data > next_node.data:
                    temp = current.data
                    current.data = next_node.data
                    next_node.data = temp
                next_node = next_node.next
            current = current.next

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


llist = LinkedList()
llist.append(12)
llist.append(11)
llist.append(13)
llist.append(5)
llist.append(6)
llist.append(6)

print("Lista original:")
llist.printList()

llist.insertionSort()

print("Lista ordenada:")
llist.printList()
