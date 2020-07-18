class Solution:
    def leastInterval(self, tasks, n: int):
        import collections
        ct = collections.Counter(tasks)
        nbucket = ct.most_common(1)[0][1]
        res = (nbucket-1)*(n+1)
        res += list(ct.values()).count(nbucket)
        return max(res, len(tasks))






