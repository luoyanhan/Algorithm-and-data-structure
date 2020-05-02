# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = list()
        self.inorder_left(root)

    def inorder_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left


    def next(self) -> int:
        """
        @return the next smallest number
        """
        min_num = self.stack.pop()
        if min_num.right:
            self.inorder_left(min_num.right)
        return min_num.val


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0