class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        if not nums:
            return 0
            
        nums.sort()
        pre_num = nums[0]
        
        i = 1
        while i < len(nums):
            if nums[i] == pre_num:
                nums.pop(i)
            else:
                pre_num = nums[i]
                i += 1
                
        return len(nums)