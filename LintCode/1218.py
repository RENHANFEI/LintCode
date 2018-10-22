class Solution:
    """
    @param num: an integer
    @return: the complement number
    """
    def findComplement(self, num):
        ans = 0
        digit = 1
        while num > 0:
            ans += abs(num % 2 - 1) * digit
            num //= 2
            digit *= 2
            
        return ans
