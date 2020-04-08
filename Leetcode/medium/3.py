class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        max_length = 0
        for i in range(length):
            result = ''
            j = i
            while j < length and s[j] not in result:
                result += s[j]
                j += 1
            if len(result) > max_length:
                max_length = len(result)
        return max_length

