class Solution:
    def fourSumCount(self, A, B, C, D) -> int:
        sum1 = dict()
        for a in A:
            for b in B:
                if a+b in sum1:
                    sum1[a+b] += 1
                else:
                    sum1[a+b] = 1
        res = 0
        for c in C:
            for d in D:
                if -(c+d) in sum1:
                    res += sum1[-(c+d)]
        return res
