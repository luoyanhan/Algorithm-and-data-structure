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
        print(red_map, blue_map)
        for target in range(1, n):
            depth = 0
            find_tag = False
            q = [-1] + [0]
            red = True
            while q:
                if depth >= n:
                    break
                head = q.pop(0)
                if head == -1:
                    if not q:
                        break
                    q.append(-1)
                    depth += 1
                    continue
                if not red:
                    next_li = blue_map[head]
                else:
                    next_li = red_map[head]
                red = not red
                if target in next_li:
                    find_tag = True
                    break
                else:
                    q += next_li
            res.append(depth) if find_tag else res.append(-1)
        return res




print(Solution().shortestAlternatingPaths(5, [[0,1],[1,2],[2,3],[3,4]], [[1,2],[2,3],[3,1]]))


