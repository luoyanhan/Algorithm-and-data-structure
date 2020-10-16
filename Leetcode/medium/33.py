class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1
        length = len(nums)
        if length == 1:
            return 0 if nums[0] == target else -1
        idx = 0
        for i in range(length-1):
            if nums[i+1] < nums[i]:
                idx = i+1
                break
        def binary(l, r):
            while r >= l:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        a = binary(0, idx-1)
        if a != -1:
            return a
        else:
            return binary(idx, length-1)


class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        while r >= l:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            if nums[mid] >= nums[0]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[len(nums)-1] >= target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

