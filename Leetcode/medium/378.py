class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        def cnt_smaller_num(target):
            num = 0
            i = m - 1
            j = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= target:
                    j += 1
                    num += i + 1
                else:
                    i -= 1
            return num
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            mid = (left+right) // 2
            num = cnt_smaller_num(mid)
            if num < k:
                left = mid + 1
            else:
                right = mid
        return left