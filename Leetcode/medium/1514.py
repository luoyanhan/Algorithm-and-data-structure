class Solution:     #超时
    def maxProbability(self, n, edges, succProb, start, end):
        from collections import defaultdict
        map = defaultdict(dict)
        for i, (start_point, end_point) in enumerate(edges):
            map[start_point][end_point] = succProb[i]
            map[end_point][start_point] = succProb[i]
        unvisited = [i for i in range(n) if i != start]
        dist = [0 for _ in range(n)]
        for end_point in map[start]:
            dist[end_point] = map[start][end_point]
        while unvisited:
            li = [(dist[point], point) for point in unvisited]
            li.sort(key=lambda x: x[0])
            next_pro, next_point = li.pop()
            unvisited.remove(next_point)
            for each_point in map[next_point]:
                if each_point in unvisited:
                    pro_next_to_each = map[next_point][each_point]
                    if pro_next_to_each*next_pro > dist[each_point]:
                        dist[each_point] = pro_next_to_each*next_pro
        return dist[end]


class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        import heapq
        from collections import defaultdict
        map = defaultdict(dict)
        for i, (start_point, end_point) in enumerate(edges):
            map[start_point][end_point] = succProb[i]
            map[end_point][start_point] = succProb[i]
        dist = [0 for _ in range(n)]
        dist[start] = 1
        q = [(-1, start)]
        while q:
            next_pro, next_point = heapq.heappop(q)
            next_pro = -next_pro
            if next_pro >= dist[next_point]:
                for each_point in map[next_point]:
                    pro_next_to_each = map[next_point][each_point]
                    each_pro = pro_next_to_each*next_pro
                    if each_pro > dist[each_point]:
                        dist[each_point] = each_pro
                        heapq.heappush(q, (-each_pro, each_point))
        return dist[end]


print(Solution().maxProbability(5,
[[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]],
[0.37,0.17,0.93,0.23,0.39,0.04],
3, 4))
