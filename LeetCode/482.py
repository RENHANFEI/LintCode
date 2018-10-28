class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        ans = []
        i = 0
        count = 0

        for i, ch in enumerate(reversed(S)):
            if ch == '-':
                continue
            if ch.islower(): ch = ch.upper()
            ans.append(ch)
            count += 1
            if count == K:
                ans.append('-')
                count = 0

        if ans and ans[-1] == '-':
            ans.pop()

        return ''.join(reversed(ans))