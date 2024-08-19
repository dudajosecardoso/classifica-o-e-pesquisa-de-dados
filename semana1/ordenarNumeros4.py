class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def selectionSort(self):
        current = self.head
        while current:
            menor = current
            menor_id = current
            next_node = current.next
            while next_node:
                if next_node.value < menor.value:
                    menor = next_node
                    menor_id = next_node
                next_node = next_node.next
            if menor_id != current:
                temp = current.value
                current.value = menor_id.value
                menor_id.value = temp
            current = current.next

    def printList(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

lista = LinkedList()
lista.append(64)
lista.append(34)
lista.append(25)
lista.append(12)
lista.append(22)
lista.append(11)
lista.append(90)

print("Lista desordenada:")
lista.printList()

lista.selectionSort()

print("Lista ordenada:")
lista.printList()
