class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):

        for i, n in enumerate(nums):
            if n == 0:
                return [i, i]
            s = n
            for j, m in enumerate(nums[i + 1:]):
                s += m
                if s == 0:
                    return [i, j + i + 1]
                
        
# class Solution:
#     """
#     @param nums: A list of integers
#     @return: A list of integers includes the index of the first number and the index of the last number
#     """
#     def subarraySum(self, nums):
        
#         if not nums:
#             return []
            
#         result = []
    
#         pre_sums = [0] * (len(nums) + 1)
        
#         for i in range(1, len(nums) + 1):
#             pre_sums[i] = pre_sums[i-1] + nums[i-1]
        
#         pre_sums_dict = dict()
#         for i, ps in enumerate(pre_sums):
#             if ps in pre_sums_dict:
#                 pre_sums_dict[ps].append(i)
#             else:
#                 pre_sums_dict[ps] = [i]
        
#         res = []
#         k = 0
#         for i, ps in enumerate(pre_sums):
#             pre_sums_dict[ps].remove(i)
#             if ps + k in pre_sums_dict and pre_sums_dict[ps + k]:
#                 res += [(i, j-1) for j in pre_sums_dict[ps + k]]
        
#         print(res)