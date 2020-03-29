class Trie(object):
    def __init__(self):
        self.root = dict()
        self.end = -1

    def insert(self, word):
        currnode = self.root
        for char in word:
            if not currnode.get(char):
                currnode[char] = dict()
            currnode = currnode.get(char)
        currnode[self.end] = True

    def search(self, word):
        currnode = self.root
        for char in word:
            if not currnode.get(char):
                return False
            currnode = currnode.get(char)
        if not currnode.get(self.end):
            return False
        return True

    def startswith(self, word):
        currnode = self.root
        for char in word:
            if not currnode.get(char):
                return False
            currnode = currnode.get(char)
        return True



