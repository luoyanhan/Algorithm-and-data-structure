class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for i in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif i > 0 and j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                elif i > 0 and j > 0:
                    dp[i][j] = min(dp[i][j - 1], dp[i-1][j]) + grid[i][j]
        return dp[m-1][n-1]


print(Solution().minPathSum([[1]]))