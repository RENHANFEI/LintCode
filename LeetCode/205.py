class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True

        ch_dict = dict()
        values = set()

        i = 0
        while i < len(s):
            if s[i] in ch_dict:
                if ch_dict[s[i]] != t[i]:
                    return False
            else:
                if t[i] in values:
                    return False
                ch_dict[s[i]] = t[i]
                values.add(t[i])
            i += 1

        return True

sol = Solution()
s = 'egg'
t = 'add'

s = 'paper'
t = 'title'

s = 'ab'
t = 'aa'

print(sol.isIsomorphic(s, t))