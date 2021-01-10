class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        res = 0
        def dfs(i, j, cur_sum):
            nonlocal res
            if cur_sum > N:
                return
            if i < 0 or i > m-1 or j < 0 or j > n-1:
                res += 1
                return
            dfs(i-1, j, cur_sum+1)
            dfs(i+1, j, cur_sum+1)
            dfs(i, j-1, cur_sum+1)
            dfs(i, j+1, cur_sum+1)
        dfs(i, j, 0)
        return res % (10**9 + 7)

class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        res = 0
        if N == 0:
            return res
        store_map = [[[0 for c in range(n+2)] for r in range(m+2)] for k in range(N+1)]
        for r in range(m+2):
            store_map[0][r][0] = 1
            store_map[0][r][n+1] = 1
        for c in range(n+2):
            store_map[0][0][c] = 1
            store_map[0][m+1][c] = 1
        for k in range(1, N+1):
            for r in range(1, m+1):
                for c in range(1, n+1):
                    store_map[k][r][c] = (store_map[k-1][r][c-1] + store_map[k-1][r][c+1] + store_map[k-1][r-1][c] +
                                         store_map[k-1][r+1][c]) % 1000000007
        for k in range(1, N+1):
            res += store_map[k][i+1][j+1]
            res %= 1000000007
        return res


print(Solution().findPaths(2,2,2,0,0))