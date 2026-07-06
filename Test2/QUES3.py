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
# Delete node function logic added to delete a node containing a specific value from the linked list.   
    def deleteNode(self, data):
        current = self.head

        if current.data == data:
            self.head = current.ref
            return
        
        while current.ref:
            if current.ref.data == data:
                current.ref = current.ref.ref
                return
            current = current.ref
    
    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.ref
   
    
Link = LinkedList()

node1 = Link.insertStart(10)
node2 = Link.insertMiddle(20, node1)
node3 = Link.insertMiddle(25, node2)
node4 = Link.insertMiddle(30, node3)
node5 = Link.insertMiddle(40, node4)
node6 = Link.insertLast(50)

Link.deleteNode(25)

Link.printList()