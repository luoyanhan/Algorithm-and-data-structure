class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort()
        length = len(intervals)
        dp = [0 for _ in range(length)]
        dp[0] = 1
        for i in range(1, length):
            dp[i] = max([dp[j] for j in range(i) if intervals[j][1] <= intervals[i][0]], default=0) + 1
        return length - dp[length-1]

class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])
        length = len(intervals)
        total = 1
        right = intervals[0][1]
        for i in range(1, length):
            if intervals[i][0] >= right:
                total += 1
                right = intervals[i][1]
        return length - total



print(Solution().eraseOverlapIntervals([ [1,2], [2,3], [3,4], [1,3] ]))