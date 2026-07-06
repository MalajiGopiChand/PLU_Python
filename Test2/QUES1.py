# 1.Create a linked list containing the values 10, 20, 30, 40, 50 and display all the elements.
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertStart(self, data):
        node = Node(data)
        self.head = node
        node.ref = None
        return node
    def insertMiddle(self, data, prev):
        node = Node(data)
        prev.ref = node
        node.ref = None
        return node
    def insertLast(self, data):
        node = Node(data)
        current = self.head

        while current.ref:
            current = current.ref
        current.ref = node
        return node
    
    def printList(self):
        current = self.head
        
        while current:
            print(current.data)
            current = current.ref
        
    
Link = LinkedList()

node1 = Link.insertStart(10)
node2 = Link.insertMiddle(20, node1)
node3 = Link.insertMiddle(30, node2)
node4 = Link.insertMiddle(40, node3)
node5 = Link.insertLast(50)

Link.printList()

