# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        pre_sum_count = {0: 1}
        def dfs(node, total):
            res = 0
            if not node:
                return res
            cur_sum = total + node.val
            res += pre_sum_count.get(cur_sum-sum, 0)
            pre_sum_count[cur_sum] = pre_sum_count.get(cur_sum, 0) + 1
            res += dfs(node.left, cur_sum)
            res += dfs(node.right, cur_sum)
            pre_sum_count[cur_sum] = pre_sum_count.get(cur_sum, 0) - 1
            return res
        return dfs(root, 0)


