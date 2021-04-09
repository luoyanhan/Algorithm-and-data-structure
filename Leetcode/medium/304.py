class NumMatrix:

    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0]) if matrix else 0
        self._summ = [[0 for j in range(n+1)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                self._summ[i][j+1] = self._summ[i][j] + matrix[i][j]


    def sumRegion(self, row1, col1, row2, col2):
        s = 0
        for i in range(row1, row2+1):
            s += self._summ[i][col2+1] - self._summ[i][col1]
        return s



class NumMatrix:

    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0]) if matrix else 0
        self._summ = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                self._summ[i+1][j+1] = self._summ[i][j+1] + self._summ[i+1][j] - self._summ[i][j] + matrix[i][j]


    def sumRegion(self, row1, col1, row2, col2):
        return self._summ[row2+1][col2+1] - self._summ[row1][col2+1] - self._summ[row2+1][col1] + self._summ[row1][col1]

