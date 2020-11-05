class Solution:
    def minEatingSpeed(self, piles, H):
        import math
        def check(k):
            hours = 0
            for each in piles:
                hours += math.ceil(each/k)
            return hours <= H

        left = math.ceil(sum(piles)/H)
        right = max(piles)
        while left <= right:
            mid = (left+right+1)//2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return right + 1



class Solution:
    def minEatingSpeed(self, piles, H):
        def check(k):
            hours = 0
            for each in piles:
                hours += each // k if each % k == 0 else each // k + 1
            return hours <= H
        left = 1
        right = max(piles)
        while left < right:
            mid = (left+right)//2
            if not check(mid):
                left = mid + 1
            else:
                right = mid
        return left


print(Solution().minEatingSpeed([30,11,23,4,20], 6))
