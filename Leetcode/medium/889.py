# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre, post):
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
        root.right = self.constructFromPrePost(pre[L+1:], post[L: -1])
        return root

class Solution:
    def constructFromPrePost(self, pre, post):
        def make(l0, l1, N):
            if not N:
                return None
            root = TreeNode(pre[l0])
            if N == 1:
                return root
            L = 0
            while L < N:
                if pre[l0+1] == post[l1-1+L]:
                    break
                L += 1
            root.left = make(l0+1, l1, L)
            root.right = make(l0+1+L, l1+L, N-L-1)   #N-L-1的1容易忽略
            return root
        return make(0, 0, len(pre))




