class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def getitem(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def setitem(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    def show(self):
        print(self.arr)

    def delitem(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del", index)
                del self.arr[arr_index][index]


class hash:
    def __init__(self):
        self.size = 20
        self.arr = [[] for i in range(self.size)]

    def gethash(self, key):
        h = 0
        for k in key:
            h += ord(k)
        return h % self.size

    def getitem(self, key):
        h = self.gethash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def show(self):
        print(self.arr)

    def setitem(self, key, valu):
        h = self.gethash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[idx][h] = (key, valu)
                found = True
        if not found:
            self.arr[h].append((key, valu))


class hashmap:

    def __init__(self):
        self.size = 20
        self.arr = [[] for i in range(self.size)]

    def hashkey(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h

    def setitem(self, key, val):
        h = self.hashkey(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[idx], [h] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    def getItem(self, key):
        h = self.hashkey(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]


ht = HashTable()
ht.setitem("march 6", '50')
ht.setitem("march 17", '59')
ht.setitem("misbahl", '50')
print(ht.getitem("march 6"))
ht.show()
