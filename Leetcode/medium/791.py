class Solution:
    def customSortString(self, S, T):
        import collections
        d = collections.Counter(T)
        res = list()
        for each in S:
            if each in d:
                res.extend([each]*d[each])
                d[each] = 0
        for each in d:
            if d[each]:
                res.extend([each] * d[each])
        return ''.join(res)



print(Solution().customSortString("cba",  "abcd"))