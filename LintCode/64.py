class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        if not B:
            return A
        
        idxA = m - 1
        idxB = n - 1
        idx = m + n - 1
        
        while idxA >= 0 and idxB >= 0:
            if A[idxA] >= B[idxB]:
                A[idx] = A[idxA]
                idxA -= 1
                idx -= 1
            else:
                A[idx] = B[idxB]
                idxB -= 1
                idx -= 1
                
        while idxA >= 0:
            A[idx] = A[idxA]
            idxA -= 1
            idx -= 1
            
        while idxB >= 0:
            A[idx] = B[idxB]
            idxB -= 1
            idx -= 1
            
        return A