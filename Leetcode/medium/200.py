class Solution:
    def numIslands(self, grid) -> int:
        neighbours = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        if not grid:
            return 0
        width, height = len(grid), len(grid[0])
        res = 0
        for x in range(width):
            for y in range(height):
                if grid[x][y] == '1':
                    q = [(x, y)]
                    grid[x][y] = '0'
                    while q:
                        top = q.pop(0)
                        for i, j in neighbours:
                            t_x = i + top[0]
                            t_y = j + top[1]
                            if t_x >= 0 and t_x < width and t_y >= 0 and t_y < height and grid[t_x][t_y] == '1':
                                q.append((t_x, t_y))
                                grid[t_x][t_y] = '0'
                    res += 1
        return res