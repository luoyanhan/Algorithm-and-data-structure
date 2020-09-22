# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre_list = list()
        stack = list()
        node = root
        while node or stack:
            while node:
                pre_list.append(node)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        for i in range(1, len(pre_list)):
            pre, next = pre_list[i-1], pre_list[i]
            pre.left = None
            pre.right = next


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        stack = [root]
        pre = None
        while stack:
            cur = stack.pop()
            if pre:
                pre.left = None
                pre.right = cur
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            pre = cur

class Solution:
    def flatten(self, root: TreeNode) -> None:
        cur = root
        while cur:
            if cur.left:
                next = node = cur.left
                while node.right:
                    node = node.right
                node.right = cur.right
                cur.left = None
                cur.right = next
            cur = cur.right

