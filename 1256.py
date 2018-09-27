import math

class Solution:
    """
    @param n: a positive integer
    @return: the nth digit of the infinite integer sequence
    """
    def findNthDigit(self, n):
        
        digit, ith, base = 1, 1, 9
        
        while n > base * digit:
            n -= base * digit
            digit += 1
            ith *= 10
            base *= 10
        
        return int(str(ith + (n - 1) // digit)[(n - 1) % digit])