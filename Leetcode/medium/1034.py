class Solution:
    def colorBorder(self, grid, r0: int, c0: int, color: int):
        neighbors = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        rows = len(grid)
        cols = len(grid[0])
        visited = []
        stack = []
        result = []
        target = (r0, c0)
        origin_color = grid[r0][c0]

        def is_border(node):
            if node[0] in [0, rows - 1] or node[1] in [0, cols - 1]:
                return True
            for i, j in neighbors:
                if grid[node[0] + i][node[1] + j] != origin_color:
                    return True
        if is_border((r0, c0)):
            result.append((r0, c0))
        visited.append(target)
        stack.append(target)
        while stack:
            node = stack.pop()
            for i, j in neighbors:
                if node[0] + i >= 0 and node[0] + i < rows and node[1] + j >= 0 and node[1] + j < cols:
                    neighbor = (node[0] + i, node[1] + j)
                    if grid[neighbor[0]][neighbor[1]] == origin_color and neighbor not in visited:
                        visited.append(neighbor)
                        stack.append(node)
                        stack.append(neighbor)
                        if is_border(neighbor):
                            result.append(neighbor)
                        break
        for i, j in result:
            grid[i][j] = color
        return grid

Solution().colorBorder([[1,1,1],[1,1,1],[1,1,1]],1,1,2)

# [[1,1,1],
#  [1,1,1],
#  [1,1,1]]