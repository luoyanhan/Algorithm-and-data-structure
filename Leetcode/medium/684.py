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

# class Solution:
#     def findRedundantConnection(self, edges): #dfs
#         graph = {node: [] for node in range(1, len(edges)+1)}
#         for start, end in edges:
#             graph[start].append(end)
#             graph[end].append(start)
#         visited = [False] * len(edges)
#
#         def dfs(node, visited, pre, graph):
#             if visited[node]:
#                 return False
#             for each in graph[node]:
#                 if each != pre:
#                     if not dfs(each, visited, node, graph):
#                         return False
#             return True
#
#
#
#
# print(Solution().findRedundantConnection([[1,2],[1,3],[2,3]]))


