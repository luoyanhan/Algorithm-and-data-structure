# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#DFS
class Solution:
    def pathSum(self, root, sum):
        def is_leaf(node):
            return not node.left and not node.right
        res = list()
        path = list()
        def dfs(node, remain):
            if not node:
                return
            path.append(node.val)
            remain -= node.val
            if remain == 0 and is_leaf(node):
                res.append(path[:])
            dfs(node.left, remain)
            dfs(node.right, remain)
            path.pop()
        dfs(root, sum)
        return res

#BFS
class Solution:
    def pathSum(self, root, sum):
        res = list()
        def is_leaf(node):
            return not node.left and not node.right
        def get_path(node):
            path = [node.val]
            while node in father_map:
                node = father_map[node]
                path.append(node.val)
            res.append(path[::-1])
        if not root:
            return res
        q = [root]
        costs = [0]
        father_map = dict()
        while q:
            node = q.pop(0)
            pre_cost = costs.pop(0)
            if is_leaf(node):
                if pre_cost + node.val == sum:
                    get_path(node)
            else:
                if node.left:
                    q.append(node.left)
                    father_map[node.left] = node
                    costs.append(pre_cost + node.val)
                if node.right:
                    q.append(node.right)
                    father_map[node.right] = node
                    costs.append(pre_cost + node.val)
        return res





