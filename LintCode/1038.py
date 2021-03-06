'''95.59%'''
class Solution:
    """
    @param J: the types of stones that are jewels
    @param S: representing the stones you have
    @return: how many of the stones you have are also jewels
    """
    def numJewelsInStones(self, J, S):
        res = 0
        for s in S:
            if s in J:
                res += 1
                
        return res

'''95.59%'''
# class Solution:
#     """
#     @param J: the types of stones that are jewels
#     @param S: representing the stones you have
#     @return: how many of the stones you have are also jewels
#     """
#     def numJewelsInStones(self, J, S):
#         res = 0
#         for j in J:
#             res += S.count(j)
            
#         return res