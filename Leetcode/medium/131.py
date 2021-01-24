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




print(Solution().partition("aab"))

