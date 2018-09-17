class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits)):
            cur = digits[-i-1] + carry
            digits[-i-1] = cur % 10
            carry = cur // 10
            if carry == 0:
                break
            
        if carry == 1:
            print(digits)
            digits.insert(0, carry)
            print(digits)
        
        return digits

sol = Solution()

x = [9,9]
print(sol.plusOne(x))