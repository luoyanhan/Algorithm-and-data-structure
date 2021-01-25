"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node):
        mapping = dict()
        def dfs(origin_node):
            if not origin_node:
                return None
            if origin_node.val in mapping:
                return mapping[origin_node.val]
            clone_node = Node(origin_node.val, list())
            mapping[origin_node.val] = clone_node
            if origin_node.neighbors:
                clone_node.neighbors = [dfs(each) for each in origin_node.neighbors]
            return clone_node
        root = dfs(node)
        return root



