class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        right_to_left = {')':'(', '}':'{', ']':'['}
        
        for ch in s:
            if ch in right_to_left:
                if not stack or stack[-1] != right_to_left[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        
        if stack:
            return False
        
        return True