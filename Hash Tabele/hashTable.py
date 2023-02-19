class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

class hashtable:
    def _init_(self):
        self.size = 100
        self.arr = [[] for i in range(self.size)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h = ord(char)
        return h % self.size

    def getitem(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def setitem(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[idx][h] = (key, value)
            found = True
            break
        if not found:
            self.arr[h].append((key, value))

ht = hashtable()
ht.setitem('misbah', '20')
print((ht.getitem('misbah')))
t = HashTable()