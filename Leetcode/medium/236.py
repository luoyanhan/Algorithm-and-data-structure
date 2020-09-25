# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def dfs(node, p, q):
            nonlocal res
            if not node:
                return False
            a = dfs(node.left, p, q)
            b = dfs(node.right, p, q)
            if (a and b) or ((node.val == p.val or node.val == q.val) and (a or b)):
                res = node
            return a or b or (node.val == p.val or node.val == q.val)
        dfs(root,p, q)
        return res


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        map = dict()
        def dfs(node):
            if node.left:
                map[node.left.val] = node
                dfs(node.left)
            if node.right:
                map[node.right.val] = node
                dfs(node.right)
        map[root.val] = None
        dfs(root)
        visited = dict()
        node = p
        while node:
            visited[node.val] = True
            node = map[node.val]
        node = q
        while node.val not in visited:
            node = map[node.val]
        return node

