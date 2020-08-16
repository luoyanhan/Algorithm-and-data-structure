# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        length = len(inorder)
        idx = {val: i for i, val in enumerate(inorder)}
        def build(preleft, preright, inleft, inright):
            if preleft > preright:
                return None
            root = TreeNode(preorder[preleft])
            size_left = idx[preorder[preleft]] - inleft
            root.left = build(preleft+1, preleft+size_left, inleft, idx[preorder[preleft]]-1)
            root.right = build(preleft+size_left+1, preright, idx[preorder[preleft]]+1, inright)
            return root
        return build(0, length-1, 0, length-1)