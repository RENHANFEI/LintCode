from collections import Counter
class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        num_a = 0
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                num_a += 1
                
        right_digits = Counter(secret) - Counter(guess)
        num_b = len(secret) - sum(right_digits.values()) - num_a
        
        return "{}A{}B".format(num_a, num_b)
        

secret = "1807"
guess = "7810"
sol = Solution()

print(sol.getHint(secret, guess))