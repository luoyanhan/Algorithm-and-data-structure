# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode):
        res = list()
        q = list()
        lastvisited = root
        while root or q:
            while root:
                q.append(root)
                root = root.left
            root = q[-1]
            if not root.right or lastvisited == root.right:
                root = q.pop()
                lastvisited = root
                res.append(root.val)
                root = None
            else:
                root = root.right
        return res

class Solution:
    def postorderTraversal(self, root: TreeNode):
        res = list()
        if not root:
            return res
        stack = [root]
        while stack:
            top = stack.pop()
            res.append(top.val)
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)
        return res[::-1]

