"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        
        if not root:
            return None
        
        if self.findN(root, n - root.val):
            return [root.val, n - root.val]
        
        if root.left:
            return self.twoSum(root.left, n)
            
        if root.right:
            return self.twoSum(root.right, n)
    
            
    def findN(self, root, n):
        if not root:
            return False
        if root.val == n:
            return True
        if root.val > n:
            return self.findN(root.left, n)
        if root.val < n:
            return self.findN(root.right, n)