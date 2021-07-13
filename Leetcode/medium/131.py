class Solution:   #回溯
    def partition(self, s):
        res = list()
        path = list()
        def judge(s):
            return s == s[::-1]

        def dfs(remain_s):
            if not remain_s:
                res.append(path[:])
            for i in range(1, len(remain_s)+1):
                this_time = remain_s[:i]
                path.append(this_time)
                if judge(this_time):
                    dfs(remain_s[i:])
                path.pop()
        dfs(s)
        return res


class Solution:
    def partition(self, s):
        length = len(s)
        dp = [[True for i in range(length)] for j in range(length)]
        for i in range(length-2, -1, -1):
            for j in range(i+1, length):
                dp[i][j] = s[i] == s[j] and dp[i+1][j-1]

        res = list()
        path = list()
        def dfs(idx):
            if idx == length:
                res.append(path[:])
            for j in range(idx, length):
                path.append(s[idx:j+1])
                if dp[idx][j]:
                    dfs(j+1)
                path.pop()
        dfs(0)
        return res



print(Solution().partition("aab"))

