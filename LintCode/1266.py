''' ascii '''
class Solution:
    """
    @param s: a string
    @param t: a string
    @return: the letter that was added in t
    """
    def findTheDifference(self, s, t):
        ascii_sum = 0
        
        for tt in t:
            ascii_sum += ord(tt)
        
        for ss in s:
            ascii_sum -= ord(ss)
            
        return chr(ascii_sum)


''' First Sol '''
# class Solution:
#     """
#     @param s: a string
#     @param t: a string
#     @return: the letter that was added in t
#     """
#     def findTheDifference(self, s, t):
#         s_list = list(s)
#         t_list = list(t)
        
#         for ss in s_list:
#             t_list.pop(t_list.index(ss))
            
#         return t_list[0]