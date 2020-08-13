# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        if not root:
            return list()
        res = list()
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


class Solution:   #只入栈右节点
    def preorderTraversal(self, root):
        if not root:
            return list()
        res = list()
        stack = list()
        node = root
        while True:
            if node:
                res.append(node.val)
                if node.right:
                    stack.append(node.right)
                node = node.left
            else:
                if not stack:
                    return res
                else:
                    node = stack.pop()


class Solution: #莫里斯算法
    def preorderTraversal(self, root):
        if not root:
            return list()
        cur = root
        res = list()
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    res.append(cur.val)
                    pre.right = cur
                    cur = cur.left
                else:
                    cur = cur.right
                    pre.right = None
        return res


