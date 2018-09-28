''' max 3^N '''
class Solution:
    
    import math
    """
    @param n: an integer
    @return: if n is a power of three
    """
    def isPowerOfThree(self, n):
        if n < 1:
            return False
        
        max_exponent = math.log(0x7fffffff) // math.log(3)
            
        return 3 ** max_exponent % n == 0


''' log3(n) '''
# class Solution:
    
#     import math
#     """
#     @param n: an integer
#     @return: if n is a power of three
#     """
#     def isPowerOfThree(self, n):
#         if n < 1:
#             return False
            
#         k = math.log(n) / math.log(3)
#         if round(k, 12) - int(k) == 0:
#             return True
#         return False
        

''' Recursion Time: 100% '''
# class Solution:
#     """
#     @param n: an integer
#     @return: if n is a power of three
#     """
#     def isPowerOfThree(self, n):
#         if n == 1:
#             return True
#         if n % 3 != 0 or n < 1:
#             return False
            
#         return self.isPowerOfThree(n / 3)