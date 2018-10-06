class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        result = 0
        
        while n != 0:
            result += n // 5
            n = n // 5
            
        return result