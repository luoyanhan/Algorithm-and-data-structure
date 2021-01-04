# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, sum):
        res = 0
        if not root:
            return res
        stack = [root]
        def dfs(node, total):
            nonlocal res
            if not node:
                return
            total += node.val
            if total == sum:
                res += 1
            dfs(node.left, total)
            dfs(node.right, total)
        while stack:
            node = stack.pop()
            dfs(node, 0)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res


class Solution:
    def pathSum(self, root, sum):
        res = 0
        if not root:
            return res
        def bfs(node):
            nonlocal res
            pre = [0]
            q = [node]
            while q:
                top = q.pop(0)
                cost = pre.pop(0) + top.val
                if cost == sum:
                    res += 1
                if top.left:
                    q.append(top.left)
                    pre.append(cost)
                if top.right:
                    q.append(top.right)
                    pre.append(cost)
        nodes = [root]
        while nodes:
            node = nodes.pop()
            bfs(node)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return res



class Solution:
    def pathSum(self, root, sum):
        if not root:
            return 0
        def count_path(node, total):
            if not node:
                return 0
            new_total = node.val + total
            res = 1 if new_total == sum else 0
            return res + count_path(node.left, new_total) + count_path(node.right, new_total)
        return count_path(root, 0) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)


class Solution:
    def pathSum(self, root, sum):
        pre_sum_count = {0: 1}

        def dfs(node, total_sum):
            res = 0
            if not node:
                return 0
            current_sum = total_sum + node.val
            res += pre_sum_count.get(current_sum-sum, 0)
            pre_sum_count[current_sum] = pre_sum_count.get(current_sum, 0) + 1
            res += dfs(node.left, current_sum)
            res += dfs(node.right, current_sum)
            pre_sum_count[current_sum] -= 1
            return res
        return dfs(root, 0)



