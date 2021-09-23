class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        mapper = [[0, -prices[0]] for _ in range(length+1)]
        for i in range(1, length):
            mapper[i][0] = max(mapper[i-1][1] + prices[i], mapper[i-1][0])
            mapper[i][1] = max(mapper[i-1][0] - prices[i], mapper[i-1][1])
        return max(mapper[length-1])


class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        dp0, dp1 = 0, -prices[0]
        for i in range(1, length):
            dp0 = max(dp0, dp1+prices[i])
            dp1 = max(dp1, dp0-prices[i])
        return max(dp0, dp1)