class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        
        if not nums:
            return 0
    
        ps = [0] * (len(nums) + 1)
        
        for i in range(1, len(nums) + 1):
            ps[i] = ps[i-1] + nums[i-1]
        
        
        ps2idx = dict()
        
        for idx, pfx_sum in enumerate(ps):
            ps2idx[pfx_sum] = ps2idx[pfx_sum] + 1 if pfx_sum in ps2idx else 1
        
        result = 0
        for idx, pfx_sum in enumerate(ps):
            ps2idx[pfx_sum] -= 1
            if pfx_sum + k in ps2idx:
                result += ps2idx[pfx_sum+k]
            
        return result
        