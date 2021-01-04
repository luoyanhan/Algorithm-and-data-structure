class Solution:
    def allPathsSourceTarget(self, graph):
        res = []
        target = len(graph) - 1
        if not graph:
            return res
        path = list()
        def dfs(idx, target):
            path.append(idx)
            if idx == target:
                res.append(path[:])
            else:
                for each in graph[idx]:
                    dfs(each, target)
            path.pop()
        dfs(0, target)
        return res


class Solution:
    def allPathsSourceTarget(self, graph):
        N = len(graph)
        def dfs(idx):
            if idx == N-1:
                return [[idx]]
            res = list()
            for nei_idx in graph[idx]:
                for each in dfs(nei_idx):
                    res.append([idx] + each)
            return res
        return dfs(0)


