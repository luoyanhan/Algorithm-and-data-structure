class Solution:
    def PredictTheWinner(self, nums):
        def inner(start, end, turn):
            if start == end:
                return nums[start]*turn
            score_start = nums[start] * turn + inner(start+1, end, -turn)
            score_end = nums[end] * turn + inner(start, end-1, -turn)
            return max(score_start*turn, score_end*turn)*turn
        return inner(0, len(nums)-1, 1) >= 0


class Solution:
    def PredictTheWinner(self, nums):
        def inner(start, end, turn):
            if start == end:
                return nums[start] * turn
            num_start = nums[start]*turn + inner(start+1, end, -turn)
            num_end = nums[end]*turn + inner(start, end-1, -turn)
            if turn == 1:
                return max(num_end, num_start)
            else:
                return min(num_end, num_start)
        return inner(0, len(nums)-1, 1) >= 0


class Solution:
    def PredictTheWinner(self, nums):
        length = len(nums)
        dp = [[0]*length for i in range(length)]
        for i in range(length):
            dp[i][i] = nums[i]
        for i in range(length-2, -1, -1):
            for j in range(i+1, length):
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][length-1] >= 0


class Solution:
    def PredictTheWinner(self, nums):
        length = len(nums)
        dp = [nums[i] for i in range(length)]
        for i in range(length-2, -1, -1):
            for j in range(i+1, length):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])
        return dp[length-1] >= 0


