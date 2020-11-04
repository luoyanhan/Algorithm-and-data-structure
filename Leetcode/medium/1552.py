class Solution:
    def maxDistance(self, position, m) -> int:
        position.sort()
        def check(gap):
            pre = position[0]
            cnt = 1
            for i in range(1, len(position)):
                if position[i] - pre >= gap:
                    cnt += 1
                    pre = position[i]
            return cnt >= m
        left = 1
        right = position[-1] - position[0]
        while left <= right:
            mid = (left+right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1     #left 是新的最小边界，因此left-1是必定可以的
