#暴力1
class Solution:
    def numberOfArithmeticSlices(self, nums):
        length = len(nums)
        total = 0
        for i in range(length-2):
            d = nums[i+1] - nums[i]
            for j in range(i+2, length):
                tag = True
                for k in range(i, j):
                    if not nums[k+1] - nums[k] == d:
                        tag = False
                        break
                if tag:
                    total += 1
        return total

#暴力2
class Solution:
    def numberOfArithmeticSlices(self, nums):
        length = len(nums)
        total = 0
        for i in range(length-2):
            d = nums[i+1] - nums[i]
            for j in range(i+2, length):
                if nums[j] - nums[j-1] != d:
                    break
                total += 1
        return total


#递归
class Solution:
    def numberOfArithmeticSlices(self, nums):
        length = len(nums)
        total = 0
        def inner(idx):
            nonlocal total
            if idx < 2:
                return 0
            ap = 0
            if nums[idx] - nums[idx-1] == nums[idx-1] - nums[idx-2]:
                ap = 1 + inner(idx-1)
                total += ap
            else:
                inner(idx-1)
            return ap
        inner(length-1)
        return total


#动态规划
class Solution:
    def numberOfArithmeticSlices(self, nums):
        length = len(nums)
        total = 0
        dp = [0 for _ in range(length)]
        for i in range(2, length):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
                total += dp[i]
        return total

#动态规划 常数空间
class Solution:
    def numberOfArithmeticSlices(self, nums):
        length = len(nums)
        total = 0
        dp = 0
        for i in range(2, length):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp += 1
                total += dp
            else:
                dp = 0
        return total


print(Solution().numberOfArithmeticSlices([1,2,3,8,9,10]))