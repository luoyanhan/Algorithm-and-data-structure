class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        max_side = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    max_side = max(max_side, 1)
                    cur_max = min(rows-i, cols-j)
                    for k in range(1, cur_max):
                        if matrix[i+k][j+k] == '0':
                            break
                        tag = True
                        for m in range(k):
                            if matrix[i+k][j+m] == '0' or matrix[i+m][j+k] == '0':
                                tag = False
                                break
                        if tag:
                            max_side = max(max_side, k+1)
                        else:
                            break
        return max_side * max_side



class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        max_side = 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    max_side = max(dp[i][j], max_side)
        return max_side ** 2