class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        
        t = list(t)
        
        for ss in s:
            if ss not in t:
                return False
            t.remove(ss)
        
        if not t:
            return True
            
        return False
