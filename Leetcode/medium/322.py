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
