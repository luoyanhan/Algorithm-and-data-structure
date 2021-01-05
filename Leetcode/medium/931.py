class Solution:  #超出时间限制
    def minFallingPathSum(self, A):
        res = float('inf')
        length = len(A)
        path = list()
        def dfs(row, col):
            nonlocal res
            if row >= length:
                res = min(res, sum(path))
                return
            path.append(A[row][col])
            if 0 <= col-1 < length:
                dfs(row+1, col-1)
            if 0 <= col < length:
                dfs(row + 1, col)
            if 0 <= col + 1 < length:
                dfs(row + 1, col + 1)
            path.pop()
        for each in range(length):
            dfs(0, each)
        return res




print(Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))