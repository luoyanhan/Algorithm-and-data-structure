class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 0
        for i in range(length):
            if i == 0 and nums[i] > nums[i+1]:
                    return i
            elif i == length-1 and nums[i] > nums[i-1]:
                return i
            else:
                left = nums[i-1]
                right = nums[i+1]
                if nums[i] > left and nums[i] > right:
                    return i


