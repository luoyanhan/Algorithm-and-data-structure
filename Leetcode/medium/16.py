class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        length = len(nums)
        nearest = nums[0] + nums[1] + nums[2]
        for i in range(length-2):
            left = i+1
            right = length-1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp == target:
                    return target
                if abs(temp-target) < abs(nearest-target):
                    nearest = temp
                if temp >= target:
                    right -= 1
                else:
                    left += 1
        return nearest

print(Solution().threeSumClosest([-1,2,1,-4], 1))


