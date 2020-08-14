# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return list()
        res = list()
        stack = [root]
        left = True
        while stack:
            next_level = list()
            tmp = list()
            if left:
                for i in range(len(stack)):
                    top = stack.pop()
                    tmp.append(top.val)
                    if top.left:
                        next_level.append(top.left)
                    if top.right:
                        next_level.append(top.right)
                left = False
            else:
                for i in range(len(stack)):
                    top = stack.pop()
                    tmp.append(top.val)
                    if top.right:
                        next_level.append(top.right)
                    if top.left:
                        next_level.append(top.left)
                left = True
            stack = next_level
            res.append(tmp)
        return res