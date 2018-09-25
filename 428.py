class Solution:
    """
    @param x: the base number
    @param n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        if n == 0:
            return 1
        
        if n == 1:
            return x
        
        if n == -1:
            return 1/x
            
        temp = self.myPow(x, n//2)
        
        if n % 2 == 0:
            return temp * temp
        
        else:
            return temp * temp * x