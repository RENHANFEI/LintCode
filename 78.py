class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for s in strs[1:]:
            
            length = min(len(prefix), len(s))
            flag = False
            for i in range(min(len(prefix), len(s))):
                if prefix[i] != s[i]:
                    flag = True
                    break
            if flag:
                prefix = prefix[:i]
            else:
                prefix = prefix[:length]
        
        return prefix
