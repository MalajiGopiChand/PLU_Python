# Display the top element of the stack without removing it.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def topElement(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print(self.stack[-1])

    def display(self):
        for i in reversed(self.stack):
            print(i)

s = Stack()

s.push(5)
s.push(10)
s.push(15)
s.push(20)

s.topElement()