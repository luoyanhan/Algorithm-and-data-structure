class Solution:
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict
        graph = defaultdict(dict)
        for (start, end), weight in zip(equations, values):
            graph[start][end] = weight
            graph[end][start] = 1/weight
        def dfs(start, end, visited):
            visited.add(start)
            if start not in graph:
                return -1
            if start == end:
                return 1
            for each in graph[start]:
                if end == each:
                    return graph[start][end]
                elif each not in visited:
                    v = dfs(each, end, visited)
                    if v != -1:
                        return v*graph[start][each]
                    else:
                        pass
            return -1
        res = list()
        for start, end in queries:
            visited = set()
            res.append(dfs(start, end, visited))
        return res



res = Solution().calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
print(res)