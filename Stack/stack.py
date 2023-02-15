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
