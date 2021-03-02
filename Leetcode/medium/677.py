class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapper = dict()


    def insert(self, key: str, val: int) -> None:
        self.mapper[key] = val


    def sum(self, prefix: str) -> int:
        cnt = 0
        for key in self.mapper:
            if key.startswith(prefix):
                cnt += self.mapper[key]
        return cnt


from collections import defaultdict
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapper = defaultdict(int)
        self.prefix_map = defaultdict(int)


    def insert(self, key: str, val: int) -> None:
        diff = val - self.mapper[key]
        self.mapper[key] = val
        for i in range(1, len(key)+1):
            self.prefix_map[key[:i]] += diff


    def sum(self, prefix: str) -> int:
        return self.prefix_map[prefix]


from collections import defaultdict
class Trie():
    def __init__(self):
        self.children = dict()
        self.score = 0

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapper = defaultdict(int)
        self.root = Trie()


    def insert(self, key: str, val: int) -> None:
        cur = self.root
        diff = val - self.mapper[key]
        self.mapper[key] = val
        for each in key:
            if each in cur.children:
                cur = cur.children[each]
            else:
                tmp = Trie()
                cur.children[each] = tmp
                cur = cur.children[each]
            cur.score += diff


    def sum(self, prefix: str) -> int:
        cur = self.root
        for each in prefix:
            if each not in cur.children:
                return 0
            cur = cur.children[each]
        return cur.score
