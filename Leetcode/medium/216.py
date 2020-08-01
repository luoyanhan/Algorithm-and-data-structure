class Solution:
    def combinationSum3(self, k, n):
        res = list()
        path = list()
        def trackback(first):
            length = len(path)
            s = sum(path)
            if s == n and length == k:
                res.append(path[:])
            if length > k or s > n:
                return
            for i in range(first, 10):
                path.append(i)
                trackback(i+1)
                path.pop()
        trackback(1)
        return res


print(Solution().combinationSum3(3, 15))
