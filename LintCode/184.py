from functools import cmp_to_key

class Solution:
    """
    @param nums: A list of non negative integers
    @return: A string
    """
    def largestNumber(self, nums):
        
        str_nums = [str(num) for num in nums]
        str_nums.sort(key=cmp_to_key(lambda x, y: 
            1 if str(x) + str(y) < str(y) + str(x) else -1))
        
        largest = ''.join(str_nums)
        
        while largest[0] == '0':
            largest = largest[1:]
            if not largest:
                return '0'
            
        return largest