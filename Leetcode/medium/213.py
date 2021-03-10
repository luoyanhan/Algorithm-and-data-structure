class Solution:
    def rob(self, nums):
        length = len(nums)
        def inner(start, end):
            cur, pre = 0, 0
            for i in range(start, end):
                cur, pre = max(pre + nums[i], cur), cur
            return cur
        return max(inner(1, length), inner(0, length-1)) if length > 1 else nums[0]



