from collections import defaultdict
class Solution:
    def numberOfBoomerangs(self, points):
        length = len(points)
        res = 0
        for i in range(length):
            map = defaultdict(int)
            for j in range(length):
                if i != j:
                    dis = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                    map[dis] += 1

            for each in map.values():
                res += each * (each-1)
        return res