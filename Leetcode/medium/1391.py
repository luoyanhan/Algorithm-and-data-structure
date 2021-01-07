class Solution:
    def hasValidPath(self, grid):
        if grid[0][0] == 5 or grid[-1][-1] == 4:
            return False
        m, n = len(grid), len(grid[0])
        father_map = [_ for _ in range(m*n*4)]
        def find_father(node):
            if father_map[node] != node:
                father_map[node] = find_father(father_map[node])
            return father_map[node]
        def union(node1, node2):
            father1 = find_father(node1)
            father2 = find_father(node2)
            if father1 != father2:
                father_map[father1] = father2
        for i in range(m):
            for j in range(n):
                root = (i*n+j) * 4
                if grid[i][j] == 1:
                    union(root, root + 2)
                elif grid[i][j] == 2:
                    union(root + 1, root + 3)
                elif grid[i][j] == 3:
                    union(root, root + 3)
                elif grid[i][j] == 4:
                    union(root + 2, root + 3)
                elif grid[i][j] == 5:
                    union(root, root + 1)
                elif grid[i][j] == 6:
                    union(root + 1, root + 2)
                if j < n-1:
                    union(root + 2, root + 4)
                if i < m-1:
                    union(root + 3, root + n*4 + 1)
        if grid[0][0] in [1, 3]:
            left = 0
        elif grid[0][0] in [2, 6]:
            left = 1
        else:
            left = 2
        if grid[-1][-1] in [1, 3, 5]:
            right = m*n*4-4
        elif grid[-1][-1] in [2, 6]:
            right = m * n * 4 - 3
        return find_father(left) == find_father(right)



class Solution:
    def hasValidPath(self, grid):
        rows, cols = len(grid), len(grid[0])
        father_map = [_ for _ in range(rows*cols)]
        def find_father(node):
            if father_map[node] != node:
                father_map[node] = find_father(father_map[node])
            return father_map[node]
        def union(node1, node2):
            father1 = find_father(node1)
            father2 = find_father(node2)
            father_map[father1] = father2

        for i in range(rows):
            for j in range(cols):
                node_idx = i*cols + j
                if grid[i][j] == 1:
                    if j > 0 and grid[i][j-1] in [1, 4, 6]:
                        union(node_idx, node_idx-1)
                    if j+1 < cols and grid[i][j + 1] in [1, 3, 5]:
                        union(node_idx, node_idx + 1)
                elif grid[i][j] == 2:
                    if i > 0 and grid[i-1][j] in [2, 3, 4]:
                        union(node_idx, node_idx - cols)
                    if i+1 < rows and grid[i + 1][j] in [2, 5, 6]:
                        union(node_idx, node_idx + cols)
                elif grid[i][j] == 3:
                    if j > 0 and grid[i][j - 1] in [1, 4, 6]:
                        union(node_idx, node_idx - 1)
                    if i + 1 < rows and grid[i + 1][j] in [2, 5, 6]:
                        union(node_idx, node_idx + cols)
                elif grid[i][j] == 4:
                    if j + 1 < cols and grid[i][j + 1] in [1, 3, 5]:
                        union(node_idx, node_idx + 1)
                    if i + 1 < rows and grid[i + 1][j] in [2, 5, 6]:
                        union(node_idx, node_idx + cols)
                elif grid[i][j] == 5:
                    if j > 0 and grid[i][j - 1] in [1, 4, 6]:
                        union(node_idx, node_idx - 1)
                    if i > 0 and grid[i - 1][j] in [2, 3, 4]:
                        union(node_idx, node_idx - cols)
                elif grid[i][j] == 6:
                    if j + 1 < cols and grid[i][j + 1] in [1, 3, 5]:
                        union(node_idx, node_idx + 1)
                    if i > 0 and grid[i - 1][j] in [2, 3, 4]:
                        union(node_idx, node_idx - cols)
        return find_father(0) == find_father(rows*cols-1)


print(Solution().hasValidPath([[6,1,3],[4,1,5]]))