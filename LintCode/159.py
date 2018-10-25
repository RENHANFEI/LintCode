class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        if not nums:
            return
        
        if len(nums) == 1:
            return nums[0]
            
        l, r = 0, len(nums) - 1
        
        while l < r:
            
            if nums[l] <= nums[r]:
                return nums[l]
            
            if r - l == 1:
                return nums[r] if nums[r] <= nums[l] else nums[l]
            
            mid = (l + r) // 2
            if nums[mid] > nums[l]:
                l = mid + 1
            else:   # mid < r:
                r = mid
