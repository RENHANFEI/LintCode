class Solution:
    """
    @param A: an array
    @return: the number of arithmetic slices in the array A.
    """
    def numberOfArithmeticSlices(self, A):
        if len(A) < 3:
            return 0
            
        diff = A[1] - A[0]
        pre = A[1]
        valid = 2
        ans = 0
        
        for a in A[2:]:
            if a - pre == diff:
                valid += 1
            else:
                if valid >= 3:
                    ans += (valid - 1) * (valid - 2) // 2
                diff = a - pre
                valid = 2
            pre = a
            
        if valid >= 3:
            ans += (valid - 1) * (valid - 2) // 2
            
        return ans
        
