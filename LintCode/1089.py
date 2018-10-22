class Solution:
    """
    @param s: the given string
    @return: whether this string is valid
    """
    def checkValidString(self, s):
        if not s:
            return True
            
        low = 0
        high = 0
        
        for ss in s:
            
            if ss == "(":
                low += 1
                high += 1
            elif ss == ")":
                if low > 0:
                    low -= 1
                high -= 1
            else:
                if low > 0:
                    low -= 1
                high += 1
            
            if high < 0:
                return False
                
        return low == 0


# class Solution:
#     """
#     @param s: the given string
#     @return: whether this string is valid
#     """
#     def checkValidString(self, s):
#         if not s:
#             return True
            
#         stack = []
#         stars = 0
        
#         for ss in s:
#             if ss == '(':
#                 if stack:
#                     stack.append(ss)
#             elif ss == ')':
#                 if not stack:
#                     return False
#                 ch = stack.pop()
#                 if not stack:
#                     if stars > 0:
#                         stack.append('*')
#                         stars -= 1
#             else:   # '*'
#                 if not stack:
#                     continue
#                 if stack[-1] == '(':
#                     stars += 1
                    
#         if stack == ["*"]:
#             stack = []
            
#         if stars >= len(stack):
#             stack = []
#             stars = 0
            
#             for ss in s[::-1]:
#                 if ss == ')':
#                     if stack:
#                         stack.append(ss)
#                 elif ss == '(':
#                     if not stack:
#                         return False
#                     ch = stack.pop()
#                     if not stack:
#                         if stars > 0:
#                             stack.append('*')
#                             stars -= 1
#                 else:   # '*'
#                     if not stack:
#                         continue
#                     if stack[-1] == ')':
#                         stars += 1
            
#             if stack == ["*"]:
#                 stack = []
            
#             if stars >= len(stack):
#                 return True
        
#         return False
