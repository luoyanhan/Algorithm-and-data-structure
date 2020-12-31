class Solution:   #并查集
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        graph = dict()
        for i in range(m):
            for j in range(n):
                node = i * n + j
                for x, y in [(i+1, j), (i, j+1)]:
                    if 0 <= x < m and 0 <= y < n:
                        graph[(node, x*n+y)] = abs(heights[i][j] - heights[x][y])
        roads = list(graph.items())
        roads.sort(key=lambda x: x[1])
        father_map = [i for i in range(m*n)]
        def find(node):
            if father_map[node] != node:
                father_map[node] = find(father_map[node])
            return father_map[node]
        def union(node1, node2):
            father1 = find(node1)
            father2 = find(node2)
            if father1 != father2:
                father_map[father1] = father2
        for rode, weight in roads:
            start, end = rode
            union(start, end)
            if find(0) == find(m*n-1):
                return weight
        return 0


#二分查找
class Solution:
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        left, right = 0, 999999
        res = 0
        while left <= right:
            mid = (left+right)//2
            stack = [(0, 0)]
            visited = [False for _ in range(m*n)]
            while stack:
                i, j = stack.pop()
                for offset_x, offset_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x, y = i+offset_x, j+offset_y
                    if 0 <= x < m and 0 <= y < n and not visited[x*n+y] and abs(heights[i][j] - heights[x][y]) <= mid:
                        visited[x*n+y] = True
                        stack.append((x, y))
            if visited[m*n-1]:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res






print(Solution().minimumEffortPath([[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]]))