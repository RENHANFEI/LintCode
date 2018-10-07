class Solution:
    """
    @param nums: The number array
    @return: Return the single number
    """
    def getSingleNumber(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        
        if nums[n // 2] == nums[n - n // 2]:
            if n // 2 % 2 == 0:
                return self.getSingleNumber(nums[n - n // 2 + 1:])
            else:
                return self.getSingleNumber(nums[: n // 2])
        else:
            if n // 2 % 2 == 0:
                if nums[n // 2] == nums[n // 2 - 1]:
                    return self.getSingleNumber(nums[: n // 2 - 1])
                else:
                    print(nums[n // 2 % 2:])
                    return self.getSingleNumber(nums[n // 2:])
            else:
                if nums[n // 2] == nums[n // 2- 1]:
                    return self.getSingleNumber(nums[n // 2 + 1:])
                else:
                    return self.getSingleNumber(nums[: n // 2])
                