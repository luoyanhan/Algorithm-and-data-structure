class Solution:
    def findKthLargest(self, nums, k):
        def swap(nums, i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        def partition(nums, left, right):
            org_left = left
            org_right = right
            idx = nums[org_left]
            left += 1
            while left <= right:
                while left <= right and nums[right] <= idx:
                    right -= 1
                while left <= right and nums[left] >= idx:
                    left += 1
                if right < left:
                    break
                swap(nums, left, right)
            swap(nums, org_left, right)
            return right
        def quick_select():
            left = 0
            right = len(nums) - 1
            while True:
                pos = partition(nums, left, right)
                if pos == k-1:
                    return nums[pos]
                elif pos > k-1:
                    right = pos - 1
                else:
                    left = pos + 1
        return quick_select()


print(Solution().findKthLargest([3,2,1,5,6,4] , 2))

