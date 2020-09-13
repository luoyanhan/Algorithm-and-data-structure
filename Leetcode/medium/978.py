class Solution:
    def maxTurbulenceSize(self, A) -> int:
        def cmp(x, y):
            if x < y:
                return -1
            elif x == y:
                return 0
            else:
                return 1
        length = len(A)
        res = 1
        anchor = 0
        for i in range(1, length):
            c = cmp(A[i-1], A[i])
            if i == length-1 or c*cmp(A[i], A[i+1]) != -1:
                if c != 0:
                    res = max(res, i-anchor+1)
                anchor = i
        return res


print(Solution().maxTurbulenceSize([9,9,9]))

