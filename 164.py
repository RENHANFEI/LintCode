"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @paramn n: An integer
    # @return: A list of root
    def generateTrees(self, n):
        return self.dfs(1, n)
    
    def dfs(self, start, end):
        if start > end:
            return [None]
        res = []
        for root_val in range(start, end + 1):
            left_tree = self.dfs(start, root_val - 1)
            right_tree = self.dfs(root_val + 1, end)
            for i in left_tree:
                for j in right_tree:
                    root = TreeNode(root_val)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res