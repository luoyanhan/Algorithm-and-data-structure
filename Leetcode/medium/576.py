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



print(Solution().findPaths(2,2,2,0,0))