# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        path = list()
        res = list()
        def dfs(node, remain):
            if not node:
                return
            path.append(node.val)
            cur_remain = remain - node.val
            if not node.left and not node.right:
                if cur_remain == 0:
                    res.append(path[:])
            else:
                if node.left:
                    dfs(node.left, cur_remain)
                if node.right:
                    dfs(node.right, cur_remain)
            path.pop()
        dfs(root, sum)
        return res
