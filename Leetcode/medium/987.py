# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root):
        import collections
        visited = collections.defaultdict(lambda: collections.defaultdict(list))
        def dfs(node, x, y):
            if node:
                visited[x][y].append(node.val)
                dfs(node.left, x-1, y+1)
                dfs(node.right, x+1, y+1)
        dfs(root, 0, 0)
        res = list()
        for x in sorted(visited):
            tmp = list()
            for y in sorted(visited[x]):
                tmp.extend(sorted([val for val in visited[x][y]]))
            res.append(tmp)
        return res


