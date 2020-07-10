class Solution:
    def networkDelayTime(self, times, N: int, K: int) -> int:
        import collections
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        dist = {node: float('inf') for node in range(1, N+1)}

        def dfs(node, distance):
            if distance >= dist[node]: return
            dist[node] = distance
            for v, w in sorted(graph[node]):
                dfs(v, w+distance)

        dfs(K, 0)
        res = max(dist.values())
        return res if res < float('inf') else -1




class Solution2:
    def networkDelayTime(self, times, N: int, K: int) -> int:
        graph = {node: list() for node in range(1, N+1)}
        for u, v, w in times:
            graph[u].append((v, w))
        dist = {node: float('inf') for node in range(1, N+1)}
        dist[K] = 0
        seen = [False] * (N+1)
        while True:
            target_node = -1
            target_dis = float('inf')
            for i in range(1, N+1):
                if not seen[i] and dist[i] < target_dis:
                    target_dis = dist[i]
                    target_node = i
            if target_node == -1: break
            seen[target_node] = True
            for v, w in graph[target_node]:
                dist[v] = min(dist[v], dist[target_node] + w)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1


class Solution3:
    def networkDelayTime(self, times, N: int, K: int) -> int:
        import heapq
        graph = {node:list() for node in range(1, N+1)}
        for u, v, w in times:
            graph[u].append((v, w))
        dist = dict()
        heap = [(0, K)]
        while heap:
            w1, node = heapq.heappop(heap)
            if node in dist: continue
            dist[node] = w1
            for v, w2 in graph[node]:
                if v not in dist:
                    heapq.heappush(heap, (w1 + w2, v))
        res = max(dist.values())
        return res if len(dist) == N else -1










