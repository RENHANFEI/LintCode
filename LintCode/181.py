class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: An integer
    """
    def bitSwapRequired(self, a, b):
        
        x = a^b
        result = 0
        
        for i in range(32):
            if x & (1 << i) != 0:
                result += 1
                
        return result
        
