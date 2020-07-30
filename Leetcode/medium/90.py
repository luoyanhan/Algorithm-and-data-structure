class Solution:
    def subsetsWithDup(self, nums):
        n = len(nums)
        res = list()
        path = list()
        def trackback(idx):
            res.append(path[:])
            if idx == n:
                return
            for i in range(idx, n):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                trackback(i+1)
                path.pop()
        nums.sort()
        trackback(0)
        return res


print(Solution().subsetsWithDup([4,4,4,1,4]))