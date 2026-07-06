# 16. Find and display all the leaf nodes of a binary tree.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def leafNodes(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.data)
    leafNodes(root.left)
    leafNodes(root.right)

root = Node(50)
root.left = Node(30)
root.right = Node(70)

leafNodes(root)