class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        if not nums:
            return 0
            
        min_num = min(nums)
        max_num = max(nums)
        
        while min_num + 1e-6 < max_num:
            mid = (min_num + max_num) / 2
            if self.valid_average(nums, mid, k):
                min_num = mid
            else:
                max_num = mid
                
        return min_num
            
            
    def valid_average(self, nums, mid, k):
        subsum = 0
        presum = 0
        min_presum = 0
        
        for i, num in enumerate(nums):
            subsum += num - mid
            
            if i >= k - 1 and subsum >= 0:
                return True
                
            if i >= k:
                presum += nums[i - k] - mid
                min_presum = min(min_presum, presum)
                if subsum - min_presum >= 0:
                    return True
                    
        return False

# class Solution:
#     """
#     @param nums: an array with positive and negative numbers
#     @param k: an integer
#     @return: the maximum average
#     """
#     def maxAverage(self, nums, k):
#         if not nums:
#             return 0
        
#         presum = [0] * (len(nums) + 1)
        
#         for i, num in enumerate(nums):
#             presum[i + 1] = presum[i] + num
        
#         max_average = sum(nums[:k]) / k
#         for i in range(len(nums) - k + 1):
#             for j in range(i + k, len(nums) + 1):
#                 max_average = max(max_average, (presum[j] - presum[i]) / (j - i))
                
#         return max_average
            
        
        
# class Solution:
#     """
#     @param nums: an array with positive and negative numbers
#     @param k: an integer
#     @return: the maximum average
#     """
#     def maxAverage(self, nums, k):
        
#         n = len(nums)
#         ans = sum(nums[:k]) / k
        
#         for start in range(n - k + 1):
#             for end in range(start + k - 1, n):
#                 subarray = nums[start:end + 1]
#                 average = sum(subarray) / (end - start + 1)
#                 ans = max(ans, average)
                
#         return ans