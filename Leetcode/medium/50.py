class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x = 1/x
            n = -n
        ans = 1
        temp = x
        while n > 0:
            if n % 2 == 1:
                ans = ans*temp
            temp = temp*temp
            n = int(n/2)
        return ans


