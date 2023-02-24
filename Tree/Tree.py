class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_product_tree():
    root = TreeNode("Electronict")
    laptop = TreeNode("Laptop")

    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("HP"))
    # print(laptop.children)