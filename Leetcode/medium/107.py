# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return list()
        res = list()
        pre = [root]
        while pre:
            next = list()
            v_li = list()
            for n in pre:
                v_li.append(n.val)
                if n.left:
                    next.append(n.left)
                if n.right:
                    next.append(n.right)
            res = [v_li] + res
            pre = next
        return res


