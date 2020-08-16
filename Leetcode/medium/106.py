# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        length = len(inorder)
        idx = {node: i for i, node in enumerate(inorder)}
        def build(postleft, postright, inleft, inright):
            if inleft > inright:
                return None
            root = TreeNode(postorder[postright])
            index_in = idx[postorder[postright]]
            length_left = index_in - inleft
            root.left = build(postleft, postleft+length_left-1, inleft, index_in-1)
            root.right = build(postleft + length_left, postright - 1, index_in + 1, inright)
            return root
        return build(0, length-1, 0, length-1)