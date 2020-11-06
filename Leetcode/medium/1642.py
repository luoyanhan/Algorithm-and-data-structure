class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        height_difference = [0] + [max(0, heights[i] - heights[i-1]) for i in range(1, len(heights))]
        def check(idx):
            tmp = height_difference[:idx+1]
            if idx <= ladders:
                return True
            tmp.sort()
            #用tmp的长度减ladders而不是直接-ladders, 避免ladders为0的情况
            if sum(tmp[:idx+1-ladders]) <= bricks:
                return True
            return False
        left = 0
        right = len(heights) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if not check(mid):
                right = mid - 1
            else:
                left = mid
        return right



print(Solution().furthestBuilding( [4,12,2,7,3,18,20,3,19], 10, 2))
