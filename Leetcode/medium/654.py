# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        def get_max(nums, length):
            if length == 1:
                return nums[0], 0
            elif length > 1:
                max_index = 0
                for i in range(1, length):
                    if nums[i] > nums[max_index]:
                        max_index = i
                return nums[max_index], max_index
        def inner(nums):
            if not nums:
                return None
            max_num, max_index = get_max(nums, len(nums))
            cur = TreeNode(max_num)
            cur.left = inner(nums[:max_index])
            cur.right = inner(nums[max_index+1:])
            return cur
        return inner(nums)

class Solution:
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        max_num = max(nums)
        max_index = nums.index(max_num)
        cur = TreeNode(max_num)
        cur.left = self.constructMaximumBinaryTree(nums[:max_index])
        cur.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        return cur

