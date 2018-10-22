class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        hash_dict = dict()
        
        for s in strs:
            s_hash = self.hashString(s)
            if s_hash in hash_dict:
                hash_dict[s_hash].append(s)
            else:
                hash_dict[s_hash] = [s]
        
        ans = []
        for hash_val, ss in hash_dict.items():
            if len(ss) > 1:
                ans += ss
        
        return ans
    
    def hashString(self, s):
        val = 0
        for ch in s:
            val += 26 ** (ord(ch) - ord('a'))
        return val