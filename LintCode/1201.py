class Solution:
    """
    @param nums: an array
    @return: the Next Greater Number for every element
    """
    def nextGreaterElements(self, nums):
        if not nums:
            return []
            
        len_nums = len(nums)
        
        if len_nums == 1:
            return [-1]
        
        num_max = max(nums)
        nums += nums
        result = [-1] * len_nums
        
        unknown_stack = []
        for i, num in enumerate(nums):
            if not unknown_stack:
                unknown_stack.append((num, i))
            else:
                while unknown_stack and unknown_stack[-1][0] < num:
                    j = unknown_stack.pop()[1]
                    if j < len_nums:
                        result[j] = num
                unknown_stack.append((num, i))
                
        return result


# class Solution:
#     """
#     @param nums: an array
#     @return: the Next Greater Number for every element
#     """
#     def nextGreaterElements(self, nums):
#         if not nums:
#             return []
            
#         len_nums = len(nums)
        
#         if len_nums == 1:
#             return [-1]
        
#         num_max = max(nums)
#         nums += nums
        
#         result = [-1] * len_nums
        
#         for i in range(len_nums):
#             if nums[i] == num_max:
#                 continue
#             for num in nums[i+1: ]:
#                 if num > nums[i]:
#                     result[i] = num
#                     break
                
#         return result