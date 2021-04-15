class Solution:
    def rob(self, nums):
        length = len(nums)
        if length <= 1:
            return 0 if not length else nums[0]
        dp = [0 for _ in range(length)]
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for i in range(2, length):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[length-1]


class Solution:
    def rob(self, nums):
        length = len(nums)
        if length <= 1:
            return 0 if not length else nums[0]
        pre_second = nums[0]
        pre_first = max(pre_second, nums[1])
        cur = max(pre_first, pre_second)
        for i in range(2, length):
            cur = max(pre_first, pre_second+nums[i])
            pre_second = pre_first
            pre_first = cur
        return cur


print(Solution().rob([1, 2, 3, 1]))