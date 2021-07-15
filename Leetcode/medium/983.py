class Solution:
    def mincostTickets(self, days, costs) -> int:
        dp = [0 for _ in range(365+1)]
        for day in range(days[-1], days[0]-1, -1):
            if day in days:
                one = costs[0] + dp[day+1] if day+1 < 366 else costs[0]
                seven = costs[1] + dp[day+7] if day+7 < 366 else costs[1]
                thirty = costs[2] + dp[day+30] if day+30 < 366 else costs[2]
                dp[day] = min(one, seven, thirty)
            else:
                dp[day] = dp[day+1] if day+1 < 366 else dp[day]
        return dp[days[0]]


print(Solution().mincostTickets([1,4,6,7,8,365], [2,7,15]))