class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        dp = [[0, 0, 0] for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = 0
        for day in range(1, length):
            dp[day][0] = max(dp[day-1][0], dp[day-1][2]-prices[day])
            dp[day][1] = dp[day-1][0] + prices[day]
            dp[day][2] = max(dp[day-1][1], dp[day-1][2])
        return max(dp[length-1][1], dp[length-1][2])


class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        pre0 = -prices[0]
        pre1 = 0
        pre2 = 0
        cur0, cur1, cur2 = 0, 0, 0
        for day in range(1, length):
            cur0 = max(pre0, pre2-prices[day])
            cur1 = pre0 + prices[day]
            cur2 = max(pre1, pre2)
            pre0 = cur0
            pre1 = cur1
            pre2 = cur2
        return max(cur1, cur2)


print(Solution().maxProfit([1,4,2]))