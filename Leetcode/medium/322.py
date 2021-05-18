from functools import lru_cache


class Solution:
    def coinChange(self, coins, amount):
        @lru_cache(maxsize=amount)
        def dfs(remain):
            if remain < 0:
                return -1
            if remain == 0:
                return 0
            min_res = 10 ** 4 + 1
            for coin in coins:
                res = dfs(remain - coin)
                if 0 <= res < min_res:
                    min_res = res + 1
            return min_res if min_res < 10 ** 4 + 1 else -1

        return dfs(amount)


class Solution:
    def coinChange(self, coins, amount):
        mapper = dict()

        def dfs(remain):
            if remain in mapper:
                return mapper[remain]
            if remain < 0:
                inner_res = -1
            elif remain == 0:
                inner_res = 0
            else:
                min_res = 10 ** 4 + 1
                for coin in coins:
                    res = dfs(remain - coin)
                    if 0 <= res < min_res:
                        min_res = res + 1
                inner_res = min_res if min_res < 10 ** 4 + 1 else -1
            mapper[remain] = inner_res
            return inner_res

        return dfs(amount)


class Solution:
    def coinChange(self, coins, amount):
        dp = [-1 for _ in range(amount + 1)]
        dp[0] = 0
        for num in range(1, amount + 1):
            for coin in coins:
                if 0 <= num - coin < amount + 1 and dp[num - coin] != -1:
                    dp[num] = min(dp[num], dp[num - coin] + 1) if dp[
                                                                      num] != -1 else \
                    dp[num - coin] + 1
        return dp[amount]


class Solution:
    def coinChange(self, coins, amount):
        dp = [10 ** 4 + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for coin in coins:
            for num in range(coin, amount + 1):
                dp[num] = min(dp[num], dp[num - coin] + 1)
        return dp[amount] if dp[amount] < 10 ** 4 + 1 else -1
