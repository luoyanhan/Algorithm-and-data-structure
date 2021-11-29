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


class Solution:
    def lengthOfLongestSubstring(self, s):
        length = len(s)
        if not length:
            return 0
        left, right = 0, 0
        max_length = 0
        cur_length = 0
        se = set()
        while right < length:
            if s[right] not in se:
                cur_length += 1
                max_length = max(max_length, cur_length)
                se.add(s[right])
                right += 1
            else:
                while s[right] in se:
                    se.remove(s[left])
                    left += 1
                    cur_length -= 1
        return max_length


