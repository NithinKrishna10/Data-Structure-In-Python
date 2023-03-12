class Trienode:
    def __init__(self):
        self.children = {}
        self.endofword = False


class Trie:
    def __init__(self):
        self.root = Trienode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trienode()
            curr = curr.children[c]
        curr.endofword = True

    def ins(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trienode()
            curr = curr.children[c]
        curr.endofword = True

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endofword

    def startwith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

    def sear(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endofword

    def printt(self):
        print(self.root.children)

    def insr(self, word ):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trienode()
            curr = curr.children[c]
        curr.endofword = True


trie = Trie()
words = ["wait", "waiter", "shop", "shopper", "nithin","nike","neymar","nani"]
for word in words:
    trie.insr(word)
c = "wait"
result = trie.search(c)
print("Search result is:", result)
trie.startwith("a")


def dfs(node, prefix, suggestions):
    print("dfjksj", node.endofword, "hdf", prefix)
    if node.endofword:
        print(prefix)
        suggestions.append(prefix)

    for char, child_node in node.children.items():
        print(child_node, char)
        dfs(child_node, prefix + char, suggestions)


def suggest(trie, prefix):
    node = trie.root
    for char in prefix:
        if char not in node.children:
            return []
        node = node.children[char]
    suggestions = []
    dfs(node, prefix, suggestions)
    return suggestions


def dfss(trie, prefix, suggestion):
    if trie.endofword:
        suggestion.append(prefix)
    for char, addres in trie.children.items():
        dfss(addres, prefix + char, suggestion)


def suggests(trie, prefix):
    curr = trie.root
    for c in prefix:
        if c not in curr.children:
            return []
        curr = curr.children[c]
    suggestion = []
    dfss(curr, prefix, suggestion)
    return suggestion


def inser(trie,word):
    curr = trie
    for c in word:
        if c not in curr:
            curr.children[c] = Trienode()
        curr = curr.children[c]
    curr.endofword = True

print()
# print(suggest(trie, "s"))s
print(suggests(trie, "w"))
# print()
# trie.printt()
# # print()
# print(trie.sear("wait"))
# print()
# print(trie.search("wait"))
