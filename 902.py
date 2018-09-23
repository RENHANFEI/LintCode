"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        asc_nodes = []
        self.inorder(root, asc_nodes)
        
        return asc_nodes[k - 1]
        
        
    def inorder(self, tree, nodes):
        if tree == None:
            return
        
        self.inorder(tree.left, nodes)
        nodes.append(tree.val)
        self.inorder(tree.right, nodes)
        