class Solution:
    def grayCode(self, n):
        res = [0]
        head = 1
        for i in range(n):
            for j in range(len(res)-1, -1, -1):
                res.append(head+res[j])
            head <<= 1
        return res

print(Solution().grayCode(2))




