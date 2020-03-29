class Solution:
    def maxDistance(self, grid):
        n = len(grid)
        queue = [(i, j) for i in range(n) for j in range(n) if grid[i][j]]
        if len(queue) == n*n or not queue:
            return -1
        step = 0
        while queue:
            temp = list()
            for i, j in queue:
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if n > x >= 0 and n > y >= 0 and not grid[x][y]:
                        temp.append((x, y))
                        grid[x][y] = 1
            queue = temp
            step += 1
        return step - 1

exa = [[1,0,1],[0,0,0],[1,0,1]]
print(Solution().maxDistance(exa))


