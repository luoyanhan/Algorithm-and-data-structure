class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        first = 10
        second = 9 * 9
        top = min(10, n)
        for i in range(2, top+1):
            first += second
            second *= (10-i)
        return first