class Solution:
    def longestPalindromeSubseq(self, s):
        length = len(s)
        if length < 2:
            return length
        dp = [[0 for j in range(length)] for i in range(length)]
        for i in range(length):
            dp[i][i] = 1
        for i in range(length-2, -1, -1):
            for j in range(i+1, length):
                if s[i] == s[j]:
                    dp[i][j] = max(dp[i][j], 2+dp[i+1][j-1])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][length-1]


Solution().longestPalindromeSubseq('aa')

