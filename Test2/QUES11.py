# 11. Display the front element of the queue without removing it.

class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, data):
        self.queue.append(data)

    def frontElement(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print(self.queue[0])

    def display(self):
        for i in self.queue:
            print(i)

q = Queue()

q.insert(10)
q.insert(20)
q.insert(30)
q.insert(40)

q.frontElement()