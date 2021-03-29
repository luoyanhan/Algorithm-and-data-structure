class Solution:
    def subarraySum(self, nums, k):
        mapper = dict()
        mapper[0] = 1
        res = 0
        total = 0
        for num in nums:
            total += num
            res += mapper.get(total-k, 0)
            mapper[total] = mapper.get(total, 0) + 1
        return res