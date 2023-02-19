class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def EnQueue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def DeQueue(self):

        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None


class queue:

    def __init__(self):
        self.front = self.rear = None

    def enqueue(self,data):

        node = Node(data)

        if self.rear is None:
            self.rear.next = node

            return
        self.front = node
        self.rear = node

    def deque(self):

        if self.front is None:
            return None
        else:
            popped = self.front
            self.front = self.front.next

            return popped.data