class Solution:
    def findCircleNum(self, M) -> int:
        length = len(M)
        def dfs(i):
            M[i][i] = 2
            for j in range(length):
                if M[i][j] == 1 and M[j][j] != 2:
                    dfs(j)
        res = 0
        for i in range(length):
            if M[i][i] == 1:
                res += 1
                dfs(i)
        return res


class Solution:
    def findCircleNum(self, M) -> int:
        length = len(M)
        q = list()
        res = 0
        for i in range(length):
            if M[i][i] == 1:
                res += 1
                q.append(i)
                while q:
                    x = q.pop(0)
                    M[x][x] = 2
                    for j in range(length):
                        if M[j][j] != 2 and M[x][j] == 1:
                            q.append(j)
        return res


class Solution:
    def findCircleNum(self, M) -> int:
        length = len(M)
        parents = [-1 for i in range(length)]
        def find_parent(i):
            if parents[i] != -1:
                return find_parent(parents[i])
            else:
                return i
        def union(i, j):
            parent_i = find_parent(i)
            parent_j = find_parent(j)
            if parent_i != parent_j:
                parents[parent_j] = parent_i
        for i in range(length):
            for j in range(length):
                if M[i][j] == 1 and i != j:
                    union(i, j)
        return parents.count(-1)