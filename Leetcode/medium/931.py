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


class Solution:  #动态规划
    def minFallingPathSum(self, A):
        length = len(A[0])
        while len(A) > 1:
            last_row = A.pop()
            for idx in range(length):
                A[-1][idx] += min(last_row[max(0, idx-1): min(length, idx+2)])
        return min(A[-1])



print(Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))