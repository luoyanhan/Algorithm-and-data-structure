class Solution:
    def findMinArrowShots(self, points) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        res = 1
        first_end = points[0][1]
        for start, end in points:
            if start > first_end:
                res += 1
                first_end = end
        return res
