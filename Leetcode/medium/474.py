class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        dp = [[0]*(n+1) for i in range(m+1)]
        for s in strs:
            tmp_m = m
            c_0 = s.count('0')
            c_1 = s.count('1')
            while tmp_m >= c_0:
                tmp_n = n
                while tmp_n >= c_1:
                    dp[tmp_m][tmp_n] = max(dp[tmp_m][tmp_n], 1+dp[tmp_m-c_0][tmp_n-c_1])
                    tmp_n -= 1
                tmp_m -= 1
        return dp[m][n]

print(Solution().findMaxForm(["10","0001","111001","1","0"], 5, 3))

