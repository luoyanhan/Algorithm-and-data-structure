# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root):
        mid_list = list()
        stack = list()
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                mid_list.append(node)
                node = node.right
        loc1 = None
        loc2 = None
        for idx in range(1, len(mid_list)):
            pre_node, cur_node = mid_list[idx-1], mid_list[idx]
            if pre_node.val > cur_node.val:
                if loc1 is None:
                    loc1 = idx-1
                else:
                    loc2 = idx
        if loc2 is None:
            node1, node2 = mid_list[loc1], mid_list[loc1+1]
        else:
            node1, node2 = mid_list[loc1], mid_list[loc2]
        node1.val, node2.val = node2.val, node1.val


class Solution:
    def recoverTree(self, root):
        stack = list()
        node = root
        pre_node = None
        node1 = None
        node2 = None
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if pre_node and pre_node.val > node.val:
                    if node2 is None:
                        node1 = pre_node
                        node2 = node
                    else:
                        node2 = node
                pre_node = node
                node = node.right
        node1.val, node2.val = node2.val, node1.val