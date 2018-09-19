class Solution:
    """
    @param nums: the arrays
    @param k: the distance of the same number
    @return: the ans of this question
    """
    def sameNumber(self, nums, k):
        for i, num in enumerate(nums[1:]):
            if num in nums[:i+1]:  # get previous numbers
                if nums[:i+1][::-1].index(num) < k - 1:
                    return 'YES'
            
        return 'NO'