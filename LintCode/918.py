class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def threeSumSmaller(self, nums, target):
        
        result = 0
        
        nums.sort()
        
        for i, n in enumerate(nums):
            if n >= target and i < len(nums) - 1 and nums[i+1] >= 0:
                break
            for j, m in enumerate(nums[i+1:]):
                s = n + m
                if s >= target and j + i + 1 < len(nums) - 1 and nums[j+i+2] >= 0:
                    break
                for k in nums[i+j+2:]:
                    if s + k < target:
                        result += 1
                    else:
                        break
                    
        return result