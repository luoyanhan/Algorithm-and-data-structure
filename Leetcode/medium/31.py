class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        left = 0
        for i in range(length-1, 0, -1):
            if nums[i-1] < nums[i]:
                left = i-1
                break
        right = left
        for each in range(left, length):
            if nums[each] > nums[left]:
                right = each
            elif nums[each] < nums[left]:
                break
            else:
                continue
        if left != right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            i = left + 1
        else:
            i = left
        j = length - 1
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1




