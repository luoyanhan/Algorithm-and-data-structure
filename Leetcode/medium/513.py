# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        q = [root]
        tmp = list()
        depth = 1
        while q:
            for i in range(len(q)):
                top = q.pop(0)
                tmp.append([top.val, depth])
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            depth += 1
        depth -= 1
        for each in tmp:
            if each[1] == depth:
                return each[0]

class Solution:
    def findBottomLeftValue(self, root):
        q = [root]
        while q:
            top = q.pop(0)
            if top.right:
                q.append(top.right)
            if top.left:
                q.append(top.left)
        return top.val


