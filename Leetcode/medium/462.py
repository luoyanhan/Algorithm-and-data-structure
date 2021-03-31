class Solution:
    def minMoves2(self, nums):
        length = len(nums)
        nums.sort()
        mid = nums[length//2]
        return sum([abs(num-mid) for num in nums])


class Solution:
    def minMoves2(self, nums):
        def partition(lo, hi):
            if lo == hi:
                return lo
            i, j = lo, hi
            while i < j:
                while i < j and nums[j] >= nums[lo]:
                    j -= 1
                while i < j and nums[i] <= nums[lo]:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[lo], nums[i] = nums[i], nums[lo]
            return i
        def find_idx(target):
            length = len(nums)
            i, j = 0, length-1
            while i <= j:
                idx = partition(i, j)
                if idx == target:
                    return nums[idx]
                elif idx < target:
                    i = idx + 1
                else:
                    j = idx - 1
            return -1

        mid = find_idx(len(nums)//2)
        return sum([abs(num - mid) for num in nums])


class Solution:  #超时
    def minMoves2(self, nums):
        def partition(lo, hi):
            if lo == hi:
                return lo
            i = lo
            for j in range(lo, hi+1):
                if nums[j] < nums[hi]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[hi], nums[i] = nums[i], nums[hi]
            return i
        def find_idx(target):
            length = len(nums)
            i, j = 0, length-1
            while i <= j:
                idx = partition(i, j)
                if idx == target:
                    return nums[idx]
                elif idx < target:
                    i = idx + 1
                else:
                    j = idx - 1
            return -1

        mid = find_idx(len(nums)//2)
        return sum([abs(num - mid) for num in nums])


print(Solution().minMoves2([1, 2, 3]))


