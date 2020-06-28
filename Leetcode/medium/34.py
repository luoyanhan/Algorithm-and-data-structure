class Solution:
    def searchRange(self, nums, target: int):
        left = 0
        length = len(nums)
        right = length - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                i = mid
                while i - 1 >= 0 and nums[i-1] == target:
                    i -= 1
                j = mid
                while j + 1 < length and nums[j+1] == target:
                    j += 1
                return [i, j]
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [-1, -1]


