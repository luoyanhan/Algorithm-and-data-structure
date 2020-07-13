
#DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        graph = {node: [] for node in range(numCourses)}
        visited = [0]*numCourses
        result = list()
        for end, pre in prerequisites:
            graph[pre].append(end)
        invalid = False
        def dfs(node):
            nonlocal invalid
            visited[node] = 1
            for each in graph[node]:
                if visited[each] == 0:
                    dfs(each)
                    if invalid:
                        return
                elif visited[each] == 1:
                    invalid = True
                    return
            visited[node] = 2
            result.append(node)
        for each in range(numCourses):
            if not invalid and not visited[each]:
                dfs(each)
        if invalid:
            return list()
        return result[::-1]




#BFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        res = list()
        q = list()
        input_dict = {node: 0 for node in range(numCourses)}
        graph = {node: []for node in range(numCourses)}
        for end, pre in prerequisites:
            input_dict[end] += 1
            graph[pre].append(end)
        for node in input_dict:
            if input_dict[node] == 0:
                q.append(node)
        while q:
            node = q.pop(0)
            res.append(node)
            for each in graph[node]:
                input_dict[each] -= 1
                if input_dict[each] == 0:
                    q.append(each)
        if sum(input_dict.values()) > 0:
            return list()
        return res