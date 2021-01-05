# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root):
        res = 0
        def get_length(node):
            nonlocal res
            if not node:
                return 0
            left_length = get_length(node.left)
            right_length = get_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.val == node.left.val:
                left_arrow = left_length + 1
            if node.right and node.val == node.right.val:
                right_arrow = right_length + 1
            res = max(res, left_arrow+right_arrow)
            return max(left_arrow, right_arrow)
        get_length(root)
        return res
