class Solution:
    def minimumTotal(self, triangle):
        depth, max_width = len(triangle), len(triangle[-1])
        dp = [[0]*i for i in range(1, depth+1)]
        dp[0][0] = triangle[0][0]
        for i in range(1, depth):
            cols = i+1
            for j in range(cols):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == len(triangle[i])-1:
                    dp[i][j] = dp[i - 1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        return min(dp[-1])

class Solution:
    def minimumTotal(self, triangle):
        depth, max_width = len(triangle), len(triangle[-1])
        floor = [0] * max_width
        floor[0] = triangle[0][0]
        for i in range(1, depth):
            floor[i] = floor[i-1] + triangle[i][i]
            for j in range(i-1, 0, -1):
                floor[j] = min(floor[j], floor[j-1]) + triangle[i][j]
            floor[0] += triangle[i][0]
        return min(floor)


print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))