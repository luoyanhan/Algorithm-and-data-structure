class Solution:
    def countServers(self, grid):
        width, height = len(grid), len(grid[0])
        count_x = [0] * width
        count_y = [0] * height
        for x in range(width):
            for y in range(height):
                if grid[x][y]:
                    count_x[x] += 1
                    count_y[y] += 1
        res = 0
        for x in range(width):
            for y in range(height):
                if grid[x][y] and (count_x[x] > 1 or count_y[y] > 1):
                    res += 1
        return res
