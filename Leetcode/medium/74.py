class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        def binary_range(li, target):
            left = 0
            right = len(li) - 1
            while left < right:
                mid = (left+right+1)//2
                if li[mid] > target:
                    right = mid - 1
                else:
                    left = mid
            return right if li[right] <= target else False

        def normal_binary(li, target):
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

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        else:
            first_col = [each[0] for each in matrix]
            row = binary_range(first_col, target)
            if not row is False:
                return normal_binary(matrix[row], target)
            return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 3
print(Solution().searchMatrix(matrix, target))

