class Solution:
    def pacificAtlantic(self, matrix):
        if not matrix:
            return set()
        row, col = len(matrix), len(matrix[0])
        in_pa = set()
        in_atl = set()
        visited = set()
        def in_area(i, j):
            return 0 <= i < row and 0 <= j < col
        def dfs(x, y, tag):
            visited.add((x, y))
            if tag:
                in_pa.add((x, y))
            else:
                in_atl.add((x, y))
            neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for off_x, off_y in neighbours:
                loc = (x+off_x, y+off_y)
                if in_area(loc[0], loc[1]) and matrix[loc[0]][loc[1]] >= matrix[x][y] and loc not in visited:
                    dfs(loc[0], loc[1], tag)
        for j in range(col):
            dfs(0, j, True)
        for i in range(1, row):
            dfs(i, 0, True)
        visited = set()
        for j in range(col-1):
            dfs(row-1, j, False)
        for i in range(row):
            dfs(i, col-1, False)
        return in_pa & in_atl

