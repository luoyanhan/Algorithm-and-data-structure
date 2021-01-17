class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        map = [[0 for j in range(n)] for i in range(n)]
        for i in range(len(edges)):
            a, b = edges[i]
            weight = succProb[i]
            map[a][b] = weight
            map[b][a] = weight
        dist = [0 for _ in range(n)]
        S = {start}
        U = set()
        for each in range(n):
            if each != start:
                U.add(each)
