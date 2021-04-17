class Trie:

    def __init__(self):
        self.is_end = False
        self.children = dict()


    def insert(self, word):
        node = self
        for each in word:
            child = Trie() if each not in node.children else node.children[each]
            node.children[each] = child
            node = child
        node.is_end = True


    def search(self, word):
        node = self
        for each in word:
            if each not in node.children:
                return False
            node = node.children[each]
        if node.is_end:
            return True
        return False


    def startsWith(self, prefix):
        node = self
        for each in prefix:
            if each not in node.children:
                return False
            node = node.children[each]
        return True

