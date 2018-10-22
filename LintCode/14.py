class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        
        left = 0
        right = len(nums) - 1
        
        while right != left:
            mid = (left + right) // 2
            if nums[mid] == target:
                while mid > 0 and nums[mid - 1] == nums[mid]:
                    mid -= 1
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                if left == mid:
                    left += 1
                else:
                    left = mid
        
        return -1