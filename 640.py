''' 97.47% dp '''
class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        ls, lt = len(s), len(t)
        
        if abs(ls - lt) > 1:
            return False
            
        d = [[0] * (lt + 1) for _ in range(2)]
        
        for j in range(lt + 1):
            d[0][j] = j
        
        for i in range(1, ls + 1):
            d[i%2][0] = i
            for j in range(max(i-1, 1), min(i + 2, lt + 1)):
                
                d[i%2][j] = min(d[(i-1)%2][j-1] + (0 if s[i-1] == t[j-1] else 1),\
                        d[i%2][j-1]+1, d[(i-1)%2][j]+1)
        
        return d[ls%2][lt] == 1

''' 97.74% '''
# class Solution:
#     """
#     @param s: a string
#     @param t: a string
#     @return: true if they are both one edit distance apart or false
#     """
#     def isOneEditDistance(self, s, t):
#         if s == t:
#             return False
        
#         if len(s) > len(t):
#             longer, shorter = s, t
#         else:
#             longer, shorter = t, s
            
#         if len(longer) - len(shorter) > 1:
#             return False
            
#         for i in range(len(shorter)):
#             if longer[i] == shorter[i]:
#                 continue
            
#             if shorter[i:] == longer[i+1:]:
#                 return True
            
#             if shorter[i+1:] == longer[i+1:]:
#                 return True
                
#             return False
            
#         return True
            
''' 100% '''
# class Solution:
#     """
#     @param s: a string
#     @param t: a string
#     @return: true if they are both one edit distance apart or false
#     """
#     def isOneEditDistance(self, s, t):
        
#         if abs(len(s) - (len(t))) > 1:
#             return False
            
#         if len(s) > len(t):
#             longer = s
#             shorter = t
#         else:
#             longer = t
#             shorter = s
        
#         if len(shorter) == 0:
#             if len(longer) == 1:
#                 return True
#             return False
        
#         cnt = 0
#         flag = 0
        
#         for i in range(len(longer) - 1):
#             if longer[i+flag] != shorter[i]:
#                 if cnt == 1:
#                     return False
#                 if longer[i+1] == shorter[i+1]:
#                     if len(longer) - len(shorter) == 1:
#                         return False
#                     cnt += 1
#                     continue
#                 if longer[i+1] == shorter[i]:
#                     flag += 1
#                     cnt += 1
        
#         if cnt == 1:
#             if longer[-1] != shorter[-1]:
#                 return False
#             return True
        
#         if cnt == 0:
#             if longer[-1] != shorter[-1]:
#                 return True
                
#         return False