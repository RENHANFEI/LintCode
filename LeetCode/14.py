class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = []
        for chs in zip(*strs):
            if len(set(chs)) > 1:
                break
            ans.append(chs[0])
            
        return ''.join(ans)

# class Solution:
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
        
#         if not strs:
#             return ""
        
#         ans = strs[0]
        
#         for s in strs[1:]:
#             i = 0
#             while i < len(ans) and i < len(s):
#                 if ans[i] != s[i]: break
#                 i += 1
#             ans = ans[:i]
                    
#         return ans
                    
#         