class Solution:
    def hanming(self, num):
        res = 0
        while num > 0:
            num &= num - 1
            res += 1
        return res
    def countBits(self, num: int):
        return [self.hanming(i) for i in range(num+1)]

class Solution:
    def countBits(self, num: int):
        i, b = 0, 1
        res = [0] * (num+1)
        while b <= num:
            while i < b and i + b <= num:
                res[i+b] = res[i] + 1
                i += 1
            i = 0
            b <<= 1
        return res

class Solution:
    def countBits(self, num: int):
        res = [0] * (num+1)
        for i in range(1, num+1):
            res[i] = res[i >> 1] + (i & 1)
        return res


class Solution:
    def countBits(self, num: int):
        res = [0] * (num+1)
        for i in range(1, num+1):
            res[i] = res[i & (i-1)] + 1
        return res