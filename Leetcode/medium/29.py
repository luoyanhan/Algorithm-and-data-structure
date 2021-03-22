
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        max_int = 2**31-1
        min_int = -2**31
        flag = 1
        if dividend < 0:
            flag, dividend = -flag, -dividend
        if divisor < 0:
            flag, divisor = -flag, -divisor
        res = 0
        while dividend >= divisor:
            mul = 1
            tmp_div = divisor
            #先乘再比较可以省掉一些判断和回退
            while tmp_div * 2 < dividend:
                mul *= 2
                tmp_div *= 2
            dividend -= tmp_div
            res += mul
        res *= flag
        if res < min_int:
            return min_int
        elif res > max_int:
            return max_int
        else:
            return res