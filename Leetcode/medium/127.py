class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        from collections import defaultdict
        if endWord not in wordList:
            return 0
        Map = defaultdict(list)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                key = word[:i] + '*' + word[i+1:]
                Map[key].append(word)
        visited = {beginWord: True}
        queue = [(beginWord, 1)]
        while queue:
            word, level = queue.pop(0)
            for i in range(L):
                key = word[:i] + '*' + word[i+1:]
                for each in Map[key]:
                    if each == endWord:
                        return level + 1
                    if each not in visited:
                        visited[each] = True
                        queue.append((each, level+1))
                Map[key] = list()
        return 0


class Solution:
    def __init__(self):
        from collections import defaultdict
        self.length = 0
        self.Map = defaultdict(list)

    def inner(self, queue, visited, other_visited):
        word, level = queue.pop(0)
        for i in range(self.length):
            key = word[:i] + '*' + word[i+1:]
            for each in self.Map[key]:
                if each in other_visited:
                    return level + other_visited[each]
                if each not in visited:
                    visited[each] = level + 1
                    queue.append((each, level + 1))
            self.Map[key] = list()


    def ladderLength(self, beginWord, endWord, wordList):
        self.length = len(beginWord)
        if endWord not in wordList:
            return 0
        for word in wordList:
            for i in range(self.length):
                key = word[:i] + '*' + word[i+1:]
                self.Map[key].append(word)
        begin_visited = {beginWord: 1}
        begin_queue = [(beginWord, 1)]
        end_visited = {endWord: 1}
        end_queue = [(endWord, 1)]
        while begin_queue and end_queue:
            ans = self.inner(begin_queue, begin_visited, end_visited)
            if ans:
                return ans
            ans = self.inner(end_queue, end_visited, begin_visited)
            if ans:
                return ans
        return 0