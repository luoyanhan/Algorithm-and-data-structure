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


#kruskal
class Solution:
    def minCostConnectPoints(self, points):
        MST = list()   #用来存储最小生成树路径， 答题不需要
        res = 0
        roads = list()
        num = 0
        length = len(points)
        father_map = {i: i for i in range(length)}   #用点在points数组的下标代替(x, y)形式，可以减少执行时间和空间
        def find_father(point_idx):
            if father_map[point_idx] != point_idx:
                father_map[point_idx] = find_father(father_map[point_idx])
            return father_map[point_idx]
        # def find_father(point_idx):
        #     while point_idx != father_map[point_idx]:
        #         point = father_map[point_idx]
        #     return father_map[point_idx]
        # def union(point1_idx, point2_idx):
        #     father1 = find_father(point1_idx)
        #     father2 = find_father(point2_idx)
        #     if father1 != father2:
        #         if father1 < father2:
        #             father_map[father1] = father2
        #         else:
        #             father_map[father2] = father1
        def union(point1_idx, point2_idx):
            father1 = find_father(point1_idx)
            father2 = find_father(point2_idx)
            if father1 != father2:
                father_map[father1] = father2
        for i in range(length):
            for j in range(i+1, length):
                point1 = points[i]
                point2 = points[j]
                roads.append(((i, j), abs(point1[0]-point2[0]) +
                              abs(point1[1]-point2[1])))
        roads.sort(key=lambda x: x[1])
        for each in roads:
            start_idx, end_idx = each[0]
            if find_father(start_idx) != find_father(end_idx):
                res += each[1]
                MST.append(each[0])
                num += 1
                if num == length - 1:
                    return res
                union(start_idx, end_idx)
        return res


print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))


