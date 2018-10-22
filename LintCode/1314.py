class Solution:
    """
    @param n: an integer
    @return: if n is a power of two
    """
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        
        return self.isPowerOfTwo( n / 2 )
