class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        if not A:
            return B
        
        if not B:
            return A
            
        ans = []
        a, b = 0, 0
        n_A, n_B = len(A), len(B)
        
        while a < n_A and b < n_B:
            while a < n_A and b < n_B and A[a] <= B[b]:
                ans.append(A[a])
                a += 1
            while a < n_A and b < n_B and A[a] > B[b]:
                ans.append(B[b])
                b += 1
                
        while a < n_A:
            ans.append(A[a])
            a += 1
        
        while b < n_B:
            ans.append(B[b])
            b += 1
            
        return ans
        
        
