class Solution:
    def findTargetSumWays(self, nums, target):
        length = len(nums)
        s_nums = sum(nums)
        if s_nums - target < 0 or (s_nums-target)%2 != 0:
            return 0
        neg = (s_nums-target) // 2
        dp = [[0 for j in range(neg+1)] for i in range(length+1)]
        dp[0][0] = 1
        for i in range(1, length+1):
            for j in range(neg+1):
                if nums[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
        return dp[length][neg]

