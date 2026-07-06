# Pop one element from the stack and display the updated stack.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def popElement(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            self.stack.pop()

    def display(self):
        for i in reversed(self.stack):
            print(i)

s = Stack()

s.push(5)
s.push(10)
s.push(15)
s.push(20)


s.popElement()
s.display()