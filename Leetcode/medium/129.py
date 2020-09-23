# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        def inner(pre_sum, cur):
            nonlocal res
            now_sum = pre_sum * 10 + cur.val
            if not cur.left and not cur.right:
                res += now_sum
                return
            if cur.left:
                inner(now_sum, cur.left)
            if cur.right:
                inner(now_sum, cur.right)
        inner(0, root)
        return res


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        stack = [(root, root.val)]
        while stack:
            node, pre_sum = stack.pop()
            if not node.left and not node.right:
                res += pre_sum
            else:
                if node.right:
                    stack.append((node.right, node.right.val + 10 * pre_sum))
                if node.left:
                    stack.append((node.left, node.left.val + 10 * pre_sum))
        return res

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, pre_sum):
            if not root:
                return 0
            pre_sum = pre_sum * 10 + root.val
            if not root.left and not root.right:
                return pre_sum
            return dfs(root.left, pre_sum) + dfs(root.right, pre_sum)
        return dfs(root, 0)

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        stack = [(root, root.val)]
        while stack:
            node, pre = stack.pop(0)
            if not node.left and not node.right:
                res += pre
            else:
                if node.left:
                    stack.append((node.left, 10 * pre + node.left.val))
                if node.right:
                    stack.append((node.right, 10 * pre + node.right.val))
        return res
