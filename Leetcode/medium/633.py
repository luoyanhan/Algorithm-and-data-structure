from math import sqrt
class Solution:
    def judgeSquareSum(self, c):
        left, right = 0, int(sqrt(c))
        while left <= right:
            s = left*left + right*right
            if s > c:
                right -= 1
            elif s < c:
                left += 1
            else:
                return True
        return False

#超时
class Solution:
    def judgeSquareSum(self, c):
        def binary(left, right, key):
            if left > right:
                return False
            mid = (left+right)//2
            if mid**2 == key:
                return True
            elif mid**2 > key:
                return binary(left, mid-1, key)
            else:
                return binary(mid+1, right, key)
        a = 0
        while a**2 <= c:
            b = c - a**2
            if binary(0, b, b):
                return True
            a += 1
        return False


print(Solution().judgeSquareSum(0))
