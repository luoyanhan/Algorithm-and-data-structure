class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        length = len(nums)
        dp = [1 for _ in range(length)]

        max_val = dp[0]
        max_size = 1
        for i in range(1, length):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j]+1)

            if dp[i] > max_size:
                max_size = dp[i]
                max_val = nums[i]

        res = list()
        if max_size == 1:
            return [nums[0]]

        idx = length-1
        while idx >= 0 and max_size > 0:
            if dp[idx] == max_size and max_val % nums[idx]==0:
                res.append(nums[idx])
                max_val = nums[idx]
                max_size -= 1
            idx -= 1
        return res








