class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ptr0, ptr2, cur = 0, n-1, 0
        while cur <= ptr2:
            if nums[cur] == 0:
                nums[ptr0], nums[cur] = nums[cur], nums[ptr0]
                ptr0 += 1
                cur += 1
            elif nums[cur] == 2:
                nums[ptr2], nums[cur] = nums[cur], nums[ptr2]
                ptr2 -= 1
            else:
                cur += 1