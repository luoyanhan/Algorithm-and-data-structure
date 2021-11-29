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


class Solution:
    def longestPalindrome(self, s):
        def check(left, right, words):
            while left <= right:
                if words[left] != words[right]:
                    return False
                left += 1
                right -= 1
            return True

        res_left, res_right = 0, 0
        for left in range(len(s)):
            right = len(s)
            if right - left < res_right - res_left:
                break
            while right >= left:
                right -= 1
                if check(left, right, s) and right - left > res_right - res_left:
                    res_right = right
                    res_left = left
                    break
        return s[res_left:res_right+1]


class Solution:
    def longestPalindrome(self, s):
        length = len(s)
        dp = [[False for j in range(length)] for i in range(length)]
        for i in range(length):
            dp[i][i] = True
        max_length = 1
        res_left, res_right = 0, 0
        for L in range(2, length+1):
            for left in range(length):
                right = left + L - 1
                if right > length-1:
                    break
                if s[left] == s[right]:
                    if L == 2:
                        dp[left][right] = True
                    elif L > 2:
                        dp[left][right] = dp[left+1][right-1]
                if dp[left][right] and L > max_length:
                    max_length = L
                    res_left, res_right = left, right
        return s[res_left:res_right+1]


class Solution:
    def longestPalindrome(self, s):
        def expand(words, left, right):
            while left >= 0 and right < len(words) and words[left] == words[right]:
                left -= 1
                right += 1
            return left+1, right-1

        res_left, res_right = 0, 0
        for left in range(len(s)):
            left1, right1 = expand(s, left, left)
            left2, right2 = expand(s, left, left+1)
            if right1-left1 > res_right - res_left:
                res_left, res_right = left1, right1
            if right2-left2 > res_right - res_left:
                res_left, res_right = left2, right2
        return s[res_left:res_right+1]

