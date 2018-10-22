class Solution:
    """
    @param S: a String consists of a and b
    @return: the longest of the longest string that meets the condition
    """
    def getAns(self, S):
        if not S:
            return 0
            
        diffs = dict()    # diffs[n] max length for numA - numB = n
        cntA = 0
        cntB = 0
        ans = 0
        diffs[0] = 0
        
        for i, s in enumerate(S):
            if s == 'A':
                cntA += 1
            else:
                cntB += 1
                
            diff = cntA - cntB
            if diff in diffs:
                ans = max(ans, i + 1 - diffs[diff])
            else:
                diffs[diff] = i + 1
            
        return ans
        
        

# class Solution:
#     """
#     @param S: a String consists of a and b
#     @return: the longest of the longest string that meets the condition
#     """
#     def getAns(self, S):
        
#         if not S or len(S) == 1:
#             return 0
        
#         ans = 0
#         numAB = []  # numAB[i][j] = (numA, numB) from i to i+j
        
#         for i, s in enumerate(S):
#             AB = [1, 0] if s == 'A' else [0, 1]
#             numAB.append([AB])
#             for j in range(i):
#                 nums = numAB[j]
#                 num = nums[-1]
#                 AB = [num[0] + 1, num[1]] if s == 'A' else [num[0], num[1] + 1]
#                 if AB[0] == AB[1] and AB[0] * 2 > ans:
#                     ans = AB[0] * 2
#                 nums.append(AB)
                
#         return ans