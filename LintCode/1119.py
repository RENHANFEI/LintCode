class Solution:
    """
    @param nums: an integer array
    @return: the maximum product
    """
    def maximumProduct(self, nums):
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])

# class Solution:
#     """
#     @param nums: an integer array
#     @return: the maximum product
#     """
#     def maximumProduct(self, nums):
        
#         n = len(nums)
#         ans = nums[0] * nums[1] * nums[2]
        
#         for i in range(n - 2):
#             for j in range(i + 1, n - 1):
#                 for k in range(j + 1, n):
#                     ans = max(ans, nums[i] * nums[j] * nums[k])
                    
#         return ans
        
