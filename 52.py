class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        n = len(nums)
        last_num = nums[-1]
        last_i = n - 1
        for i, num in enumerate(nums[:-1][::-1]):
            if num < last_num:
                res = nums[n - i - 2:]
                min_num = last_num
                for x in res:
                    if x > num:
                        min_num = min(min_num, x)
                res.remove(min_num)
                return nums[:n - i - 2] + [min_num] + sorted(res)
            last_i, last_num = n - i - 2, num
            
        return nums[::-1]