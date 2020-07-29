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


class Solution:
    def subsets(self, nums):
        n = len(nums)
        res = list()
        n_bit = 1 << n
        for i in range(2**n):
            bitmask = bin(i | n_bit)[3:]
            res.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        return res




print(Solution().subsets([1,2,3]))



