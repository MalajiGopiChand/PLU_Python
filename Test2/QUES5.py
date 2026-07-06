# Create an empty stack and push the values 5, 10, 15, 20 into it.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def display(self):
        for i in reversed(self.stack):
            print(i)

s = Stack()

s.push(5)
s.push(10)
s.push(15)
s.push(20)

print("Stack elements are:")
s.display()