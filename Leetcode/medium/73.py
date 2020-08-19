class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        is_col = False
        for i in range(rows):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, rows):
            for j in range(1, cols):
                if not matrix[0][j] or not matrix[i][0]:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(cols):
                matrix[0][j] = 0
        if is_col:
            for i in range(rows):
                matrix[i][0] = 0




