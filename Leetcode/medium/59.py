class Solution:
    def generateMatrix(self, n):
        matrix = [[0]*n for i in range(n)]
        left, right, top, bottom = 0, n-1, 0, n-1
        nums = [num for num in range(1, n**2+1)]
        while nums:
            for i in range(left, right+1):
                matrix[top][i] = nums.pop(0)
            for i in range(top+1, bottom+1):
                matrix[i][right] = nums.pop(0)
            if left < right and top < bottom:
                for i in range(right-1, left, -1):
                    matrix[bottom][i] = nums.pop(0)
                for i in range(bottom, top, -1):
                    matrix[i][left] = nums.pop(0)
            left, right, top, bottom = left+1, right-1, top+1, bottom-1
        return matrix
