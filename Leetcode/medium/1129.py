class Solution:
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        dist = [[0, 0]] + [[-1, -1] for _ in range(n-1)]  #red第一个, blue第二个
        from collections import defaultdict
        red_map = defaultdict(list)
        blue_map = defaultdict(list)
        for start, end in red_edges:
            red_map[start].append(end)
        for start, end in blue_edges:
            blue_map[start].append(end)
        now_should_red = [0]
        now_should_blue = [0]
        step = 0
        while now_should_red or now_should_blue:
            step += 1
            new_should_red = list()
            new_should_blue = list()
            if now_should_red:
                for point in now_should_red:
                    for each in red_map[point]:
                        if dist[each][0] == -1:
                            dist[each][0] = step
                            new_should_blue.append(each)
            if now_should_blue:
                for point in now_should_blue:
                    for each in blue_map[point]:
                        if dist[each][1] == -1:
                            dist[each][1] = step
                            new_should_red.append(each)
            now_should_red, now_should_blue = new_should_red, new_should_blue
        res = list()
        for fir, sec in dist:
            if fir == -1 and sec == -1:
                res.append(-1)
            elif fir == -1:
                res.append(sec)
            elif sec == -1:
                res.append(fir)
            else:
                res.append(min(fir, sec))
        return res




print(Solution().shortestAlternatingPaths(5, [[0,1],[1,2],[2,3],[3,4]], [[1,2],[2,3],[3,1]]))
print(Solution().shortestAlternatingPaths(5, [[3,2],[4,1],[1,4],[2,4]], [[2,3],[0,4],[4,3],[4,4],[4,0],[1,0]]))

print(Solution().shortestAlternatingPaths(5, [[2,0],[4,3],[4,4],[3,0],[1,4]], [[2,1],[4,3],[3,1],[3,0],[1,1],[2,0],[0,3],[3,3],[2,3]]))


