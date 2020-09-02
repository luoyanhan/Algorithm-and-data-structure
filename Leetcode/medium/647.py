class Solution:
    def countSubstrings(self, s: str):
        res = 0
        length = len(s)
        def inner(left, right):
            nonlocal res
            while left >= 0 and right < length and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        for i in range(length):
            inner(i, i)
            inner(i, i+1)
        return res


class Solution:
    def countSubstrings(self, s: str):
        res = 0
        length = len(s)
        for i in range(2*length-1):
            left = i//2
            right = left + i % 2
            while left >= 0 and right < length and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res


print(Solution().countSubstrings("abc"))

