# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder):
        idx = 0
        length = len(preorder)
        def helper(lower=float('-inf'), upper=float('inf')):
            nonlocal idx
            if idx == length:
                return None
            val = preorder[idx]
            if val > upper or val < lower:
                return None
            idx += 1
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root
        return helper()

class Solution:
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        for i in range(1, len(preorder)):
            node, child = stack[-1], TreeNode(preorder[i])
            while stack and child.val > stack[-1].val:
                node = stack.pop()
            if node.val < child.val:
                node.right = child
            else:
                node.left = child
            stack.append(child)
        return root


