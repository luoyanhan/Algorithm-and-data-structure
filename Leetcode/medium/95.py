# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int):
        def gen(start, end):
            if start > end:
                return [None]
            all_trees = list()
            for i in range(start, end+1):
                lefts = gen(start, i-1)
                rights = gen(i+1, end)
                for left in lefts:
                    for right in rights:
                        cur = TreeNode(i)
                        cur.left = left
                        cur.right = right
                        all_trees.append(cur)
            return all_trees
        return gen(1, n) if n else list()


Solution().generateTrees(3)
