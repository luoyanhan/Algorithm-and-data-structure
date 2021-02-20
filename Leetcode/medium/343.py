class Solution:
    def integerBreak(self, n):
        dp = [0 for i in range(n+1)]
        for i in range(2, n+1):
            for j in range(i):
                dp[i] = max(j*(i-j), j*dp[i-j], dp[i])
        return dp[n]