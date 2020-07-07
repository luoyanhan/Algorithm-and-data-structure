class Solution:
    def closedIsland(self, grid) -> int:
        neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        width, height = len(grid), len(grid[0])
        result = 0
        for x in range(width):
            for y in range(height):
                if grid[x][y] == 0:
                    stack = list()
                    stack.append((x, y))
                    grid[x][y] = 1
                    flag = False
                    while stack:
                        top = stack.pop()
                        if top[0] in [0, width-1] or top[1] in [0, height-1]:
                            flag = True
                        for neighbour in neighbours:
                            i = top[0] + neighbour[0]
                            j = top[1] + neighbour[1]
                            if i < width and i >=0 and j < height and j >= 0 and grid[i][j] == 0:
                                stack.append((i, j))
                                grid[i][j] = 1
                    if not flag:
                        result += 1
        return result