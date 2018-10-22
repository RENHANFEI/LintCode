class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        A = list(A)
        
        for b in B:
            if b not in A:
                return False
            A.remove(b)
            
        return True
