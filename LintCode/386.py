class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        
        if k == 0:
            return 0

        ans = 0
        cur_string = ""
        num_ch = 0
        
        for i, ss in enumerate(s):
            if ss in cur_string:
                cur_string += ss
            else:
                if num_ch >= k: # surpass
                    ans = max(ans, len(cur_string))
                    while num_ch >= k:
                        cur_string = cur_string[1:]
                        num_ch = len(set(cur_string))
                cur_string += ss
                num_ch += 1
        
        ans = max(ans, len(cur_string))
        
        return ans