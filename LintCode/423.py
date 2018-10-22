class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        pre_parts = ['(', '{', '[']
        post_parts = [')', '}', ']']
        
        stack = []
        
        for ch in s:
            if ch in pre_parts:
                stack.append(ch)
            if ch in post_parts:
                if stack == []:
                    return False
                if pre_parts.index(stack.pop()) != post_parts.index(ch):
                    return False
        
        if stack != []:
            return False
            
        return True
