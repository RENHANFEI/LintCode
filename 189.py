class Solution:
    """
    @param A: An array of integers
    @return: An integer
    """
    def firstMissingPositive(self, A):
        
        if not A:
            return 1
            
        A.sort()
        
        if A[-1] <= 0 or A[0] > 1:
            return 1
        
        for i, a in enumerate(A):
            if a >= 0 and i < len(A) - 1 and A[i+1] != a and A[i+1] != a + 1:
                return a + 1
        
        return a + 1
