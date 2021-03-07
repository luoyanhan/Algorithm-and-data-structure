class Solution:
    def increasingTriplet(self, nums):
        length =len(nums)
        front = [nums[0] for _ in range(length)]
        back = [nums[-1] for _ in range(length)]
        for i in range(1, length):
            front[i] = min(front[i-1], nums[i])
        for i in range(length-2, 0, -1):
            back[i] = max(back[i+1], nums[i])
        for i in range(length):
            if front[i] < nums[i] and nums[i] < back[i]:
                return True
        return False

import sys
class Solution:
    def increasingTriplet(self, nums):
        mid, small = sys.maxsize, sys.maxsize
        length = len(nums)
        for i in range(length):
            if nums[i] <= small:
                small = nums[i]
            elif nums[i] <= mid:
                mid = nums[i]
            else:
                return True
        return False


class Solution:
    def increasingTriplet(self, nums):
        length = len(nums)
        dp = [1 for _ in range(length)]
        for i in range(1, length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            if dp[i] >= 3:
                return True
        return False

print(Solution().increasingTriplet([3,5,1,2,0,3]))