"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        if root == None:
            return []
            
        if root.left == root.right == None:
            return [str(root.val)]
        
        self.res = []
        root_path = str(root.val)
        
        if root.left != None:
            self.findPath(root.left, root_path)
        
        if root.right != None:
            self.findPath(root.right, root_path)
        
        return self.res
        
        
    def findPath(self, root, pre_path):
        if root.left == root.right == None:
            self.res.append(pre_path + "->" + str(root.val))
            return
        
        if root.left != None:
            self.findPath(root.left, pre_path + "->" + str(root.val))
        
        if root.right != None:
            self.findPath(root.right, pre_path + "->" + str(root.val))
