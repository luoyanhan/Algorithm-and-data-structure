class Solution:
    def subsets(self, nums):
        res = list()
        path = list()
        l = len(nums)
        def trackback(length, k, pre_index):
            if length == k:
                res.append(path[:])
                return
            for i in range(pre_index, l):
                path.append(nums[i])
                trackback(length+1, k, i+1)
                path.pop()
        for i in range(l+1):
            trackback(0, i, 0)
        return res




print(Solution().subsets([1,2,3]))



