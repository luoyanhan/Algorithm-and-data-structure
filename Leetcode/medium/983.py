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


class Solution:
    def mincostTickets(self, days, costs) -> int:
        length = len(days)
        dp = [1000*length for _ in range(length)]
        for i in range(length-1, -1, -1):
            j = i
            for day, cost in zip([1, 7, 30], costs):
                while j < length and days[i] + day > days[j]:
                    j += 1
                dp[i] = min(dp[j] + cost, dp[i]) if length > j > i else min(cost, dp[i])
        return dp[0]

print(Solution().mincostTickets([6,9,10,14,15,16,17,18,20,22,23,24,29,30,31,33,35,37,38,40,41,46,47,51,54,57,59,65,70,76,77,81,85,87,90,91,93,94,95,97,98,100,103,104,105,106,107,111,112,113,114,116,117,118,120,124,128,129,135,137,139,145,146,151,152,153,157,165,166,173,174,179,181,182,185,187,188,190,191,192,195,196,204,205,206,208,210,214,218,219,221,225,229,231,233,235,239,240,245,247,249,251,252,258,261,263,268,270,273,274,275,276,280,283,285,286,288,289,290,291,292,293,296,298,299,301,303,307,313,314,319,323,325,327,329,334,339,340,341,342,344,346,349,352,354,355,356,357,358,359,363,364],
                                [21, 115, 345]))