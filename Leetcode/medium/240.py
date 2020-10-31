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




matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print(Solution().searchMatrix(matrix, 5))
