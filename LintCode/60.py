class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        if not A or target <= A[0]:
            return 0
            
        if target > A[-1]:
            return len(A)
            
        l = 0
        r = len(A) - 1
        while l < r:
            mid = (l + r) // 2
            if A[mid] > target:
                r = mid - 1
            elif A[mid] < target:
                l = mid + 1
            else:
                return mid
                
        if A[r] < target:
            return r + 1
        else:
            return r
        
