class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return False
        length = len(nums)
        if length == 1:
            return True if nums[0] == target else False
        idx = 0
        for i in range(length-1):
            if nums[i+1] < nums[i]:
                idx = i+1
                break
        def binary(l, r):
            while r >= l:
                mid = (l+r)//2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return False

        a = binary(0, idx-1)
        if a:
            return a
        else:
            return binary(idx, length-1)


class Solution:
    def search(self, nums, target: int):
        if not nums:
            return False
        l, r = 0, len(nums)-1
        while r >= l:
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid]:
                l += 1
                continue
            #第一段无序
            if nums[mid] < nums[l]:
                if nums[mid] < target <= nums[len(nums)-1]:
                    l = mid+1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return False

print(Solution().search([1, 3, 1, 1, 1], 3))