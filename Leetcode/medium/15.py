class Solution:
    def threeSum(self, nums):
        length = len(nums)
        result = []
        nums.sort()
        for i in range(length-2):
            if nums[i] > 0:
                return result
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = length - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < 0:
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    left += 1
                elif s > 0:
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
        return result

print(Solution().threeSum([-2,0,0,2,2]))
