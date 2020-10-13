class Solution:
    def matrixBlockSum(self, mat, K: int) :
        m, n = len(mat), len(mat[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + mat[i-1][j-1]

        def get(x, y):
            if x < 0:
                x = 0
            elif x > m:
                x = m
            if y < 0:
                y = 0
            elif y > n:
                y = n
            return dp[x][y]

        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = get(i+K+1, j+K+1) - get(i-K, j+K+1) - get(i+K+1, j-K) + get(i-K, j-K)
        return ans




class Solution:
    def matrixBlockSum(self, mat, K: int) :
        m, n = len(mat), len(mat[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + mat[i-1][j-1]

        def get(x, y):
            x = min(max(x, 0), m)
            y = min(max(y, 0), n)
            return dp[x][y]

        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = get(i+K+1, j+K+1) - get(i-K, j+K+1) - get(i+K+1, j-K) + get(i-K, j-K)
        return ans