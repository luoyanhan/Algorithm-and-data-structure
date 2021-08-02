class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)


class Solution:
    def lengthOfLIS(self, nums):
        length = len(nums)
        dp = [1 for _ in range(length)]
        for i in range(1, length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


class Solution:
    def lengthOfLIS(self, nums):
        dp = list()
        for num in nums:
            if not dp or num > dp[-1]:
                dp.append(num)
            else:
                left, right = 0, len(dp)-1
                loc = right
                while left <= right:
                    mid = (left+right)//2
                    if dp[mid] >= num:
                        loc = mid
                        right = mid - 1
                    else:
                        left = mid + 1
                dp[loc] = num
        return len(dp)


