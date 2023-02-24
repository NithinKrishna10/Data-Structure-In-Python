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



# Stack Using Queue


class QtoSt:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self,x):
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.pop(0))

        self.q1,self.q2 = self.q2,self.q1

    def pop(self):
        if self.q1:
            return self.q1.pop(0)
        return None

if __name__ == '__main__':
    que = Queue()
    que.enqueue("January")
    que.enqueue("February")
    que.enqueue("March")
    que.enqueue("April")
    print(que.dequeue())

    qs = QtoSt()
    qs.push(20)
    qs.push(40)
    print(qs.pop())
