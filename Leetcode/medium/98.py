# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def judge(root, low=-sys.float_info.max, up=sys.float_info.max):
            if not root:
                return True
            val = root.val
            if val <= low or val >= up:
                return False
            if not judge(root.left, low, val):
                return False
            if not judge(root.right, val, up):
                return False
            return True
        return judge(root)