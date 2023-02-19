class Queue:

    def __init__(self):
        self.queue = list()

    def enqueue(self, val):
        # Insert method to add element
        if val not in self.queue:
            self.queue.insert(0, val)
            return True
        return False

    # Pop method to remove element
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("Queue is Empty")


if __name__ == '__main__':
    que = Queue()
    que.enqueue("January")
    que.enqueue("February")
    que.enqueue("March")
    que.enqueue("April")
    print(que.dequeue())
