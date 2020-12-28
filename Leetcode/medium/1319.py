class Solution:   #origin
    def makeConnected(self, n, connections):
        father_map = [i for i in range(n)]
        surplus = 0
        def find_father(node):
            if father_map[node] != node:
                father_map[node] = find_father(father_map[node])
            return father_map[node]
        for connection in connections:
            father1 = find_father(connection[0])
            father2 = find_father(connection[1])
            if father1 != father2:
                father_map[father1] = father2
            else:
                surplus += 1
        num_component = 0
        for each in range(n):
            if father_map[each] == each:
                num_component += 1
        if num_component-1 <= surplus:
            return num_component - 1
        return -1


class Solution:   #优化
    def makeConnected(self, n, connections):
        if len(connections) < n-1:
            return -1
        father_map = [i for i in range(n)]
        num_component = n
        def find_father(node):
            if father_map[node] != node:
                father_map[node] = find_father(father_map[node])
            return father_map[node]
        for connection in connections:
            father1 = find_father(connection[0])
            father2 = find_father(connection[1])
            if father1 != father2:
                father_map[father1] = father2
                num_component -= 1
        return num_component - 1

#按秩合并优化? DFS求连通分量？

print(Solution().makeConnected(4, [[0,1],[0,2],[1,2]]))

