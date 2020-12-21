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
            print(i, j)
            graph[father_i] = father_j
        for row in range(length):
            for col, value in enumerate(grid[row]):
                root = (row*length + col) * 4
                if value == "/":
                    union(root+0, root+3)
                    union(root+1, root+2)
                elif value == "\\":
                    union(root+0, root+1)
                    union(root+2, root+3)
                if row < length-1:
                    union(root+2, root+length*4)
                # if row > 0:
                #     union(root, root-4*length+2)
                if col < length-1:
                    union(root+1, root+4+3)
                # if col > 0:
                #     union(root+3, root-4+1)
        res = 0
        print(graph)
        for i in range(length*length*4):
            if find(i) == i:
                res += 1
        return res


# class DSU:
#     def __init__(self, N):
#         self.p = list(range(N))
#
#     def find(self, x):
#         if self.p[x] != x:
#             self.p[x] = self.find(self.p[x])
#         return self.p[x]
#
#     def union(self, x, y):
#         xr = self.find(x)
#         yr = self.find(y)
#         self.p[xr] = yr
#
# class Solution(object):
#     def regionsBySlashes(self, grid):
#         N = len(grid)
#         dsu = DSU(4 * N * N)
#         for r, row in enumerate(grid):
#             for c, val in enumerate(row):
#                 root = 4 * (r*N + c)
#                 if val in '/ ':
#                     dsu.union(root + 0, root + 1)
#                     dsu.union(root + 2, root + 3)
#                 if val in '\ ':
#                     dsu.union(root + 0, root + 2)
#                     dsu.union(root + 1, root + 3)
#
#                 # north/south
#                 if r+1 < N: dsu.union(root + 3, (root+4*N) + 0)
#                 # if r-1 >= 0: dsu.union(root + 0, (root-4*N) + 3)
#                 # east/west
#                 if c+1 < N: dsu.union(root + 2, (root+4) + 1)
#                 # if c-1 >= 0: dsu.union(root + 1, (root-4) + 2)
#         print(dsu.p)
#         return sum(dsu.find(x) == x for x in range(4*N*N))


print(Solution().regionsBySlashes([" /","/ "]))
