"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

'''DFS'''
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        if not root:
            return []
            
        ans = []
        self.dfs(root, ans, 0)
        
        return ans
        
        
    def dfs(self, node, ans, level):
        if level > len(ans) - 1:
            ans.append([])
        
        ans[level].append(node.val)
        
        if node.left:
            self.dfs(node.left, ans, level + 1)
            
        if node.right:
            self.dfs(node.right, ans, level + 1)
        
        
        
        


'''My First Solution'''
# class Solution:
#     """
#     @param root: A Tree
#     @return: Level order a list of lists of integer
#     """
#     def levelOrder(self, root):
        
#         if not root:
#             return []
        
#         queue = [[root], []]
#         idx = 0 # which queue
        
#         ans = [[]]
        
#         while queue[idx]:
#             node = queue[idx].pop(0)
#             if node.left:
#                 queue[1 - idx].append(node.left)
#             if node.right:
#                 queue[1 - idx].append(node.right)
#             ans[-1].append(node.val)
#             if not queue[idx] and queue[1 - idx]:
#                 idx = 1 - idx
#                 ans.append([])
        
#         return ans