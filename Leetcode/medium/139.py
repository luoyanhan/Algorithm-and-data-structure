class Solution:
    def wordBreak(self, s, wordDict):
        length = len(s)
        dp = [False] * (length+1)
        dp[0] = True
        for i in range(1, length+1):
            for j in range(0, i):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = True
        return dp[length]


print(Solution().wordBreak("leetcode", ["leet","code"]))