class Solution:
    def replaceWords(self, dictionary, sentence):
        dictionary.sort(key=lambda x: (x, len(x)))
        li = sentence.split()
        for i in range(len(li)):
            word = li[i]
            for each in dictionary:
                if word.startswith(each):
                    li[i] = each
                    break
        return ' '.join(li)

class Solution:
    def replaceWords(self, dictionary, sentence):
        dictionary = set(dictionary)
        li = sentence.split()
        for i in range(len(li)):
            word = li[i]
            for j in range(1, len(word)+1):
                if word[:j] in dictionary:
                    li[i] = word[:j]
                    break
        return ' '.join(li)

from collections import defaultdict
from functools import reduce
class Solution:
    def replaceWords(self, dictionary, sentence):
        Trie = lambda: defaultdict(Trie)
        root = Trie()
        for word in dictionary:
            reduce(dict.__getitem__, word, root)['end'] = word
        def repl(word):
            cur = root
            for letter in word:
                if letter not in cur or 'end' in cur:
                    break
                cur = cur[letter]
            return cur.get('end', word)

        return ' '.join(map(repl, sentence.split()))

print(Solution().replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))

