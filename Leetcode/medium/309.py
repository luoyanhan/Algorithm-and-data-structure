class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        dp = [[0, 0, 0] for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = 0
        print(dp)
        for day in range(1, length):
            dp[day][0] = max(dp[day-1][0], dp[day-1][2]-prices[day])
            dp[day][1] = dp[day-1][0] + prices[day]
            dp[day][2] = max(dp[day-1][1], dp[day-1][2])
        return max(dp[length-1][1], dp[length-2][2])


print(Solution().maxProfit([1,4,2]))