class Solution:
    def smallestK(self, arr, k):
        def pattition(lo, hi):
            if lo >= hi:
                return lo
            i, j = lo, hi
            while i < j:
                while i < j and arr[j] >= arr[lo]:
                    j -= 1
                while i < j and arr[i] <= arr[lo]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[i], arr[lo] = arr[lo], arr[i]
            return i

        if not arr or k == 0:
            return list()

        left, right = 0, len(arr) - 1
        while left <= right:
            mid = pattition(left, right)
            if mid < k - 1:
                left = mid + 1
            elif mid > k - 1:
                right = mid - 1
            else:
                return arr[:k] if arr[:k] else list()


print(Solution().smallestK([1, 2, 3], 0))
