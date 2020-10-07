class Solution:
    #暴力枚举， 超时
    def numSquares(self, n: int) -> int:
        import math
        nums = [num**2 for num in range(1, int(math.sqrt(n))+1)]
        def findmin(k):
            if k in nums:
                return 1
            min_time = float('inf')
            for num in nums:
                if num > k:
                    break
                time = findmin(k-num) + 1
                min_time = min(min_time, time)
            return min_time
        return findmin(n)



class Solution:
    #动态规划
    def numSquares(self, n: int) -> int:
        import math
        nums = [num**2 for num in range(int(math.sqrt(n))+1)]
        dp = [float('inf') for i in range(n+1)]
        dp[0] = 0
        for i in range(1, n+1):
            for num in nums:
                if num > i:
                    break
                dp[i] = min(dp[i], dp[i-num] + 1)
        return dp[-1]
