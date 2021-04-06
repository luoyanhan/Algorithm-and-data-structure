# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root):
        res = list()
        if not root:
            return res
        li = [root]
        while li:
            tmp = list()
            bigest = li[0].val
            for node in li:
                bigest = max(node.val, bigest)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            res.append(bigest)
            li = tmp
        return res
