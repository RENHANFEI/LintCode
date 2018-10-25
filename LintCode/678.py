class Solution:
    """
    @param str: String
    @return: String
    """
    def convertPalindrome(self, s):
        idx = len(s) - 1
        
        while idx > 0:
            valid = True
            for i in range(idx // 2 + 1):
                if s[idx - i] != s[i]:
                    valid = False
                    break
            if valid:
                break
            idx -= 1
        
        return ''.join(reversed(s[idx + 1:])) + s
        
        

# class Solution:
#     """
#     @param str: String
#     @return: String
#     """
#     def convertPalindrome(self, s):
        
#         if self.isPalindrome(s):
#             return s
        
#         for i in range(1, len(s) + 1):
#             if self.isPalindrome(s[:-i]):
#                 return ''.join(reversed(s[-i:])) + s
        
#     def isPalindrome(self, s):
#         return s == ''.join(reversed(s))
