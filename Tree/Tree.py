


class Tree:
    def __init__(self, data):
        self.children = []
        self.data = data

left = Tree("left")
middle = Tree("middle")
right = Tree("right")
root = Tree("root")
root.children = [left, middle, right]
