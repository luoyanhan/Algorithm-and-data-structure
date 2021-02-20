class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        res = 0
        length = len(timeSeries)
        for i in range(length):
            if i < length - 1:
                res += min(duration, timeSeries[i+1] - timeSeries[i])
            else:
                res += duration
        return res

