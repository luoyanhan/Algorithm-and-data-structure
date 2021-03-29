class Solution:
    def subarraysDivByK(self, A, K):
        mapper = dict()
        mapper[0] = 1
        res = 0
        total = 0
        for num in A:
            total += num
            m = total % K
            same = mapper.get(m, 0)
            mapper[m] = same + 1
            res += same
        return res
