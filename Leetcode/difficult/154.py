class Solution:
    def findMin(self, nums):
        length = len(nums)
        if length == 1:
            return nums[0]
        for i in range(1, length):
            if nums[i-1] > nums[i]:
                return nums[i]
        return nums[0]