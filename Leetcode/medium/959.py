class Solution:
    def regionsBySlashes(self, grid):
        length = len(grid)
        graph = [i for i in range(length*length*4)]
        def find(i):
            if graph[i] != i:
                graph[i] = find(graph[i])
            return graph[i]
        def union(i, j):
            father_i = find(i)
            father_j = find(j)
            graph[father_i] = father_j
        for row in range(length):
            for col, value in enumerate(grid[row]):
                root = (row*length + col) * 4
                if value in "/ ":
                    union(root+0, root+3)
                    union(root+1, root+2)
                if value in "\ ":
                    union(root+0, root+1)
                    union(root+2, root+3)
                if row < length-1:
                    union(root+2, root+length*4)
                if col < length-1:
                    union(root+1, root+4+3)
        res = 0
        for i in range(length*length*4):
            if find(i) == i:
                res += 1
        return res


print(Solution().regionsBySlashes([" /","/ "]))
