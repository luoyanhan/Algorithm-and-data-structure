class Solution:
    def shortestPathBinaryMatrix(self, grid):
        step = 1
        N = len(grid)
        now_points = list()
        if N == 1 and grid[0][0] == 0:
            return step
        if grid[0][0] == 0:
            grid[0][0] = 1
            now_points.append((0, 0))
        while now_points:
            step += 1
            next_points = list()
            for i, j in now_points:
                for x_off, y_off in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
                    x, y = i+x_off, j+y_off
                    if 0 <= x < N and 0 <= y < N and grid[x][y] == 0:
                        if x == N-1 and y == N-1:
                            return step
                        next_points.append((x, y))
                        grid[x][y] = 1
            now_points = next_points
        return -1