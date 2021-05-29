class Solution:
    def countAndSay(self, n):
        if n == 1:
            return '1'
        n = self.countAndSay(n-1)
        res = ''
        cnt = 0
        pre = None
        for cur in n:
            if pre is not None and cur != pre:
                res += str(cnt) + pre
                cnt = 1
            else:
                cnt += 1
            pre = cur
        if pre:
            res += str(cnt) + pre
        return res


print(Solution().countAndSay(4))