class Solution:
    def reverseWords(self, s: str) -> str:
        s_li = s.split()
        result = ' '.join(s_li[::-1])
        return result


print(Solution().reverseWords('the sky is blue'))