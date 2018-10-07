class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        result = A[0]
        for a in A[1:]:
           result ^= a
        return result


# class Solution:
#     """
#     @param A: An integer array
#     @return: An integer
#     """
#     def singleNumber(self, A):
#         aa = []
#         for a in A:
#             if a in aa:
#                 aa.remove(a)
#             else:
#                 aa.append(a)
        
#         return aa[0]
