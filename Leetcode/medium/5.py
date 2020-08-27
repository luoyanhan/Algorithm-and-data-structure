class Solution:
    def longestPalindrome(self, s):
        res = ''
        length = len(s)
        mapping = [[False]*length for i in range(length)]
        for l in range(length):
            for j in range(length):
                end = l + j
                if end >= length:
                    break
                if l == 0:
                    mapping[j][end] = True
                elif l == 1:
                    mapping[j][end] = (s[j] == s[end])
                else:
                    mapping[j][end] = mapping[j+1][end-1] and s[j] == s[end]
                if mapping[j][end] and l+1 > len(res):
                    res = s[j: end+1]
        return res


class Solution:
    def longestPalindrome(self, s):
        start, end = 0, 0
        length = len(s)
        def inner(left, right):
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        for i in range(length):
            left1, right1 = inner(i, i)
            left2, right2 = inner(i, i+1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end+1]

