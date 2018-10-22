class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        if n % 2 == 0:
            return (self.findKth(A, B, n // 2) + self.findKth(A, B, n // 2 + 1))/2
        else:
            return self.findKth(A, B, (n + 1) // 2)
    
    def findKth(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])
            
        a = A[k // 2 - 1] if k // 2 <= len(A) else None
        b = B[k // 2 - 1] if k // 2 <= len(B) else None
        
        if b == None or (a != None and a < b):
            return self.findKth(A[k // 2:], B, k - k // 2)
        return self.findKth(A, B[k // 2:], k - k // 2)