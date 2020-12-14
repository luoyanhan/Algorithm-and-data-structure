#超时
class Solution:
    def minCostConnectPoints(self, points) -> int:
        length = len(points)
        from collections import defaultdict
        graph = defaultdict(dict)
        for i in range(length):
            for j in range(length):
                graph[i][j] = (abs(points[i][0]-points[j][0]) +
                                abs(points[i][1]-points[j][1]))
        visited = {0}
        unvisited = {i for i in range(1, length)}
        res = 0
        while unvisited:
            min_weight = float('inf')
            start = None
            for each_unvisited in unvisited:
                for each_visited in visited:
                    if graph[each_unvisited][each_visited] < min_weight:
                        min_weight = graph[each_unvisited][each_visited]
                        start = each_unvisited
            res += min_weight
            visited.add(start)
            unvisited.remove(start)
        return res


#Prime 方法
class Solution:
    def minCostConnectPoints(self, points) -> int:
        unvisited = {(x, y): float('inf') for x, y in points}
        visited = [unvisited.popitem()[0]]
        res = 0
        while unvisited:
            for (x, y), weight in unvisited.items():
                i, j = visited[-1]
                dist = abs(x-i) + abs(y-j)
                unvisited[(x, y)] = min(weight, dist)
            (x, y), weight = min(unvisited.items(), key=lambda x: x[1])
            res += weight
            del unvisited[(x, y)]
            visited.append((x, y))
        return res





print(Solution().minCostConnectPoints())


