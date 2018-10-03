class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def findMissing(self, nums):
        
        nums.sort()
        
        for i, n in enumerate(nums):
            if i != n:
                return i
        
        return i + 1