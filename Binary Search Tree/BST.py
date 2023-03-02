class BST:

    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    #  Insertion In Binary Search Tree
    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    # Search in Binary Search Tree
    def search(self, data):
        if self.key is None:
            return

        if self.key == data:
            print("Node is Found!", self.key)
            x = self.key
            return x
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in tree")
                return
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in tree")
                return
    def ins(self,s):

        if self.key == s:
            return

        if self.key < s:
            if self.lchild:
                self.lchild.ins(s)
            self.lchild = BST(s)
        else:
            if self.rchild:
                self.rchild.ins(s)
            self.rchild = BST(s)
    # Pre-Order Traversal In Binary Search Tree
    def preorder(self):
        if self.key is None:
            return
        else:
            print(self.key, end=" ")
            if self.lchild:
                self.lchild.preorder()
            if self.rchild:
                self.rchild.preorder()

    # Post-Order Traversal In Binary Search Tree
    def postorder(self):
        if self.key is None:
            return
        else:

            if self.lchild:
                self.lchild.postorder()
            if self.rchild:
                self.rchild.postorder()
            print(self.key, end=" ")

    # In-Order Traversal In Binary Search Tree
    def inorder(self):
        if self.key is None:
            return
        else:
            if self.lchild:
                self.lchild.inorder()
            print(self.key, end=" ")
            if self.rchild:
                self.rchild.inorder()

    # Deletion In Binary Search Tree
    def delete(self, data, curr):
        if self.key is None:
            print("Tree Is Empty")
            return
        if self.key > data:
            if self.lchild:
                self.lchild = self.lchild.delete(data, curr)
            else:
                print("Given Node is Not Present in the Tree")
        elif self.key < data:
            if self.rchild:
                self.rchild = self.rchild.delete(data, curr)
            else:
                print("Given Node is Not Present in the Tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = self.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key, curr)
            return self

    def min(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("\nmin node :", current.key)

    def max(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("\nmin node :", current.key)


def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)


root = BST(10)

list3 = [6, 3, 1, 98, 3, 7]
for i in list3:
    root.insert(i)
# root.delete(98)


root.preorder()
if count(root) > 1:
    root.delete(10, root.key)
else:
    print("can't perform deletion opearation!")

root.min()
root.max()
print("post")
root.postorder()
print("In-Order")
root.inorder()
# print(root.search(75))
