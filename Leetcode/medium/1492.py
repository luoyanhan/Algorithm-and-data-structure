class Solution:
    def kthFactor(self, n, k):
        i = 1
        cnt = 0
        while i * i <= n:
            if n % i == 0:
                cnt += 1
                if cnt == k:
                    return i
            i += 1
        i -= 1
        if i * i == n:
            i -= 1
        while i > 0:
            if n % i == 0:
                cnt += 1
                if cnt == k:
                    return n // i
            i -= 1
        return -1