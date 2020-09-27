class Solution:
    def stoneGame(self, piles) -> bool:
        li = 0
        a = 0
        while piles:
            first = piles.pop(0)
            last = piles.pop()
            a += max(first, last)
            li += min(first, last)
        if a > li:
            return True
        return False


class Solution:
    def stoneGame(self, piles) -> bool:
        length = len(piles)
        map = [[0] * length for i in range(length)]
        for i, num in enumerate(piles):
            map[i][i] = num
        for i in range(length-2, -1, -1):
            for j in range(i+1, length):
                map[i][j] = max(piles[i] - map[i+1][j], piles[j] - map[i][j-1])
        return map[0][length-1] > 0


class Solution:
    def stoneGame(self, piles) -> bool:
        length = len(piles)
        dp = [0] * length
        for i, num in enumerate(piles):
            dp[i] = num
        for i in range(length-2, -1, -1):
            for j in range(i+1, length):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j-1])
        return dp[length-1] > 0