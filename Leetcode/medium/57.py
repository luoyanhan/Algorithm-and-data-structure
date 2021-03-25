class Solution:
    def insert(self, intervals, newInterval):
        left, right = newInterval
        res = list()
        placed = False
        for l, r in intervals:
            if r < left:
                res.append([l, r])
            elif l > right:
                if not placed:
                    placed = True
                    res.append([left, right])
                res.append([l, r])
            else:
                left = min(left, l)
                right = max(right, r)
        if not placed:
            res.append([left, right])
        return res


print(Solution().insert([[1,5]], [2, 7]))
