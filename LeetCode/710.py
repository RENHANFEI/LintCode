import random

class Solution:

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.N = N
        self.blacklist = set(blacklist)
        if N < len(blacklist) * 5:
            self.whitelist = list(set(range(N)) - self.blacklist)
        else:
            self.whitelist = None

    def pick(self):
        """
        :rtype: int
        """
        if self.whitelist:
            return random.choice(self.whitelist)
        else:
            num = random.randint(0, self.N - 1)
            while num in self.blacklist:
                num = random.randint(0, self.N - 1)
            return num
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()