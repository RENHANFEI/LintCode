class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        if x < 1:
            return 0
            
        l, r = 1, x//2 + 1
        
        while r > l:
            mid = (l + r) // 2
            square = mid * mid
            if square > x:
                r = mid - 1
            elif square < x:
                l = mid + 1
            else:
                return mid
                
        if r * r > x:
            return r - 1
        return r