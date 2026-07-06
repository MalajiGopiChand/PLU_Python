# 4. Count and display the total number of nodes in the linked list.

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

    def inserMiddle(self, data, prev):
        node = Node(data)
        node.ref = prev.ref
        prev.ref = node
        return node

    def insertLast(self, data):
        node = Node(data)
        current = self.head
        while current.ref:
            current = current.ref
        current.ref = node
        return node

    def countNodes(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.ref
        return count

    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.ref

Link = LinkedList()

node1 = Link.insertStart(10)
node2 = Link.inserMiddle(20, node1)
node3 = Link.inserMiddle(25, node2)
node4 = Link.inserMiddle(30, node3)

print("Total nodes:", Link.countNodes())
Link.printList()