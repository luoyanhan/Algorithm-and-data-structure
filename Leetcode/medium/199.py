# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode):
        if not root:
            return list()
        stack = [root, None]
        res = list()
        while stack:
            cur = stack.pop(0)
            if not cur:
                if stack:
                    stack.append(cur)
                continue
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            if stack[0] == None:
                res.append(cur.val)
        return res


class Solution:
    def rightSideView(self, root: TreeNode):
        if not root:
            return list()
        d = dict()
        stack = [(root, 0)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            if node:
                if depth > max_depth:
                    max_depth = depth
                d.setdefault(depth, node.val)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return [d[depth] for depth in range(max_depth+1)]




