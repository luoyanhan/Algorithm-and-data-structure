class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def binary(start, target, is_row):
            if is_row:
                left = start
                right = n - 1
                li = matrix[left]
                while left <= right:
                    mid = (left + right) // 2
                    if li[mid] == target:
                        return True
                    elif li[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False
            else:
                left = start
                right = m - 1
                while left <= right:
                    mid = (left + right) // 2
                    if matrix[mid][start] == target:
                        return True
                    elif matrix[mid][start] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        for i in range(min(m, n)):
            if binary(i, target, True) or binary(i , target, False):
                return True
        return False


class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        i = 0
        j = n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False



class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        def inner(left, right, up, down):
            if left > right or up > down:
                return False
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False
            mid = (left + right) // 2
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            return inner(left, mid-1, row, down) or inner(mid+1, right, up, row-1)
        return inner(0, len(matrix[0])-1, 0, len(matrix)-1)



class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n-1]:
                for each in matrix[i]:
                    if each == target:
                        return True
        return False


class Solution:
    def searchMatrix(self, matrix, target):
        def binary(li, left, right, target):
            while left <= right:
                mid = (left+right)//2
                if li[mid] == target:
                    return True
                elif li[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        for each in matrix:
            if binary(each, 0, len(each)-1, target):
                return True
        return False




matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

print(Solution().searchMatrix(matrix, 5))

matrix = [[1,2,3,4,5],
          [6,7,8,9,10],
          [11,12,13,14,15],
          [16,17,18,19,20],
          [21,22,23,24,25]]
print(Solution().searchMatrix(matrix, 19))
