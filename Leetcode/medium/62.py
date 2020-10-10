class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*m] + [[1] + [0]*(m-1)] * (n-1)
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]


class Solution:
    #空间优化
    def uniquePaths(self, m: int, n: int) -> int:
        pre = [1]*m
        cur = pre[:]
        for i in range(1, n):
            for j in range(1, m):
                cur[j] = cur[j-1] + pre[j]
            pre = cur[:]
        return cur[-1]

class Solution:
    #空间优化
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*m
        for i in range(1, n):
            for j in range(1, m):
                dp[j] += dp[j-1]
        return dp[-1]



Solution().uniquePaths(7, 3)