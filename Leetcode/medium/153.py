class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        for i in range(1, length):
            if nums[i] < nums[i-1]:
                return nums[i]
        return nums[0]