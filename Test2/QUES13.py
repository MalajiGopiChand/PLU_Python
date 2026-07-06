# 13. Create the binary tree: 50 two child 30 and 70. Display the root node, left child and right child of the root node.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(50)
root.left = Node(30)
root.right = Node(70)

print(root.data)
print(root.left.data)
print(root.right.data)