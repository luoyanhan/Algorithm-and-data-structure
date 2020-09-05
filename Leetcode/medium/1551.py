class Solution:
    def minOperations(self, n: int) -> int:
        #平均值是n
        res = 0
        for i in range(n):
            if 2 * i + 1 > n:
                res += 2 * i + 1 - n
        return res