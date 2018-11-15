class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        start, end, ans = 0, 1, 1
        subset = {s[0]: 0}    # key:letter, value:idx
        
        while start < len(s) and end < len(s):
            if s[end] not in subset or subset[s[end]] < start:
                subset[s[end]] = end
                ans = max(ans, end - start + 1)
            else:
                start = subset[s[end]] + 1
                subset[s[end]] = end
            end += 1
            
        return ans
            
            
        