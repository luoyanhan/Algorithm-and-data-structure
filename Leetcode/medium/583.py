class Solution:
    def minDistance(self, word1, word2):
        def cal(s1, s2, m, n):
            if m == 0 or n == 0:
                return 0
            if s1[m-1] == s2[n-1]:
                return 1+cal(s1, s2, m-1, n-1)
            else:
                return max(cal(s1, s2, m-1, n), cal(s1, s2, m, n-1))
        return len(word1) + len(word2) - 2*cal(word1, word2, len(word1), len(word2))


class Solution:
    def minDistance(self, word1, word2):
        dp = [[0 for _ in range(len(word2)+1)] for j in range(len(word1)+1)]
        def cal(s1, s2, m, n):
            if m == 0 or n == 0:
                return 0
            if dp[m][n] > 0:
                return dp[m][n]
            if s1[m-1] == s2[n-1]:
                dp[m][n] = 1 + cal(s1, s2, m-1, n-1)
            else:
                dp[m][n] = max(cal(s1, s2, m - 1, n), cal(s1, s2, m, n - 1))
            return dp[m][n]
        return len(word1) + len(word2) - 2 * cal(word1, word2, len(word1),
                                                 len(word2))


class Solution:
    def minDistance(self, word1, word2):
        dp = [[0 for _ in range(len(word2)+1)] for j in range(len(word1)+1)]
        length1, length2 = len(word1), len(word2)
        for i in range(length1+1):
            for j in range(length2+1):
                if i == 0 or j == 0:
                    continue
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return length1 + length2 - 2*dp[length1][length2]


class Solution:
    def minDistance(self, word1, word2):
        length1, length2 = len(word1), len(word2)
        dp = [[length1 + length2 for _ in range(len(word2)+1)] for j in range(len(word1)+1)]
        for i in range(length1 + 1):
            for j in range(length2 + 1):
                if i == 0 or j == 0:
                    dp[i][j] = max(i, j)
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
        return dp[length1][length2]


class Solution:
    def minDistance(self, word1, word2):
        length1, length2 = len(word1), len(word2)
        dp = [length1 + length2 for _ in range(length2+1)]
        for i in range(length1+1):
            temp = [length1 + length2 for _ in range(length2+1)]
            for j in range(length2+1):
                if i == 0 or j == 0:
                    temp[j] = max(i, j)
                elif word1[i-1] == word2[j-1]:
                    temp[j] = dp[j-1]
                else:
                    temp[j] = 1 + min(dp[j], temp[j-1])
            dp = temp[:]
        return dp[length2]

print(Solution().minDistance("dinitrophenylhydrazine", "benzalphenylhydrazone"))