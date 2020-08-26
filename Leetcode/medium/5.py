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

