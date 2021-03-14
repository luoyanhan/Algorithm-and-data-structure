class Solution:
    def canPartition(self, nums):
        target, rest = divmod(sum(nums), 2)
        length = len(nums)
        if length <= 1 or rest:
            return False
        max_num = max(nums)
        if max_num > target:
            return False
        dp = [[False for j in range(target+1)] for i in range(length)]
        dp[0][nums[0]] = True
        for i in range(length):
            dp[i][0] = True
        for i in range(1, length):
            for j in range(1, target+1):
                if nums[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-nums[i]] | dp[i-1][j]
        return dp[length-1][target]


class Solution:
    def canPartition(self, nums):
        target, rest = divmod(sum(nums), 2)
        length = len(nums)
        if length <= 1 or rest:
            return False
        max_num = max(nums)
        if max_num > target:
            return False
        dp = [False for j in range(target+1)]
        dp[0] = True
        for i in range(length):
            for j in range(target, nums[i]-1, -1):
                dp[j] = dp[j-nums[i]] | dp[j]
        return dp[target]

class Solution:
    def canPartition(self, nums):
        target, rest = divmod(sum(nums), 2)
        if rest:
            return False
        sums = {0}
        for num in nums:
            tmp = {s+num for s in sums}
            if target in tmp:
                return True
            sums = sums | tmp
        return False



print(Solution().canPartition([1,5,11,5]))