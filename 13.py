class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        
        l = len(target)
        
        for i in range(len(source) - l + 1):
            if source[i:i+l] == target:
                return i
        return -1