class Solution:
    def shipWithinDays(self, weights, D) -> int:
        # def check(one_time):
        #     idx = 0
        #     length = len(weights)
        #     for i in range(D):
        #         today = one_time
        #         while today > 0 and idx < length and today >= weights[idx]:
        #             today -= weights[idx]
        #             idx += 1
        #     return idx >= length
        #改进了check方法，降低时间复杂度
        def check(one_time):
            d = 1
            today = one_time
            for each in weights:
                if each > one_time:
                    return False
                elif each > today:
                    d += 1
                    today = one_time
                today -= each
            return d <= D
        left = min(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            if not check(mid):
                left = mid + 1
            else:
                right = mid
        return left


print(Solution().shipWithinDays( [3,2,2,4,1,4], 3))
