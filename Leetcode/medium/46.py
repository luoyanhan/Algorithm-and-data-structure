class Solution:
    def permute(self, nums):
        res = list()
        def dfs(resident, tmp):
            if not resident:
                res.append(tmp)
                return
            for i in range(len(resident)):
                dfs(resident[:i]+resident[i+1:], tmp+[resident[i]])
        dfs(nums, list())
        return res

class Solution:
    def permute(self, nums):
        res = list()
        length = len(nums)
        def dfs(first=0):
            if first == length:
                res.append(nums[:])
                return
            for i in range(first, length):
                nums[i], nums[first] = nums[first], nums[i]
                dfs(first+1)
                nums[i], nums[first] = nums[first], nums[i]
        dfs()
        return res


print(Solution().permute([1,2,3]))

