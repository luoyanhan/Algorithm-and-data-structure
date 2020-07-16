class Solution:
    def findRedundantConnection(self, edges): # union_find set
        father = [i for i in range(len(edges)+1)]

        def find_father(node, father):
            while node != father[node]:
                node = father[node]
            return node

        def union(node1, node2):
            x = find_father(node1, father)
            y = find_father(node2, father)
            if x == y:
                return False
            father[x] = y
            return True

        for start, end in edges:
            if not union(start, end):
                return [start, end]

class Solution:
    def findRedundantConnection(self, edges): #dfs
        def dfs(node, visited, pre, graph):
            if visited[node]:
                return False
            visited[node] = True
            for each in graph[node]:
                if each != pre:
                    if not dfs(each, visited, node, graph):
                        return False
            return True

        graph = {node: [] for node in range(1, len(edges)+1)}
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            visited = [False] * (len(edges)+1)
            if not dfs(start, visited, -1, graph):
                return [start, end]





