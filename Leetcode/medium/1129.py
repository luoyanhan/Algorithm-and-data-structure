class Solution:
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        res = [0]
        if n == 1:
            return res
        from collections import defaultdict
        red_map = defaultdict(list)
        blue_map = defaultdict(list)
        for start, end in red_edges:
            red_map[start].append(end)
        for start, end in blue_edges:
            blue_map[start].append(end)
        for target in range(1, n):
            res.append(-1)
            path = [0]
            def dfs(target, pre, red):
                if (red and target in red_map[pre]) or (
                        not red and target in blue_map[pre]):
                    res[target] = min(res[target], len(path))
                elif red and target not in red_map[pre]:
                    for cur in red_map[pre]:
                        path.append(cur)
                        dfs(target, cur, not red)
                elif not red and target not in blue_map[pre]:
                    for cur in blue_map[pre]:
                        path.append(cur)
                        dfs(target, cur, not red)
                path.pop()
            dfs(target, 0, 1)
            dfs(target, 0, 0)
        return res




print(Solution().shortestAlternatingPaths())


