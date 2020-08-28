class Solution:
    def canJump(self, nums):
        length = len(nums)
        rightmost = 0
        for idx in range(length):
            if idx <= rightmost and idx + nums[idx] > rightmost:
                rightmost = idx + nums[idx]
        return rightmost >= length - 1


