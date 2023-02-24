class Node:
    def __init__(self,data) -> None:
        self.data = data


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.empty():
            return self.stack[-1]
        else:
            return None

    def empty(self):
        return len(self.stack) == 0

# String Reverse
def revstr(string):
    stack = []
    for s in string:
        stack.append(s)
    revrse =""
    while stack:
        revrse = revrse+stack.pop()
    return revrse
strr ="NITHIN"

print(revstr(strr))


# Queue Using Stack

class MyQueue:

    def __init__(self):
        self.stack_a = []
        self.stack_b = []

    def push(self, x: int) -> None:
        self.stack_a.append(x)

    def pop(self) -> int:
        if not self.stack_b:
            while self.stack_a:
                self.stack_b.append(self.stack_a.pop())
        return self.stack_b.pop()

    def peek(self) -> int:
        if not self.stack_b:
            while self.stack_a:
                self.stack_b.append(self.stack_a.pop())
        return self.stack_b[-1]

    def empty(self) -> bool:
        return not self.stack_a and not self.stack_b

