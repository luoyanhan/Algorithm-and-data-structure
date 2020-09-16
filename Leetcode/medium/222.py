# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def get_depth(root):
            res = 0
            node = root
            while node:
                res += 1
                node = node.left
            return res
        def exist(idx, depth, node):
            left = 0
            right = 2**(depth-1) - 1
            for i in range(depth-1):
                mid = (left + right)//2
                if idx > mid:
                    node = node.right
                    left = mid + 1
                else:
                    node = node.left
                    right = mid
            return not node is None
        if not root:
            return 0
        d = get_depth(root)
        if d == 1:
            return 1
        left = 1
        right = 2**(d-1) - 1
        while left <= right:
            mid = (left+right)//2
            if exist(mid, d, root):
                left = mid+1
            else:
                right = mid-1
        return left + 2**(d-1)-1

