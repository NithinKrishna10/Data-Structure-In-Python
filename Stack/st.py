from collections import deque


class Queue:

    def __init__(self):
        self.queue = list()
        self.queue2 = list()

    def enqueue(self, val):
        # Insert method to add element
        if val not in self.queue2:
            self.queue.insert(0, val)
            return True
        return False

    # Pop method to remove element
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("Queue is Empty")

    def push(self, data):
        self.queue.insert(0, data)
        print(self.queue)

    def pop(self):
        while self.queue:
            self.queue2.append(self.dequeue())
        return self.queue2.pop(0)


que = Queue()

que.push(10)
que.push(20)
print(que.pop())
