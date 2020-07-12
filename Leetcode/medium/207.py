# class Solution:
#     def canFinish(self, numCourses: int, prerequisites):
#         input_dict = {node: 0 for node in range(numCourses)}
#         output_dict = {node: [] for node in range(numCourses)}
#         for end, start in prerequisites:
#             input_dict[end] += 1
#             output_dict[start].append(end)
#         q = list()
#         for node in input_dict:
#             if input_dict[node] == 0:
#                 q.append(node)
#         while q:
#             top = q.pop(0)
#             for each in output_dict[top]:
#                 input_dict[each] -= 1
#                 if input_dict[each] == 0:
#                     q.append(each)
#         return not max(input_dict.values())

class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        output_dict = {node: [] for node in range(numCourses)}
        tag_list = [0] * numCourses
        for end, start in prerequisites:
            output_dict[start].append(end)
        def dfs(node, tag_list, output_dict):
            if tag_list[node] == -1:
                return False
            if tag_list[node] == 1:
                return True
            tag_list[node] = -1
            for each in output_dict[node]:
                if not dfs(each, tag_list, output_dict):
                    return False
            tag_list[node] = 1
            return True
        for each in range(numCourses):
            if not dfs(each, tag_list, output_dict):
                return False
        return True



print(Solution().canFinish(2, [[1,0],[0,1]] ))
