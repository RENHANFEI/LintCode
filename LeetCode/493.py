# class Solution(object):
#     def reversePairs(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         ans = 0
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if nums[i] > 2 * nums[j]:
#                     ans += 1
                    
#         return ans


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.cnt = 1
        self.left = left
        self.right = right

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        root = None
        ans = 0
        for num in nums:
            ans += self.search(root, 2 * num + 1)
            root = self.insert(root, num)
            
        return ans
        
    
    def insert(self, root, val):
        if not root:
            return Node(val)
        
        if root.val > val:
            root.left = self.insert(root.left, val)
        elif root.val < val:
            root.cnt += 1
            root.right = self.insert(root.right, val)
        else:
            root.cnt += 1
            
        return root
    
    def search(self, root, val):
        if not root:
            return 0
        if val == 1:
            print((root.val, val))
        if val > root.val:
            return self.search(root.right, val)
        elif val < root.val:
            return root.cnt + self.search(root.left, val)
        else:
            return root.cnt
    
        
    
sol = Solution()
x = [1, 3, 2, 3, 1]
sol.reversePairs(x)