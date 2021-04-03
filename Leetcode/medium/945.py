class Solution:
    def minIncrementForUnique(self, A):
        res = 0
        taken = 0
        cnt = [0 for _ in range(80000)]
        for num in A:
            cnt[num] += 1
        for idx in range(80000):
            if cnt[idx] > 1:
                taken += cnt[idx] - 1
                res -= idx * (cnt[idx] - 1)
            elif taken > 0 and cnt[idx] == 0:
                taken -= 1
                res += idx
        return res


class Solution:
    def minIncrementForUnique(self, A):
        res = 0
        taken = 0
        A.append(100000)
        A.sort()
        for idx in range(1, len(A)):
            if A[idx] == A[idx-1]:
                taken += 1
                res -= A[idx]
            else:
                release = min(taken, A[idx] - A[idx-1] - 1)
                taken -= release
                res += A[idx-1]*release + (1+release)*release//2
        return res
