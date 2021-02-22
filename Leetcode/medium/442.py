class Solution:
    def findDuplicates(self, nums):
        res = list()
        nums.sort()
        length = len(nums)
        i = 1
        while i < length:
            if nums[i] == nums[i-1]:
                res.append(nums[i])
            i += 1
        return res



class Solution:
    def findDuplicates(self, nums):
        res = list()
        for num in nums:
            abs_num = abs(num)
            if nums[abs_num-1] < 0:
                res.append(abs_num)
            else:
                nums[abs_num-1] *= -1
        return res