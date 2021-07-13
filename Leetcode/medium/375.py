class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[n**2 for i in range(n+1)] for j in range(n+1)]
        for i in range(1, n+1):
            dp[i][i] = 0
        for j in range(2, n+1):
            for i in range(j-1, 0, -1):
                for k in range(i+1, j):
                    dp[i][j] = min(k+max(dp[i][k-1], dp[k+1][j]), dp[i][j])
                dp[i][j] = min(i+dp[i+1][j], dp[i][j])
                dp[i][j] = min(j+dp[i][j-1], dp[i][j])
        return dp[1][n]
