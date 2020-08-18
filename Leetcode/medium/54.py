class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return list()
        res = list()
        rows, cols = len(matrix), len(matrix[0])
        visited = [[False]*cols for i in range(rows)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction_index = 0
        x, y = 0, 0
        for i in range(rows*cols):
            res.append(matrix[x][y])
            visited[x][y] = True
            next_x = x + directions[direction_index][0]
            next_y = y + directions[direction_index][1]
            if not(rows > next_x >= 0 and cols > next_y >= 0 and not visited[next_x][next_y]):
                direction_index = (direction_index+1) % 4
            x += directions[direction_index][0]
            y += directions[direction_index][1]
        return res