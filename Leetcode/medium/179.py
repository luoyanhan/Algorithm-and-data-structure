class Solution:
    def largestNumber(self, nums):
        from functools import cmp_to_key
        temp = sorted(list(map(str, nums)), key=cmp_to_key(lambda x, y: int(x+y)-int(y+x)), reverse=True)
        return ''.join(temp if temp[0] != '0' else '0')




print(Solution().largestNumber([10,2]))