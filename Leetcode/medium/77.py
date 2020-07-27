class Solution:
    def combine(self, n, k):
        res = list()
        path = list()
        def trackback(length, pre_index):
            if length == k:
                res.append(path[:])
                return
            if pre_index < n-1:
                for i in range(pre_index+1, n):
                    path.append(i+1)
                    trackback(length+1, i)
                    path.pop()
        trackback(0, -1)
        return res


print(Solution().combine(4, 2))





