class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def binary_range(li, target):
            left = 0
            right = len(li) - 1
            while left < right:
                mid = (left + right + 1) // 2
                if li[mid] > target:
                    right = mid - 1
                else:
                    left = mid
            return right if li[right] <= target else False

        def binary(li, target):
            left = 0
            right = len(li) - 1
            while left <= right:
                mid = (left + right) // 2
                if li[mid] == target:
                    return True
                elif li[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        last_col = [row[-1] for row in matrix]
        row_idx = binary_range(last_col, target)
        print(row_idx)

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Solution().searchMatrix(matrix, 5)