class Solution:
    def permuteUnique(self, nums):
        res = list()
        path = list()
        length = len(nums)
        used = [False]*length
        nums.sort()
        def dfs(count, used):
            if count == length:
                res.append(path[:])
                return
            for i in range(length):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue
                    path.append(nums[i])
                    used[i] = True
                    dfs(count + 1, used)
                    path.pop()
                    used[i] = False
        dfs(0, used)
        return res

print(Solution().permuteUnique([2,2,1,1]))