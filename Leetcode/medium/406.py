class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda x: (x[0], -x[1]))
        length = len(people)
        res = [[] for _ in range(length)]
        for p in people:
            space = p[1] + 1
            for i in range(length):
                if not res[i]:
                    space -= 1
                    if not space:
                        res[i] = p
        return res


class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda x: (-x[0], x[1]))
        res = list()
        for p in people:
            res[p[1]:p[1]] = [p]
        return res