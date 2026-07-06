# 10. Remove one element from the front of the queue and display the updated queue.

class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            self.queue.pop(0)

    def display(self):
        for i in self.queue:
            print(i)

q = Queue()

q.insert(10)
q.insert(20)
q.insert(30)
q.insert(40)

q.delete()
q.display()