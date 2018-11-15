class TextValidation(object):

    def __init__(self, blacklist=None):
        self.root = dict()
        self.END = '/'
        self.blacklist = blacklist
        self.initialize_trie()

    def initialize_trie(self):
        for phrase in blacklist:
            node = self.root
            words = phrase.split()
            for word in words:
                node.setdefault(word, dict())
                node = node[word]
            node[self.END] = None

    def is_safe(self, text):
        words = text.split()
        for start, word in enumerate(words):
            if word in self.root:
                node = self.root[word]
                if self.END in node:
                    return False
                for w in words[start + 1:]:
                    if w in node:
                        node = node[w]
                        if self.END in node:
                            return False
                    else:
                        break
        return True


blacklist = ["machine guns", "world war i", "hate"]
textValid = TextValidation(blacklist)
s1 = "i love world war i"
s2 = "i love world war ii"
s3 = "world i love world war i"
s4 = "hate"
s = [s1, s2, s3, s4]

for ss in s:
    print(textValid.is_safe(ss))