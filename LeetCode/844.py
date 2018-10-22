class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        S = self.backspace(S)
        T = self.backspace(T)
        
        return S == T
    
    def backspace(self, S):
        s_stack = []
        for s in S:
            if s == '#':
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(s)
        return s_stack

# class Solution:
#     def backspaceCompare(self, S, T):
#         """
#         :type S: str
#         :type T: str
#         :rtype: bool
#         """
#         S = self.backspace(S)
#         T = self.backspace(T)
        
#         return S == T
    
#     def backspace(self, S):
#         i = 0
#         while S and i < len(S):
#             if S[i] == '#' and i >= 1:
#                 S = S[:i-1] + S[i+1:]
#                 i -= 1
#             else:
#                 i += 1
                
#         while S and S[0] == '#':
#             S = S[1:]

#         return S