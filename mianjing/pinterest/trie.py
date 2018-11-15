class Trie(object):
    def __init__(self):
        self.root = dict()
        self.END = '/'

    def add(self, word):
        node = self.root
        for ch in word:
            node.setdefault(ch, dict())
            node = node[ch]
        node[self.END] = None

    def find(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return self.END in node

trie = Trie()
a = "add"
b = "ad"
c = "a"
trie.add(a)
trie.add(b)
print(trie.find(a))
print(trie.find(c))