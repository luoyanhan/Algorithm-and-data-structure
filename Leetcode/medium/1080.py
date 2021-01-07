# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sufficientSubset(self, root, limit):
        def post_order(node, cur_sum):
            if not node.left and not node.right:
                return cur_sum + node.val >= limit
            res_left = False
            res_right = False
            if node.left:
                res_left = post_order(node.left, cur_sum+node.val)
            if node.right:
                res_right = post_order(node.right, cur_sum+node.val)
            if not res_left:
                node.left = None
            if not res_right:
                node.right = None
            return res_left or res_right
        res_root = post_order(root, 0)
        if not res_root:
            return None
        return root
