class Solution:
    """
    @param nums: an array
    @return: the shortest subarray's length
    """
    def findUnsortedSubarray(self, nums):
        sorted_nums = sorted(nums)
        
        if sorted_nums == nums:
            return 0
        
        start = 0
        for start in range(len(nums)):
            if sorted_nums[start] != nums[start]:
                break
            
        end = len(nums) - 1
        for end in range(len(nums))[::-1]:
            if sorted_nums[end] != nums[end]:
                break
            
        return end - start + 1
        
