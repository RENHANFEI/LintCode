class Solution:
    """
    @param s: a string
    @param t: a string
    @return: the letter that was added in t
    """
    def findTheDifference(self, s, t):
        s_list = list(s)
        t_list = list(t)
        
        for ss in s_list:
            t_list.pop(t_list.index(ss))
            
        return t_list[0]